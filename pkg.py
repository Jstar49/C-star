'''
Author: joessem jxxclj@gmail.com
Date: 2022-11-20 21:18:40
LastEditors: joessem jxxclj@gmail.com
LastEditTime: 2022-12-06 23:24:08
FilePath: \C-star\pkg.py
Description: 
    一些类型定义 & 枚举
Copyright (c) 2022 by joessem jxxclj@gmail.com, All Rights Reserved. 
'''
from config import args
from enum import Enum, IntEnum, unique, auto

# Indentation
INDENT = "  "

# block id
BLOCK_ID = 0

def Get_BLOCKID():
    global BLOCK_ID
    BLOCK_ID += 1
    return BLOCK_ID

# data types
class VarTypes:
    VOID = "void"
    BOOL = "bool"
    UCHAR = "unsigned char"
    CHAR = "char"
    USHORT = "unsigned short"
    SHORT = "short"
    UINT = "unsigned int"
    INT = "int"
    ULONG = "unsigned long"
    LONG = "long"
    ULONGLONG = "unsigned long long"
    LONGLONG = "long long"
    FLOAT = "float"
    DOUBLE = "double"

# Arithmetic operation
@unique
class MathematicalTypes(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    REM = "%"
    # ADDS = "++"
    # SUBS = "--"
    # bits 
    AND = "&"
    OR = "|"
    XOR = "^"
    # ROC = "~"
    SRL = ">>"
    SLL = "<<"

# Assignment operation
@unique
class AssignementTypes(Enum):
    ASSIGNE = "="
    ADDASSIGN = "+="
    SUBASSIGN = "-="
    MULASSIGNE = "*="
    DIVASSIGNE = "/="
    REMASSIGNE = "%="
    ANDASSIGNE = "&="
    ORASSIGNE = "|="
    XORASSIGNE = "^="
    # ROCASSIGNE = "~="
    SRLASSIGNE = ">>="
    SLLASSIGNE = "<<="

class StatementsTypes(Enum):
    Assignement = auto()

# Data Range between different types
class TypeRanges:
    BOOL_MIN = 0
    BOOL_MAX = 1
    CHAR_MIN = -128
    CHAR_MAX = 127
    UCHAR_MIN = 0
    UCHAR_MAX = 255
    USHORT_MIN = 0
    USHORT_MAX = 65535
    SHORT_MIN = -32768
    SHORT_MAX = 32767
    UINT_MIN = 0
    UINT_MAX = 4294967295  # 1 << 32
    INT_MIN = -2147483648
    INT_MAX = 2147483647
    ULONG_MIN = 0
    ULONG_MAX = (1<<32) - 1 if args.target == 32 else (1<<64) - 1
    LONG_MIN = -(1<<31) if args.target == 32 else (-(1<<63))
    LONG_MAX = (1 << 31) - 1 if args.target == 32 else (1 << 63) - 1
    LONGLONG_MIN = - (1 << 63)
    LONGLONG_MAX = (1 << 63) - 1