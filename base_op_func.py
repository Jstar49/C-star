import random

from pkg import *

class Base_Op:
    def __init__(self) -> None:
        self.op_type = None
        self.func_name = ""
        self.func_type = None
        self.args = []

        self.func_codes = []

class Base_Op_Class:
    def __init__(self) -> None:
        self.base_ops = {
            MathematicalTypes.ADD: "add", 
            MathematicalTypes.SUB: "sub", 
            MathematicalTypes.MUL: "mul", 
            MathematicalTypes.DIV: "div", 
            MathematicalTypes.REM: "rem"
        }
        self.base_vartype = list(VarTypes)

        self.base_op_func_can_used = []
        self.base_op_func_used = []
    
    def Build_Base_Op_functions(self):
        for i in range(len(self.base_vartype)):
            for item in self.base_ops:
                func_type = self.base_vartype[i].value
                func_name = f"_func_{self.base_ops[item]}_{self.base_vartype[i].value}_"
                print(func_name)
                if self.base_ops[item] == "add":
                    pass
                elif self.base_ops[item] == "div":
                    pass

s = Base_Op_Class()
s.Build_Base_Op_functions()