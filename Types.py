'''
Author: joessem jxxclj@gmail.com
Date: 2022-11-26 23:33:51
LastEditors: joessem jxxclj@gmail.com
LastEditTime: 2022-12-11 21:01:58
FilePath: \C-star\Types.py
Description: 

Copyright (c) 2022 by joessem jxxclj@gmail.com, All Rights Reserved. 
'''

from pkg import TypeRanges, VarTypes
import random

# Base Type class
class Var_t:
    def __init__(self) -> None:
        self.val = None
        self.min = None
        self.max = None
        self.var_name = ""
        self.type_name = ""
        # variable valid range
        self.valid_range = None

    # random values in ranges
    def Random_values(self):
        # print(self.min, self.max)
        self.val = random.randint(self.min, self.max)

# bool class
class Bool_t(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.BOOL_MIN
        self.max = TypeRanges.BOOL_MAX
        self.type_name = VarTypes.BOOL
        # self.Random_values()

# char class
class Char_t(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.CHAR_MIN
        self.max = TypeRanges.CHAR_MAX
        self.type_name = VarTypes.CHAR
        # self.Random_values()


# unsigned char class
class UChar_t(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.UCHAR_MIN
        self.max = TypeRanges.UCHAR_MAX
        self.type_name = VarTypes.UCHAR
        # self.Random_values()

# short class
class Short_t(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.SHORT_MIN
        self.max = TypeRanges.SHORT_MAX
        self.type_name = VarTypes.SHORT
        # self.Random_values()

# unsigned short class
class UShort_t(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.USHORT_MIN
        self.max = TypeRanges.USHORT_MAX
        self.type_name = VarTypes.USHORT
        # self.Random_values()

# int class
class Int_t(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.INT_MIN
        self.max = TypeRanges.INT_MAX
        self.type_name = VarTypes.INT
        # self.Random_values()

# unsigned int class
class UInt_t(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.UINT_MIN
        self.max = TypeRanges.UINT_MAX
        self.type_name = VarTypes.UINT
        # self.Random_values()

# long class
class Long_t(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.LONG_MIN
        self.max = TypeRanges.LONG_MAX
        self.type_name = VarTypes.LONG
        # self.Random_values()

# unsigned long class
class ULong_t(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.ULONG_MIN
        self.max = TypeRanges.ULONG_MAX
        self.type_name = VarTypes.ULONG
        # self.Random_values()

# long long class
class LLong_t(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.LONGLONG_MIN
        self.max = TypeRanges.LONGLONG_MAX
        self.type_name = VarTypes.LONGLONG
        # self.Random_values()

# unsigned long long class
class ULLong_t(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.ULONGLONG_MIN
        self.max = TypeRanges.ULONGLONG_MAX
        self.type_name = VarTypes.ULONGLONG
        # self.Random_values()

# return a random data type
def Get_Random_Type_Var():
    type_list =  [Char_t, UChar_t, Short_t, UShort_t, Int_t, 
                UInt_t, Long_t, ULong_t, LLong_t, ULLong_t]
    tmp_val = random.choice(type_list)()
    tmp_val.Random_values()
    # print(type(tmp_val), tmp_val.val)
    return tmp_val

def Get_Var_By_Type(tp):
    typedict = {"bool": Bool_t, "unsigned char": UChar_t, "char": Char_t, 
                "unsigned short": UShort_t, "short": Short_t, "unsigned int": UInt_t, 
                "int": Int_t, "unsigned long": ULong_t, "long": Long_t, 
                "unsigned long long": ULLong_t, "long long": LLong_t}
    tmp_val = typedict[tp]()
    tmp_val.Random_values()
    return tmp_val

# Get_Random_Type_Var()