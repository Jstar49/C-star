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
    UCHAR = "unsigned_char"
    CHAR = "char"
    USHORT = "unsigned_short"
    SHORT = "short"
    UINT = "unsigned_int"
    INT = "int"
    ULONG = "unsigned_long"
    LONG = "long"
    ULONGLONG = "unsigned_long_long"
    LONGLONG = "long_long"
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
    # AND = "&"
    # OR = "|"
    # XOR = "^"
    # # ROC = "~"
    # SRL = ">>"
    # SLL = "<<"

# Assignment operation
@unique
class AssignementTypes(Enum):
    ASSIGNE = "="
    # ADDASSIGN = "+="
    # SUBASSIGN = "-="
    # MULASSIGNE = "*="
    # DIVASSIGNE = "/="
    # REMASSIGNE = "%="
    # ANDASSIGNE = "&="
    # ORASSIGNE = "|="
    # XORASSIGNE = "^="
    # # ROCASSIGNE = "~="
    # SRLASSIGNE = ">>="
    # SLLASSIGNE = "<<="

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
    
VarType2CType = {
  VarTypes.UCHAR:"c_ubyte",
  VarTypes.CHAR:"c_byte",
  VarTypes.USHORT:"c_ushort",
  VarTypes.SHORT:"c_short",
  VarTypes.UINT:"c_uint",
  VarTypes.INT:"c_int",
  VarTypes.ULONG:"c_ulong",
  VarTypes.LONG:"c_long",
  VarTypes.ULONGLONG:"c_ulonglong",
  VarTypes.LONGLONG:"c_longlong"
}

MathematicalTypes2FuncOp = {
  MathematicalTypes.ADD:"add",
  MathematicalTypes.SUB:"sub",
  MathematicalTypes.MUL:"mul",
  MathematicalTypes.DIV:"div",
  MathematicalTypes.REM:"rem"
}

VarTypeCalPriority = {
    VarTypes.CHAR: 0,
    VarTypes.UCHAR: 0,
    VarTypes.SHORT: 0,
    VarTypes.USHORT: 0,
    VarTypes.INT: 1,
    VarTypes.UINT: 2,
    VarTypes.LONG: 3,
    VarTypes.ULONG: 4,
    VarTypes.LONGLONG: 5,
    VarTypes.ULONGLONG: 6,
}

VarPriority2Type = {
    1: VarTypes.INT,
    2: VarTypes.UINT,
    3: VarTypes.LONG,
    4: VarTypes.ULONG,
    5: VarTypes.LONGLONG,
    6: VarTypes.ULONGLONG,
}

def get_return_type(type1:VarTypes, type2:VarTypes):
  # 等级低于int的操作数，运算时全会被当作int
  # 等级高于int的操作数，大体上要同时符合这个要求
    # 优先无符号，同时优先更长。都要满足
  
  priority1 = VarTypeCalPriority[type1]
  priority2 = VarTypeCalPriority[type2]
  priority1 = max(1, priority1)
  priority2 = max(1, priority2)
  max_priority = max(priority1,priority2)
  uflag = False
  if priority1%2==0 or priority2%2==0:
    uflag = True
  if max_priority%2!=0 and uflag:
    max_priority+=1
  return VarPriority2Type[max_priority]