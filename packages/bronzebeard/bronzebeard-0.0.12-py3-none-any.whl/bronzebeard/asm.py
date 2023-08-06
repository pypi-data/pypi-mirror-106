import abc
import argparse
import copy
from ctypes import c_uint32
from functools import partial
import os
import re
import struct


REGISTERS = {
    # ints  # strs    # names    # aliases
    0:  0,  '0':  0,  'x0':  0,  'zero': 0,
    1:  1,  '1':  1,  'x1':  1,  'ra':   1,
    2:  2,  '2':  2,  'x2':  2,  'sp':   2,
    3:  3,  '3':  3,  'x3':  3,  'gp':   3,
    4:  4,  '4':  4,  'x4':  4,  'tp':   4,
    5:  5,  '5':  5,  'x5':  5,  't0':   5,
    6:  6,  '6':  6,  'x6':  6,  't1':   6,
    7:  7,  '7':  7,  'x7':  7,  't2':   7,
    8:  8,  '8':  8,  'x8':  8,  's0':   8, 'fp': 8,
    9:  9,  '9':  9,  'x9':  9,  's1':   9,
    10: 10, '10': 10, 'x10': 10, 'a0':   10,
    11: 11, '11': 11, 'x11': 11, 'a1':   11,
    12: 12, '12': 12, 'x12': 12, 'a2':   12,
    13: 13, '13': 13, 'x13': 13, 'a3':   13,
    14: 14, '14': 14, 'x14': 14, 'a4':   14,
    15: 15, '15': 15, 'x15': 15, 'a5':   15,
    16: 16, '16': 16, 'x16': 16, 'a6':   16,
    17: 17, '17': 17, 'x17': 17, 'a7':   17,
    18: 18, '18': 18, 'x18': 18, 's2':   18,
    19: 19, '19': 19, 'x19': 19, 's3':   19,
    20: 20, '20': 20, 'x20': 20, 's4':   20,
    21: 21, '21': 21, 'x21': 21, 's5':   21,
    22: 22, '22': 22, 'x22': 22, 's6':   22,
    23: 23, '23': 23, 'x23': 23, 's7':   23,
    24: 24, '24': 24, 'x24': 24, 's8':   24,
    25: 25, '25': 25, 'x25': 25, 's9':   25,
    26: 26, '26': 26, 'x26': 26, 's10':  26,
    27: 27, '27': 27, 'x27': 27, 's11':  27,
    28: 28, '28': 28, 'x28': 28, 't3':   28,
    29: 29, '29': 29, 'x29': 29, 't4':   29,
    30: 30, '30': 30, 'x30': 30, 't5':   30,
    31: 31, '31': 31, 'x31': 31, 't6':   31,
}


def lookup_register(reg, compressed=False):
    if reg not in REGISTERS:
        raise ValueError('register must be a valid integer, name, or alias: {}'.format(reg))

    reg = REGISTERS[reg]

    # check for compressed instruction register, validate and apply
    if compressed:
        # must be in "common" registers: x8-x15
        if reg < 8 or reg > 15:
            raise ValueError('compressed register must be between 8 and 15: {}'.format(reg))
        # subtract 8 to get compressed, 3-bit reg value
        reg -= 8

    return reg


def r_type(rd, rs1, rs2, *, opcode, funct3, funct7):
    rd = lookup_register(rd)
    rs1 = lookup_register(rs1)
    rs2 = lookup_register(rs2)

    code = 0
    code |= opcode
    code |= rd << 7
    code |= funct3 << 12
    code |= rs1 << 15
    code |= rs2 << 20
    code |= funct7 << 25

    return code


def i_type(rd, rs1, imm, *, opcode, funct3):
    rd = lookup_register(rd)
    rs1 = lookup_register(rs1)

    if imm < -0x800 or imm > 0x7ff:
        raise ValueError('12-bit immediate must be between -0x800 (-2048) and 0x7ff (2047): {}'.format(imm))

    imm = c_uint32(imm).value & 0b111111111111

    code = 0
    code |= opcode
    code |= rd << 7
    code |= funct3 << 12
    code |= rs1 << 15
    code |= imm << 20

    return code


def s_type(rs1, rs2, imm, *, opcode, funct3):
    rs1 = lookup_register(rs1)
    rs2 = lookup_register(rs2)

    if imm < -0x800 or imm > 0x7ff:
        raise ValueError('12-bit immediate must be between -0x800 (-2048) and 0x7ff (2047): {}'.format(imm))

    imm = c_uint32(imm).value & 0b111111111111

    imm_11_5 = (imm >> 5) & 0b1111111
    imm_4_0 = imm & 0b11111

    code = 0
    code |= opcode
    code |= imm_4_0 << 7
    code |= funct3 << 12
    code |= rs1 << 15
    code |= rs2 << 20
    code |= imm_11_5 << 25

    return code


def b_type(rs1, rs2, imm, *, opcode, funct3):
    rs1 = lookup_register(rs1)
    rs2 = lookup_register(rs2)

    if imm < -0x1000 or imm > 0x0fff:
        raise ValueError('12-bit MO2 immediate must be between -0x1000 (-4096) and 0x0fff (4095): {}'.format(imm))
    if imm % 2 != 0:
        raise ValueError('12-bit MO2 immediate must be a muliple of 2: {}'.format(imm))

    imm = imm >> 1
    imm = c_uint32(imm).value & 0b111111111111

    imm_12 = (imm >> 11) & 0b1
    imm_11 = (imm >> 10) & 0b1
    imm_10_5 = (imm >> 4) & 0b111111
    imm_4_1 = imm & 0b1111

    code = 0
    code |= opcode
    code |= imm_11 << 7
    code |= imm_4_1 << 8
    code |= funct3 << 12
    code |= rs1 << 15
    code |= rs2 << 20
    code |= imm_10_5 << 25
    code |= imm_12 << 31

    return code


def u_type(rd, imm, *, opcode):
    rd = lookup_register(rd)

    if imm < -0x80000 or imm > 0x7ffff:
        raise ValueError('20-bit immediate must be between -0x80000 (-524288) and 0x7ffff (524287): {}'.format(imm))

    imm = c_uint32(imm).value & 0b11111111111111111111

    code = 0
    code |= opcode
    code |= rd << 7
    code |= imm << 12

    return code


def j_type(rd, imm, *, opcode):
    rd = lookup_register(rd)

    if imm < -0x100000 or imm > 0x0fffff:
        raise ValueError('20-bit MO2 immediate must be between -0x100000 (-1048576) and 0x0fffff (1048575): {}'.format(imm))
    if imm % 2 != 0:
        raise ValueError('20-bit MO2 immediate must be a muliple of 2: {}'.format(imm))

    imm = imm >> 1
    imm = c_uint32(imm).value & 0b11111111111111111111

    imm_20 = (imm >> 19) & 0b1
    imm_19_12 = (imm >> 11) & 0b11111111
    imm_11 = (imm >> 10) & 0b1
    imm_10_1 = imm & 0b1111111111

    code = 0
    code |= opcode
    code |= rd << 7
    code |= imm_19_12 << 12
    code |= imm_11 << 20
    code |= imm_10_1 << 21
    code |= imm_20 << 31

    return code


def a_type(rd, rs1, rs2, *, opcode, funct3, funct5, aq=0, rl=0):
    # TODO: better error message here, note that it must be explicitly 0 or 1
    aq = int(aq)
    rl = int(rl)
    if aq not in [0, 1]:
        raise ValueError('aq must be either 0 or 1')
    if rl not in [0, 1]:
        raise ValueError('rl must be either 0 or 1')

    # build aq/rl into a funct7 and defer to r_type
    funct7 = funct5 << 2 | aq << 1 | rl
    return r_type(rd, rs1, rs2, opcode=opcode, funct3=funct3, funct7=funct7)


# c.jr, c.mv, c.jalr, c.add
def cr_type(rd_rs1, rs2, *, opcode, funct4):
    rd_rs1 = lookup_register(rd_rs1)
    rs2 = lookup_register(rs2)

    code = 0
    code |= opcode
    code |= rs2 << 2
    code |= rd_rs1 << 7
    code |= funct4 << 12

    return code


# c.nop, c.addi, c.li, c.lui, c.slli
def ci_type(rd_rs1, imm, *, opcode, funct3):
    rd_rs1 = lookup_register(rd_rs1)

    if imm < -32 or imm > 31:
        raise ValueError('6-bit immediate must be between -32 (-0x20) and 31 (0x1f): {}'.format(imm))

    imm = c_uint32(imm).value & 0b111111

    imm_5 = (imm >> 5) & 0b1
    imm_4_0 = imm & 0b11111

    code = 0
    code |= opcode
    code |= imm_4_0 << 2
    code |= rd_rs1 << 7
    code |= imm_5 << 12
    code |= funct3 << 13

    return code


# CI variation
# c.addi16sp
def cis_type(rd_rs1, imm, *, opcode, funct3):
    rd_rs1 = lookup_register(rd_rs1)

    if imm < -512 or imm > 496:
        raise ValueError('6-bit MO16 immediate must be between -512 (-0x200) and 496 (0x1f0): {}'.format(imm))
    if imm % 16 != 0:
        raise ValueError('6-bit MO16 immediate must be a multiple of 16: {}'.format(imm))

    imm = imm >> 4
    imm = c_uint32(imm).value & 0b111111

    imm_9 = (imm >> 5) & 0b1
    imm_8_4 = imm & 0b11111

    code = 0
    code |= opcode
    code |= imm_8_4 << 2
    code |= rd_rs1 << 7
    code |= imm_9 << 12
    code |= funct3 << 13

    return code


# CI variation
# c.lwsp
def cls_type(rd, imm, *, opcode, funct3):
    rd = lookup_register(rd)

    if imm < 0 or imm > 252:
        raise ValueError('6-bit MO4 unsigned immediate must be between 0 (0x00) and 0xfc (252): {}'.format(imm))
    if imm % 4 != 0:
        raise ValueError('6-bit MO4 unsigned immediate must be a multiple of 4: {}'.format(imm))

    imm = imm >> 2
    imm = c_uint32(imm).value & 0b111111

    imm_7 = (imm >> 5) & 0b1
    imm_6_2 = imm & 0b11111

    code = 0
    code |= opcode
    code |= imm_6_2 << 2
    code |= rd << 7
    code |= imm_7 << 12
    code |= funct3 << 13

    return code


# c.swsp
def css_type(rs2, imm, *, opcode, funct3):
    rs2 = lookup_register(rs2)

    if imm < 0 or imm > 252:
        raise ValueError('6-bit MO4 unsigned immediate must be between 0 (0x00) and 0xfc (252): {}'.format(imm))
    if imm % 4 != 0:
        raise ValueError('6-bit MO4 unsigned immediate must be a multiple of 4: {}'.format(imm))

    imm = imm >> 2
    imm = c_uint32(imm).value & 0b111111

    imm_7_6 = (imm >> 4) & 0b11
    imm_5_2 = imm & 0b1111

    code = 0
    code |= opcode
    code |= rs2 << 2
    code |= imm_7_6 << 7
    code |= imm_5_2 << 9
    code |= funct3 << 13

    return code


# c.addi4spn
def ciw_type(rd, imm, *, opcode, funct3):
    rd = lookup_register(rd, compressed=True)

    if imm < 0 or imm > 1020:
        raise ValueError('8-bit MO4 unsigned immediate must be between 0 (0x00) and 0x3fc (1020): {}'.format(imm))
    if imm % 4 != 0:
        raise ValueError('8-bit MO4 unsigned immediate must be a multiple of 4: {}'.format(imm))

    imm = imm >> 2
    imm = c_uint32(imm).value & 0b11111111

    imm_9_6 = (imm >> 4) & 0b1111
    imm_5_4 = (imm >> 2) & 0b11
    imm_3 = (imm >> 1) & 0b1
    imm_2 = imm & 0b1

    code = 0
    code |= opcode
    code |= rd << 2
    code |= imm_3 << 5
    code |= imm_2 << 6
    code |= imm_9_6 << 7
    code |= imm_5_4 << 11
    code |= funct3 << 13

    return code


# c.lw
def cl_type(rd, rs1, imm, *, opcode, funct3):
    rd = lookup_register(rd, compressed=True)
    rs1 = lookup_register(rs1, compressed=True)

    if imm < 0 or imm > 124:
        raise ValueError('5-bit MO4 unsigned immediate must be between 0 (0x00) and 0x7c (124): {}'.format(imm))
    if imm % 4 != 0:
        raise ValueError('5-bit MO4 unsigned immediate must be a multiple of 4: {}'.format(imm))

    imm = imm >> 2
    imm = c_uint32(imm).value & 0b11111

    imm_6 = (imm >> 4) & 0b1
    imm_5_3 = (imm >> 1) & 0b111
    imm_2 = imm & 0b1

    code = 0
    code |= opcode
    code |= rd << 2
    code |= imm_6 << 5
    code |= imm_2 << 6
    code |= rs1 << 7
    code |= imm_5_3 << 10
    code |= funct3 << 13

    return code


# c.sw
def cs_type(rs1, rs2, imm, *, opcode, funct3):
    rs1 = lookup_register(rs1, compressed=True)
    rs2 = lookup_register(rs2, compressed=True)

    if imm < 0 or imm > 124:
        raise ValueError('5-bit MO4 unsigned immediate must be between 0 (0x00) and 0x7c (124): {}'.format(imm))
    if imm % 4 != 0:
        raise ValueError('5-bit MO4 unsigned immediate must be a multiple of 4: {}'.format(imm))

    imm = imm >> 2
    imm = c_uint32(imm).value & 0b11111

    imm_6 = (imm >> 4) & 0b1
    imm_5_3 = (imm >> 1) & 0b111
    imm_2 = imm & 0b1

    code = 0
    code |= opcode
    code |= rs2 << 2
    code |= imm_6 << 5
    code |= imm_2 << 6
    code |= rs1 << 7
    code |= imm_5_3 << 10
    code |= funct3 << 13

    return code


# c.sub, c.xor, c.or, c.and
def ca_type(rd_rs1, rs2, *, opcode, funct2, funct6):
    rd_rs1 = lookup_register(rd_rs1, compressed=True)
    rs2 = lookup_register(rs2, compressed=True)

    code = 0
    code |= opcode
    code |= rs2 << 2
    code |= funct2 << 5
    code |= rd_rs1 << 7
    code |= funct6 << 10

    return code


# c.beqz, c.bnez
def cb_type(rs1, imm, *, opcode, funct3):
    rs1 = lookup_register(rs1, compressed=True)

    imm = imm >> 1
    imm = c_uint32(imm).value & 0b11111111

    imm_8 = (imm >> 7) & 0b1
    imm_7_6 = (imm >> 5) & 0b11
    imm_5 = (imm >> 4) & 0b1
    imm_4_3 = (imm >> 2) & 0b11
    imm_2_1 = imm & 0b11

    code = 0
    code |= opcode
    code |= imm_5 << 2
    code |= imm_2_1 << 3
    code |= imm_7_6 << 5
    code |= rs1 << 7
    code |= imm_4_3 << 10
    code |= imm_8 << 12
    code |= funct3 << 13

    return code


# CB variation
# c.srli, c.srai, c.andi
def cbi_type(rd_rs1, imm, *, opcode, funct2, funct3):
    rd_rs1 = lookup_register(rd_rs1, compressed=True)

    imm = c_uint32(imm).value & 0b111111

    imm_5 = (imm >> 5) & 0b1
    imm_4_0 = imm & 0b11111

    code = 0
    code |= opcode
    code |= imm_4_0 << 2
    code |= rd_rs1 << 7
    code |= funct2 << 10
    code |= imm_5 << 12
    code |= funct3 << 13

    return code


# c.jal, c.j
def cj_type(imm, *, opcode, funct3):
    if imm < -2048 or imm > 2046:
        raise ValueError('11-bit MO2 immediate must be between -0x800 (-2048) and 0x7fe (2046): {}'.format(imm))
    if imm % 2 != 0:
        raise ValueError('11-bit MO2 immediate must be a muliple of 2: {}'.format(imm))

    imm = imm >> 1
    imm = c_uint32(imm).value & 0b11111111111

    imm_11 = (imm >> 10) & 0b1
    imm_10 = (imm >> 9) & 0b1
    imm_9_8 = (imm >> 7) & 0b11
    imm_7 = (imm >> 6) & 0b1
    imm_6 = (imm >> 5) & 0b1
    imm_5 = (imm >> 4) & 0b1
    imm_4 = (imm >> 3) & 0b1
    imm_3_1 = imm & 0b111

    code = 0
    code |= opcode
    code |= imm_5 << 2
    code |= imm_3_1 << 3
    code |= imm_7 << 6
    code |= imm_6 << 7
    code |= imm_10 << 8
    code |= imm_9_8 << 9
    code |= imm_4 << 11
    code |= imm_11 << 12
    code |= funct3 << 13

    return code


# RV32I Base Integer Instruction Set
LUI        = partial(u_type,   opcode=0b0110111)
AUIPC      = partial(u_type,   opcode=0b0010111)
JAL        = partial(j_type,   opcode=0b1101111)
JALR       = partial(i_type,   opcode=0b1100111, funct3=0b000)
BEQ        = partial(b_type,   opcode=0b1100011, funct3=0b000)
BNE        = partial(b_type,   opcode=0b1100011, funct3=0b001)
BLT        = partial(b_type,   opcode=0b1100011, funct3=0b100)
BGE        = partial(b_type,   opcode=0b1100011, funct3=0b101)
BLTU       = partial(b_type,   opcode=0b1100011, funct3=0b110)
BGEU       = partial(b_type,   opcode=0b1100011, funct3=0b111)
LB         = partial(i_type,   opcode=0b0000011, funct3=0b000)
LH         = partial(i_type,   opcode=0b0000011, funct3=0b001)
LW         = partial(i_type,   opcode=0b0000011, funct3=0b010)
LBU        = partial(i_type,   opcode=0b0000011, funct3=0b100)
LHU        = partial(i_type,   opcode=0b0000011, funct3=0b101)
SB         = partial(s_type,   opcode=0b0100011, funct3=0b000)
SH         = partial(s_type,   opcode=0b0100011, funct3=0b001)
SW         = partial(s_type,   opcode=0b0100011, funct3=0b010)
ADDI       = partial(i_type,   opcode=0b0010011, funct3=0b000)
SLTI       = partial(i_type,   opcode=0b0010011, funct3=0b010)
SLTIU      = partial(i_type,   opcode=0b0010011, funct3=0b011)
XORI       = partial(i_type,   opcode=0b0010011, funct3=0b100)
ORI        = partial(i_type,   opcode=0b0010011, funct3=0b110)
ANDI       = partial(i_type,   opcode=0b0010011, funct3=0b111)
SLLI       = partial(r_type,   opcode=0b0010011, funct3=0b001, funct7=0b0000000)
SRLI       = partial(r_type,   opcode=0b0010011, funct3=0b101, funct7=0b0000000)
SRAI       = partial(r_type,   opcode=0b0010011, funct3=0b101, funct7=0b0100000)
ADD        = partial(r_type,   opcode=0b0110011, funct3=0b000, funct7=0b0000000)
SUB        = partial(r_type,   opcode=0b0110011, funct3=0b000, funct7=0b0100000)
SLL        = partial(r_type,   opcode=0b0110011, funct3=0b001, funct7=0b0000000)
SLT        = partial(r_type,   opcode=0b0110011, funct3=0b010, funct7=0b0000000)
SLTU       = partial(r_type,   opcode=0b0110011, funct3=0b011, funct7=0b0000000)
XOR        = partial(r_type,   opcode=0b0110011, funct3=0b100, funct7=0b0000000)
SRL        = partial(r_type,   opcode=0b0110011, funct3=0b101, funct7=0b0000000)
SRA        = partial(r_type,   opcode=0b0110011, funct3=0b101, funct7=0b0100000)
OR         = partial(r_type,   opcode=0b0110011, funct3=0b110, funct7=0b0000000)
AND        = partial(r_type,   opcode=0b0110011, funct3=0b111, funct7=0b0000000)

# RV32M Standard Extension for Integer Multiplication and Division
MUL        = partial(r_type,   opcode=0b0110011, funct3=0b000, funct7=0b0000001)
MULH       = partial(r_type,   opcode=0b0110011, funct3=0b001, funct7=0b0000001)
MULHSU     = partial(r_type,   opcode=0b0110011, funct3=0b010, funct7=0b0000001)
MULHU      = partial(r_type,   opcode=0b0110011, funct3=0b011, funct7=0b0000001)
DIV        = partial(r_type,   opcode=0b0110011, funct3=0b100, funct7=0b0000001)
DIVU       = partial(r_type,   opcode=0b0110011, funct3=0b101, funct7=0b0000001)
REM        = partial(r_type,   opcode=0b0110011, funct3=0b110, funct7=0b0000001)
REMU       = partial(r_type,   opcode=0b0110011, funct3=0b111, funct7=0b0000001)

# RV32A Standard Extension for Atomic Instructions
LR_W       = partial(a_type,   opcode=0b0101111, funct3=0b010, funct5=0b00010)
SC_W       = partial(a_type,   opcode=0b0101111, funct3=0b010, funct5=0b00011)
AMOSWAP_W  = partial(a_type,   opcode=0b0101111, funct3=0b010, funct5=0b00001)
AMOADD_W   = partial(a_type,   opcode=0b0101111, funct3=0b010, funct5=0b00000)
AMOXOR_W   = partial(a_type,   opcode=0b0101111, funct3=0b010, funct5=0b00100)
AMOAND_W   = partial(a_type,   opcode=0b0101111, funct3=0b010, funct5=0b01100)
AMOOR_W    = partial(a_type,   opcode=0b0101111, funct3=0b010, funct5=0b01000)
AMOMIN_W   = partial(a_type,   opcode=0b0101111, funct3=0b010, funct5=0b10000)
AMOMAX_W   = partial(a_type,   opcode=0b0101111, funct3=0b010, funct5=0b10100)
AMOMINU_W  = partial(a_type,   opcode=0b0101111, funct3=0b010, funct5=0b11000)
AMOMAXU_W  = partial(a_type,   opcode=0b0101111, funct3=0b010, funct5=0b11100)

# RV32C Standard Extension for Compressed Instructions
C_ADDI4SPN = partial(ciw_type, opcode=0b00, funct3=0b000)
C_LW       = partial(cl_type,  opcode=0b00, funct3=0b010)
C_SW       = partial(cs_type,  opcode=0b00, funct3=0b110)
C_NOP      = partial(ci_type,  opcode=0b01, funct3=0b000, rd_rs1=0, imm=0)  # c.nop syntax will be special
C_ADDI     = partial(ci_type,  opcode=0b01, funct3=0b000)
C_JAL      = partial(cj_type,  opcode=0b01, funct3=0b001)
C_LI       = partial(ci_type,  opcode=0b01, funct3=0b010)
C_ADDI16SP = partial(cis_type, opcode=0b01, funct3=0b011)
C_LUI      = partial(ci_type,  opcode=0b01, funct3=0b011)
C_SRLI     = partial(cbi_type, opcode=0b01, funct2=0b00, funct3=0b100)
C_SRAI     = partial(cbi_type, opcode=0b01, funct2=0b01, funct3=0b100)
C_ANDI     = partial(cbi_type, opcode=0b01, funct2=0b10, funct3=0b100)
C_SUB      = partial(ca_type,  opcode=0b01, funct2=0b00, funct6=0b100011)
C_XOR      = partial(ca_type,  opcode=0b01, funct2=0b01, funct6=0b100011)
C_OR       = partial(ca_type,  opcode=0b01, funct2=0b10, funct6=0b100011)
C_AND      = partial(ca_type,  opcode=0b01, funct2=0b11, funct6=0b100011)
C_J        = partial(cj_type,  opcode=0b01, funct3=0b101)
C_BEQZ     = partial(cb_type,  opcode=0b01, funct3=0b110)
C_BNEZ     = partial(cb_type,  opcode=0b01, funct3=0b111)
C_SLLI     = partial(ci_type,  opcode=0b10, funct3=0b000)
C_LWSP     = partial(cls_type, opcode=0b10, funct3=0b010)
C_JR       = partial(cr_type,  opcode=0b10, funct4=0b1000)
C_MV       = partial(cr_type,  opcode=0b10, funct4=0b1000)
C_JALR     = partial(cr_type,  opcode=0b10, funct4=0b1001)
C_ADD      = partial(cr_type,  opcode=0b10, funct4=0b1001)
C_SWSP     = partial(css_type, opcode=0b10, funct3=0b110)


R_TYPE_INSTRUCTIONS = {
    'slli':       SLLI,
    'srli':       SRLI,
    'srai':       SRAI,
    'add':        ADD,
    'sub':        SUB,
    'sll':        SLL,
    'slt':        SLT,
    'sltu':       SLTU,
    'xor':        XOR,
    'srl':        SRL,
    'sra':        SRA,
    'or':         OR,
    'and':        AND,
    'mul':        MUL,
    'mulh':       MULH,
    'mulhsu':     MULHSU,
    'mulhu':      MULHU,
    'div':        DIV,
    'divu':       DIVU,
    'rem':        REM,
    'remu':       REMU,
}

I_TYPE_INSTRUCTIONS = {
    'jalr':       JALR,
    'lb':         LB,
    'lh':         LH,
    'lw':         LW,
    'lbu':        LBU,
    'lhu':        LHU,
    'addi':       ADDI,
    'slti':       SLTI,
    'sltiu':      SLTIU,
    'xori':       XORI,
    'ori':        ORI,
    'andi':       ANDI,
}

S_TYPE_INSTRUCTIONS = {
    'sb':         SB,
    'sh':         SH,
    'sw':         SW,
}

B_TYPE_INSTRUCTIONS = {
    'beq':        BEQ,
    'bne':        BNE,
    'blt':        BLT,
    'bge':        BGE,
    'bltu':       BLTU,
    'bgeu':       BGEU,
}

U_TYPE_INSTRUCTIONS = {
    'lui':        LUI,
    'auipc':      AUIPC,
}

J_TYPE_INSTRUCTIONS = {
    'jal':        JAL,
}

A_TYPE_INSTRUCTIONS = {
    'lr.w':       LR_W,
    'sc.w':       SC_W,
    'amoswap.w':  AMOSWAP_W,
    'amoadd.w':   AMOADD_W,
    'amoxor.w':   AMOXOR_W,
    'amoand.w':   AMOAND_W,
    'amoor.w':    AMOOR_W,
    'amomin.w':   AMOMIN_W,
    'amomax.w':   AMOMAX_W,
    'amominu.w':  AMOMINU_W,
    'amomaxu.w':  AMOMAXU_W,
}

CR_TYPE_INSTRUCTIONS = {
    'c.jr':       C_JR,
    'c.mv':       C_MV,
    'c.jalr':     C_JALR,
    'c.add':      C_ADD,
}

CI_TYPE_INSTRUCTIONS = {
    'c.nop':      C_NOP,
    'c.addi':     C_ADDI,
    'c.li':       C_LI,
    'c.lui':      C_LUI,
    'c.slli':     C_SLLI,
}

CIS_TYPE_INSTRUCTIONS = {
    'c.addi16sp': C_ADDI16SP,
}

CLS_TYPE_INSTRUCTIONS = {
    'c.lwsp':     C_LWSP,    
}

CSS_TYPE_INSTRUCTIONS = {
    'c.swsp':     C_SWSP,
}

CIW_TYPE_INSTRUCTIONS = {
    'c.addi4spn': C_ADDI4SPN,
}

CL_TYPE_INSTRUCTIONS = {
    'c.lw':       C_LW,
}

CS_TYPE_INSTRUCTIONS = {
    'c.sw':       C_SW,
}

CA_TYPE_INSTRUCTIONS = {
    'c.sub':      C_SUB,
    'c.xor':      C_XOR,
    'c.or':       C_OR,
    'c.and':      C_AND,
}

CB_TYPE_INSTRUCTIONS = {
    'c.beqz':     C_BEQZ,
    'b.bnez':     C_BNEZ,
}

CBI_TYPE_INSTRUCTIONS = {
    'c.srli':     C_SRLI,
    'c.srai':     C_SRAI,
    'c.andi':     C_ANDI,
}

CJ_TYPE_INSTRUCTIONS = {
    'c.jal':      C_JAL,
    'c.j':        C_J,
}

INSTRUCTIONS = {}
INSTRUCTIONS.update(R_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(I_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(S_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(B_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(U_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(J_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(A_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(CR_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(CI_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(CIS_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(CLS_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(CSS_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(CIW_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(CL_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(CS_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(CA_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(CB_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(CBI_TYPE_INSTRUCTIONS)
INSTRUCTIONS.update(CJ_TYPE_INSTRUCTIONS)


def sign_extend(value, bits):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)


def relocate_hi(imm):
    if imm & 0x800:
        imm += 2**12
    return sign_extend((imm >> 12) & 0x000fffff, 20)


def relocate_lo(imm):
    return sign_extend(imm & 0x00000fff, 12)


class Line:

    def __init__(self, file, number, contents):
        self.file = file
        self.number = number
        self.contents = contents

    def __repr__(self):
        return '{}({!r}, {!r}, {!r})'.format(type(self).__name__, self.file, self.number, self.contents)

    def __str__(self):
        return '{}:{}: {}'.format(self.file, self.number, self.contents)


class LineTokens:

    def __init__(self, line, tokens):
        self.line = line
        self.tokens = tokens


class Expr(abc.ABC):

    @abc.abstractmethod
    def eval(self, position, env):
        """Evaluate an expression to an integer"""


# arithmetic / lookup / combo of both
# defers evaulation to Python's builtin eval
class Arithmetic(Expr):

    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return '{}({!r})'.format(type(self).__name__, self.expr)

    def eval(self, position, env):
        return eval(self.expr, env)


class Position(Expr):

    def __init__(self, reference, expr):
        self.reference = reference
        self.expr = expr

    def __repr__(self):
        return '{}({!r}, {!r})'.format(type(self).__name__, self.reference, self.expr)

    def eval(self, position, env):
        dest = env[self.reference]
        base = self.expr.eval(position, env)
        return base + dest


class Offset(Expr):

    def __init__(self, reference):
        self.reference = reference

    def __repr__(self):
        return '{}({!r})'.format(type(self).__name__, self.reference)

    def eval(self, position, env):
        dest = env[self.reference]
        return dest - position


class Hi(Expr):

    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return '{}({!r})'.format(type(self).__name__, self.expr)

    def eval(self, position, env):
        # TODO: move this check to the parser
        if isinstance(self.expr, Hi) or isinstance(self.expr, Lo):
            raise TypeError('%hi and %lo expressions cannot nest')

        value = self.expr.eval(position, env)
        return relocate_hi(value)


class Lo(Expr):

    def __init__(self, expr) -> None:
        self.expr = expr

    def __repr__(self):
        return '{}({!r})'.format(type(self).__name__, self.expr)

    def eval(self, position, env):
        # TODO: move this check to the parser
        if isinstance(self.expr, Hi) or isinstance(self.expr, Lo):
            raise TypeError('%hi and %lo expressions cannot nest')

        value = self.expr.eval(position, env)
        return relocate_lo(value)


# base class for assembly "things"
class Item(abc.ABC):

    @abc.abstractmethod
    def size(self, position):
        """Check the size of this item at the given position in a program"""


class Align(Item):

    def __init__(self, alignment):
        self.alignment = alignment

    def __repr__(self):
        return '{}({!r})'.format(type(self).__name__, self.alignment)

    def size(self, position):
        padding = self.alignment - (position % self.alignment)
        if padding == self.alignment:
            return 0
        else:
            return padding


class Label(Item):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '{}({!r})'.format(type(self).__name__, self.name)

    def size(self, position):
        return 0


class Constant(Item):

    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

    def __repr__(self):
        return '{}({!r}, {!r})'.format(type(self).__name__, self.name, self.expr)

    def size(self, position):
        return 0


class Bytes(Item):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return '{}({!r})'.format(type(self).__name__, self.values)

    def size(self, position):
        # this works because each byte occupies 1 byte
        return len(self.values)


class String(Item):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return '{}({!r})'.format(type(self).__name__, self.values)

    def size(self, position):
        return len(' '.join(self.values))


class Pack(Item):

    def __init__(self, fmt, expr):
        self.fmt = fmt
        self.expr = expr

    def __repr__(self):
        return '{}({!r}, {!r})'.format(type(self).__name__, self.fmt, self.expr)

    def size(self, position):
        return struct.calcsize(self.fmt)


class Blob(Item):

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        # repr is still valid, just wanted a more consistent hex format
        s = ''.join(['\\x{:02x}'.format(b) for b in self.data])
        return "{}(b'{}')".format(type(self).__name__, s)

    def size(self, position):
        return len(self.data)


class Instruction(Item):

    def size(self, position):
        return 4


class CompressedInstruction(Instruction):

    def size(self, position):
        return 2


class RTypeInstruction(Instruction):

    def __init__(self, name, rd, rs1, rs2):
        self.name = name
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2

    def __repr__(self):
        return '{}({!r}, rd={!r}, rs1={!r}, rs2={!r})'.format(type(self).__name__, self.name, self.rd, self.rs1, self.rs2)


class ITypeInstruction(Instruction):

    def __init__(self, name, rd, rs1, expr):
        self.name = name
        self.rd = rd
        self.rs1 = rs1
        self.expr = expr

    def __repr__(self):
        return '{}({!r}, rd={!r}, rs1={!r}, imm={!r})'.format(type(self).__name__, self.name, self.rd, self.rs1, self.expr)


class STypeInstruction(Instruction):

    def __init__(self, name, rs1, rs2, expr):
        self.name = name
        self.rs1 = rs1
        self.rs2 = rs2
        self.expr = expr

    def __repr__(self):
        return '{}({!r}, rs1={!r}, rs2={!r}, imm={!r})'.format(type(self).__name__, self.name, self.rs1, self.rs2, self.expr)


class BTypeInstruction(Instruction):

    def __init__(self, name, rs1, rs2, expr):
        self.name = name
        self.rs1 = rs1
        self.rs2 = rs2
        self.expr = expr

    def __repr__(self):
        return '{}({!r}, rs1={!r}, rs2={!r}, imm={!r})'.format(type(self).__name__, self.name, self.rs1, self.rs2, self.expr)


class UTypeInstruction(Instruction):

    def __init__(self, name, rd, expr):
        self.name = name
        self.rd = rd
        self.expr = expr

    def __repr__(self):
        return '{}({!r}, rd={!r}, imm={!r})'.format(type(self).__name__, self.name, self.rd, self.expr)


class JTypeInstruction(Instruction):

    def __init__(self, name, rd, expr):
        self.name = name
        self.rd = rd
        self.expr = expr

    def __repr__(self):
        return '{}({!r}, rd={!r}, imm={!r})'.format(type(self).__name__, self.name, self.rd, self.expr)


class ATypeInstruction(Instruction):

    def __init__(self, name, rd, rs1, rs2, aq=0, rl=0):
        self.name = name
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
        self.aq = aq
        self.rl = rl

    def __repr__(self):
        s = '{}({!r}, rd={!r}, rs1={!r}, rs2={!r}, aq={!r}, rl={!r})'
        s = s.format(type(self).__name__, self.name, self.rd, self.rs1, self.rs2, self.aq, self.rl)
        return s


# TODO: classes for compressed instruction types


def read_assembly(path_or_source):
    if os.path.exists(path_or_source):
        path = path_or_source
        with open(path) as f:
            source = f.read()
    else:
        path = '<source>'
        source = path_or_source

    lines = []
    for i, line in enumerate(source.splitlines(), start=1):
        # skip empty lines
        if len(line.strip()) == 0:
            continue
        lines.append(Line(path, i, line))

    return lines


def lex_assembly(lines):
    line_tokens = []

    for line in lines:
        # strip comments
        contents = re.sub(r'#.*$', r'', line.contents, flags=re.MULTILINE)
        # strip whitespace
        contents = contents.strip()
        # skip empty lines
        if len(contents) == 0:
            continue
        # split line into tokens
        tokens = re.split(r'[\s,()\'"]+', contents)
        # remove empty tokens
        while '' in tokens:
            tokens.remove('')
        # carry the line and its tokens forward
        line_tokens.append(LineTokens(line, tokens))

    return line_tokens


# helper for parsing exprs since they occur in multiple places
# TODO: catch invalid expr nesting here
def parse_expression(expr):
    head = expr[0].lower()
    if head == '%position':
        _, reference, *expr = expr
        return Position(reference, Arithmetic(' '.join(expr)))
    elif head == '%offset':
        _, reference = expr
        return Offset(reference)
    elif head == '%hi':
        _, *expr = expr
        return Hi(parse_expression(expr))
    elif head == '%lo':
        _, *expr = expr
        return Lo(parse_expression(expr))
    else:
        return Arithmetic(' '.join(expr))


def parse_assembly(line_tokens):
    items = []
    for lt in line_tokens:
        line = lt.line
        tokens = lt.tokens

        head = tokens[0].lower()

        # labels
        if len(tokens) == 1 and tokens[0].endswith(':'):
            name = tokens[0].rstrip(':')
            label = Label(name)
            items.append(label)
        # constants
        elif len(tokens) >= 3 and tokens[1] == '=':
            name, _, *expr = tokens
            constant = Constant(name, parse_expression(expr))
            items.append(constant)
        # aligns
        elif head == 'align':
            _, alignment = tokens
            align = Align(int(alignment))
            items.append(align)
        # packs
        elif head == 'pack':
            _, fmt, *expr = tokens
            pack = Pack(fmt, parse_expression(expr))
            items.append(pack)
        # bytes
        elif head == 'bytes':
            # TODO: ensure bytes are valid here?
            _, *values = tokens
            bytes = Bytes(values)
            items.append(bytes)
        # strings
        elif head == 'string':
            _, *values = tokens
            string = String(values)
            items.append(string)
        # r-type instructions
        elif head in R_TYPE_INSTRUCTIONS:
            name, rd, rs1, rs2 = tokens
            name = name.lower()
            inst = RTypeInstruction(name, rd, rs1, rs2)
            items.append(inst)
        # i-type instructions
        elif head in I_TYPE_INSTRUCTIONS:
            name, rd, rs1, *expr = tokens
            name = name.lower()
            inst = ITypeInstruction(name, rd, rs1, parse_expression(expr))
            items.append(inst)
        # s-type instructions
        elif head in S_TYPE_INSTRUCTIONS:
            name, rs1, rs2, *expr = tokens
            name = name.lower()
            inst = STypeInstruction(name, rs1, rs2, parse_expression(expr))
            items.append(inst)
        # b-type instructions
        elif head in B_TYPE_INSTRUCTIONS:
            name, rs1, rs2, *expr = tokens
            name = name.lower()
            # ensure behavior is "offset" for branch instructions
            if expr[0] != '%offset':
                expr.insert(0, '%offset')
            inst = BTypeInstruction(name, rs1, rs2, parse_expression(expr))
            items.append(inst)
        # u-type instructions
        elif head in U_TYPE_INSTRUCTIONS:
            name, rd, *expr = tokens
            name = name.lower()
            inst = UTypeInstruction(name, rd, parse_expression(expr))
            items.append(inst)
        # j-type instructions
        elif head in J_TYPE_INSTRUCTIONS:
            name, rd, *expr = tokens
            name = name.lower()
            # ensure behavior is "offset" for branch instructions
            if expr[0] != '%offset':
                expr.insert(0, '%offset')
            inst = JTypeInstruction(name, rd, parse_expression(expr))
            items.append(inst)
        # a-type instructions
        elif head in A_TYPE_INSTRUCTIONS:
            name, rd, rs1, rs2, *ordering = tokens
            # check for specific ordering bits
            if len(ordering) == 0:
                aq, rl = 0, 0
            elif len(ordering) == 2:
                aq, rl = ordering
            else:
                raise ValueError('invalid ordering bits for atomic instruction:\n{}'.format(line))
            inst = ATypeInstruction(name, rd, rs1, rs2, aq, rl)
            items.append(inst)
        # TODO: compressed instructions
        else:
            raise ValueError('invalid syntax:\n{}'.format(line))

    return items


def resolve_aligns(items):
    position = 0
    new_items = []
    for item in items:
        if isinstance(item, Align):
            padding = item.size(position)
            position += padding
            blob = Blob(b'\x00' * padding)
            new_items.append(blob)
        else:
            position += item.size(position)
            new_items.append(item)

    return new_items


def resolve_labels(items, env):
    new_env = copy.deepcopy(env)

    position = 0
    new_items = []
    for item in items:
        if isinstance(item, Label):
            new_env[item.name] = position
        else:
            position += item.size(position)
            new_items.append(item)

    return new_items, new_env


def resolve_constants(items, env):
    new_env = copy.deepcopy(env)

    position = 0
    new_items = []
    for item in items:
        if isinstance(item, Constant):
            if item.name in REGISTERS:
                raise ValueError('constant name shadows register name "{}"'.format(item.name))
            new_env[item.name] = item.expr.eval(position, new_env)
        else:
            position += item.size(position)
            new_items.append(item)

    return new_items, new_env


def resolve_registers(items, env):
    new_items = []
    for item in items:
        if isinstance(item, RTypeInstruction):
            rd = env.get(item.rd) or item.rd
            rs1 = env.get(item.rs1) or item.rs1
            rs2 = env.get(item.rs2) or item.rs2
            inst = RTypeInstruction(item.name, rd, rs1, rs2)
            new_items.append(inst)
        elif isinstance(item, ITypeInstruction):
            rd = env.get(item.rd) or item.rd
            rs1 = env.get(item.rs1) or item.rs1
            inst = ITypeInstruction(item.name, rd, rs1, item.expr)
            new_items.append(inst)
        elif isinstance(item, STypeInstruction):
            rs1 = env.get(item.rs1) or item.rs1
            rs2 = env.get(item.rs2) or item.rs2
            inst = STypeInstruction(item.name, rs1, rs2, item.expr)
            new_items.append(inst)
        elif isinstance(item, BTypeInstruction):
            rs1 = env.get(item.rs1) or item.rs1
            rs2 = env.get(item.rs2) or item.rs2
            inst = BTypeInstruction(item.name, rs1, rs2, item.expr)
            new_items.append(inst)
        elif isinstance(item, UTypeInstruction):
            rd = env.get(item.rd) or item.rd
            inst = UTypeInstruction(item.name, rd, item.expr)
            new_items.append(inst)
        elif isinstance(item, JTypeInstruction):
            rd = env.get(item.rd) or item.rd
            inst = JTypeInstruction(item.name, rd, item.expr)
            new_items.append(inst)
        elif isinstance(item, ATypeInstruction):
            rd = env.get(item.rd) or item.rd
            rs1 = env.get(item.rs1) or item.rs1
            rs2 = env.get(item.rs2) or item.rs2
            inst = ATypeInstruction(item.name, rd, rs1, rs2, item.aq, item.rl)
            new_items.append(inst)
        else:
            new_items.append(item)

    return new_items


def resolve_immediates(items, env):
    position = 0
    new_items = []
    for item in items:
        if isinstance(item, ITypeInstruction):
            imm = item.expr.eval(position, env)
            position += item.size(position)
            inst = ITypeInstruction(item.name, item.rd, item.rs1, imm)
            new_items.append(inst)
        elif isinstance(item, STypeInstruction):
            imm = item.expr.eval(position, env)
            position += item.size(position)
            inst = STypeInstruction(item.name, item.rs1, item.rs2, imm)
            new_items.append(inst)
        elif isinstance(item, BTypeInstruction):
            imm = item.expr.eval(position, env)
            position += item.size(position)
            inst = BTypeInstruction(item.name, item.rs1, item.rs2, imm)
            new_items.append(inst)
        elif isinstance(item, UTypeInstruction):
            imm = item.expr.eval(position, env)
            position += item.size(position)
            inst = UTypeInstruction(item.name, item.rd, imm)
            new_items.append(inst)
        elif isinstance(item, JTypeInstruction):
            imm = item.expr.eval(position, env)
            position += item.size(position)
            inst = JTypeInstruction(item.name, item.rd, imm)
            new_items.append(inst)
        elif isinstance(item, Pack):
            imm = item.expr.eval(position, env)
            position += item.size(position)
            pack = Pack(item.fmt, imm)
            new_items.append(pack)
        else:
            position += item.size(position)
            new_items.append(item)

    return new_items


def resolve_compressible(items):
    # check if any instructions meet the criteria for a compressed equivalent
    return items


def resolve_instructions(items):
    new_items = []
    for item in items:
        if isinstance(item, RTypeInstruction):
            encode_func = INSTRUCTIONS[item.name]
            code = encode_func(item.rd, item.rs1, item.rs2)
            code = struct.pack('<I', code)
            blob = Blob(code)
            new_items.append(blob)
        elif isinstance(item, ITypeInstruction):
            encode_func = INSTRUCTIONS[item.name]
            code = encode_func(item.rd, item.rs1, item.expr)
            code = struct.pack('<I', code)
            blob = Blob(code)
            new_items.append(blob)
        elif isinstance(item, STypeInstruction):
            encode_func = INSTRUCTIONS[item.name]
            code = encode_func(item.rs1, item.rs2, item.expr)
            code = struct.pack('<I', code)
            blob = Blob(code)
            new_items.append(blob)
        elif isinstance(item, BTypeInstruction):
            encode_func = INSTRUCTIONS[item.name]
            code = encode_func(item.rs1, item.rs2, item.expr)
            code = struct.pack('<I', code)
            blob = Blob(code)
            new_items.append(blob)
        elif isinstance(item, UTypeInstruction):
            encode_func = INSTRUCTIONS[item.name]
            code = encode_func(item.rd, item.expr)
            code = struct.pack('<I', code)
            blob = Blob(code)
            new_items.append(blob)
        elif isinstance(item, JTypeInstruction):
            encode_func = INSTRUCTIONS[item.name]
            code = encode_func(item.rd, item.expr)
            code = struct.pack('<I', code)
            blob = Blob(code)
            new_items.append(blob)
        elif isinstance(item, ATypeInstruction):
            encode_func = INSTRUCTIONS[item.name]
            code = encode_func(item.rd, item.rs1, item.rs2, aq=item.aq, rl=item.rl)
            code = struct.pack('<I', code)
            blob = Blob(code)
            new_items.append(blob)
        else:
            new_items.append(item)

    return new_items


def resolve_packs(items):
    new_items = []
    for item in items:
        if isinstance(item, Pack):
            data = struct.pack(item.fmt, item.expr)
            blob = Blob(data)
            new_items.append(blob)
        else:
            new_items.append(item)

    return new_items


def resolve_bytes(items):
    new_items = []
    for item in items:
        if isinstance(item, Bytes):
            data = [int(byte, base=0) for byte in item.values]
            for byte in data:
                if byte < 0 or byte > 255:
                    raise ValueError('bytes literal not in range [0, 255] at {}'.format(line))
            blob = Blob(bytes(data))
            new_items.append(blob)
        else:
            new_items.append(item)

    return new_items


def resolve_strings(items):
    new_items = []
    for item in items:
        if isinstance(item, String):
            text = ' '.join(item.values)
            blob = Blob(text.encode())
            new_items.append(blob)
        else:
            new_items.append(item)

    return new_items


def resolve_blobs(items):
    output = bytearray()
    for item in items:
        if not isinstance(item, Blob):
            raise ValueError('expected only blobs at this point')
        output.extend(item.data)
    return output


# Passes:
#  0. Read -> Lex -> Parse source
#  1. Resolve aligns  (convert aligns to blobs based on position)
#  2. Resolve labels  (store label locations into env)
#  3. Resolve constants  (eval expr and update env)
#  4. Resolve registers  (could be constants for readability)
#  5. Resolve immediates  (Arithmetic, Position, Offset, Hi, Lo)
#  6. Resolve compressible  (identify and compress eligible instructions)
#  7. Resolve instructions  (convert xTypeInstruction to Blob)
#  8. Resolve bytes  (convert Bytes to Blob)
#  9. Resolve strings  (convert String to Blob)
# 10. Resolve packs  (convert Pack to Blob)
# 11. Resolve blobs  (merge all Blobs into a single binary)

def assemble(path_or_source, compress=False, verbose=False):
    """
    Assemble a RISC-V assembly program into a raw binary.

    :param path_or_source: Path to an assembly file or raw assembly source
    :returns: Assembled binary as bytes
    """

    # exclude Python builtins from eval env
    # https://docs.python.org/3/library/functions.html#eval
    env = {
        '__builtins__': None,
    }
    env.update(REGISTERS)

    # read, lex, and parse the source
    lines = read_assembly(path_or_source)
    line_tokens = lex_assembly(lines)
    items = parse_assembly(line_tokens)

    # run items through each pass
    items = resolve_aligns(items)
    items, env = resolve_labels(items, env)
    items, env = resolve_constants(items, env)
    items = resolve_registers(items, env)
    items = resolve_immediates(items, env)
    if compress:
        items = resolve_compressible(items)
    items = resolve_instructions(items)
    items = resolve_bytes(items)
    items = resolve_strings(items)
    items = resolve_packs(items)
    program = resolve_blobs(items)

    if verbose:
        # print resolved environment
        succint_env = {k: v for k, v in env.items() if k not in REGISTERS}
        succint_env.pop('__builtins__')
        for k, v in succint_env.items():
            print('{} = {} (0x{:08x})'.format(k, v, v))

    return program


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Assemble RISC-V source code',
        prog='python -m bronzebeard.asm',
    )
    parser.add_argument('input_asm', type=str, help='input source file')
    parser.add_argument('output_bin', type=str, help='output binary file')
    parser.add_argument('--compress', action='store_true', help='identify and compress instructions')
    parser.add_argument('--verbose', action='store_true', help='verbose assembler output')
    args = parser.parse_args()

    binary = assemble(args.input_asm, args.compress, args.verbose)
    with open(args.output_bin, 'wb') as out_bin:
        out_bin.write(binary)
