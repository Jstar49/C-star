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
        # print(self.base_vartype)
        self.base_op_func_can_used = {}
        self.base_op_func_used = []
    
    def Mark_func_used(self, func_name):
        if func_name not in self.base_op_func_used:
            self.base_op_func_used.append(func_name)
    
    def Build_Base_Op_functions(self):
        for i in range(len(self.base_vartype)):
            for item in self.base_ops:
                base_op = Base_Op()
                # print(i, self.base_vartype)
                base_op.op_type = self.base_vartype[i].value
                base_op.func_name = f"_func_{self.base_ops[item]}_{self.base_vartype[i].value}_"
                base_op.args = f"({self.base_vartype[i].value} ax, {self.base_vartype[i].value} bx)"
                # print(func_name)
                tmp = base_op.op_type + " " + base_op.func_name + " " + base_op.args + ""
                base_op.func_codes.append(tmp)
                base_op.func_codes.append("{")
                tmp = INDENT
                if self.base_ops[item] == "add":
                    tmp += "return ax + bx;"
                elif self.base_ops[item] == "mul":
                    tmp += "return ax * bx;"
                elif self.base_ops[item] == "sub":
                    tmp += "return ax - bx;"
                elif self.base_ops[item] == "div":
                    tmp += f'''if (bx == 0) return ax;\n{INDENT}return ax / bx;'''
                elif self.base_ops[item] == "rem":
                    tmp += f'''if (bx == 0) return ax;\n{INDENT}return ax % bx;'''
                base_op.func_codes.append(tmp)
                base_op.func_codes.append("}")
                self.base_op_func_can_used[base_op.func_name] = base_op

                # for k in base_op.func_codes:
                #     print(k)
    
    def Build_operator_codes(self):
        tmp_rets = []
        for op in self.base_op_func_used:
            tmp_rets += self.base_op_func_can_used[op].func_codes
        return tmp_rets

base_op_c = Base_Op_Class()
base_op_c.Build_Base_Op_functions()