from pkg import TypeRanges, VarTypes
import random

# Constant class
class Constant_t:
    def __init__(self) -> None:
        self.is_float = 0
        self.value = 0
        self.const_range = [TypeRanges.INT32_MIN, TypeRanges.INT32_MAX]
    
    def random_const(self):
        if self.is_float:
            pass
        else:
            self.value = random.randint(self.const_range[0], self.const_range[1])

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
        
'''
# bool class
class Bool_t(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.BOOL_MIN
        self.max = TypeRanges.BOOL_MAX
        self.type_name = VarTypes.BOOL
        # self.Random_values()'''

# char class
class INT8_T(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.INT8_MIN
        self.max = TypeRanges.INT8_MAX
        self.type_name = VarTypes.INT8
        # self.Random_values()


# unsigned char class
class UINT8_T(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.UINT8_MIN
        self.max = TypeRanges.UINT8_MAX
        self.type_name = VarTypes.UINT8
        # self.Random_values()

# short class
class INT16_T(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.INT16_MIN
        self.max = TypeRanges.INT16_MAX
        self.type_name = VarTypes.INT16
        # self.Random_values()

# unsigned short class
class UINT16_T(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.UINT16_MIN
        self.max = TypeRanges.UINT16_MAX
        self.type_name = VarTypes.UINT16
        # self.Random_values()

# int class
class INT32_T(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.INT32_MIN
        self.max = TypeRanges.INT32_MAX
        self.type_name = VarTypes.INT32
        # self.Random_values()

# unsigned int class
class UINT32_T(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.UINT32_MIN
        self.max = TypeRanges.UINT32_MAX
        self.type_name = VarTypes.UINT32
        # self.Random_values()

# long class
class INT64_T(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.INT64_MIN
        self.max = TypeRanges.INT64_MAX
        self.type_name = VarTypes.INT64
        # self.Random_values()

# unsigned long class
class UINT64_T(Var_t):
    def __init__(self) -> None:
        super().__init__()
        self.min = TypeRanges.UINT64_MIN
        self.max = TypeRanges.UINT64_MAX
        self.type_name = VarTypes.UINT64 
        # self.Random_values()


# return a random data type
def Get_Random_Type_Var():
    type_list =  [INT8_T, UINT8_T, INT16_T, UINT16_T, INT32_T, 
                UINT32_T, INT64_T, UINT64_T]
    tmp_val = random.choice(type_list)()
    tmp_val.Random_values()
    # print(type(tmp_val), tmp_val.val)
    return tmp_val

def Get_Var_By_Type(tp):
    typedict = {"int8_t": INT8_T, "uint8_t": UINT8_T,
                "int16_t": INT16_T, "uint16_t": UINT16_T, 
                "int32_t": INT32_T, "uint32_t": UINT32_T,
                "int64_t": INT64_T, "uint64_t": UINT64_T,}
    tmp_val = typedict[tp]()
    tmp_val.Random_values()
    return tmp_val

# Get_Random_Type_Var()