'''
Author: joessem jxxclj@gmail.com
Date: 2022-11-27 23:10:15
LastEditors: joessem jxxclj@gmail.com
LastEditTime: 2022-11-29 23:47:33
FilePath: \C-star\code_statements.py
Description: 
    Generate C statements

Copyright (c) 2022 by joessem jxxclj@gmail.com, All Rights Reserved. 
'''
import random
from pkg import MathematicalTypes, AssignementTypes, StatementsTypes

# 
class RandomArithmetics:
    def __init__(self, left_var = None, right_var = None) -> None:
        # type of arithmetic, such as +,-,*,/
        self.arithmetic_type = None
        # need left var, and right var
        tmp = random.randint(0, 1)
        self.left_var = left_var if tmp == 0 else right_var
        self.right_var = right_var if tmp == 0 else left_var
    
    # get random Arithmetic
    def Gen_Arithmetic(self):
        self.arithmetic_type = random.choice(list(MathematicalTypes))
        # print(self.arithmetic_type, self.arithmetic_type.value)


# Generate assignements, need a parents var
class Assignement:
    def __init__(self, parents_var = None) -> None:
        # AssignementType
        self.assignement_type = None
        # need a parents var
        self.parents_var = parents_var
        # 赋值语句的右边，可以是计算，也可以是简单的赋值，或者是一个函数调用
        # 或者函数指针
        self.children = None
        self.children_type = None
        # statements C code
        self.state_c_code = ""
    
    # gen right
    def Gen_Assigned_And_children(self, var_can_used=[]):
        self.assignement_type = random.choice(list(AssignementTypes))
        # gen random arithmetics
        self.Gen_RandomArithmetics(var_can_used)
    
    # gen random arithmetics
    def Gen_RandomArithmetics(self, var_can_used = []):
        # self.children = RandomArithmetics(left_var, right_var)
        # self.children.Gen_Arithmetic()
        num_of_arithmetics = random.randint(1, 5)
        for i in range(num_of_arithmetics):
            deep_of_arithmetics = random.randint(1, 4)
            for j in range(deep_of_arithmetics):
                left = random.choice(var_can_used)
                right = random.choice(var_can_used)
                tmp_ari = RandomArithmetics(left, right)
                tmp_ari.Gen_Arithmetic()
    
    # assignement statement to C code
    def Gen_Assignement_C_Code(self):
        self.state_c_code += self.parents_var.var_name
        self.state_c_code += " " + self.assignement_type.value

        self.state_c_code += " " + self.children.left_var.var_name
        self.state_c_code += " " + self.children.arithmetic_type.value
        self.state_c_code += " " + self.children.right_var.var_name
        self.state_c_code += ";"
        
# 生成 C 语句
class Statements:
    def __init__(self) -> None:
        # statements type, such as signed, if, while
        self.statement_type = None
        self.state = None
        # var has used in this statement
        self.var_used = []
        # the variables that can be used
        self.var_can_use = []
        
    # gen statements
    def Gen_Statements(self):
        self.Gen_Assignement()

    def Gen_Assignement(self):
        self.statement_type = StatementsTypes.Assignement
        self.state = Assignement()
        self.state.parents_var = random.choice(self.var_can_use)
        print("====== Gen_Assignement self.state.parents_var", self.state.parents_var)
        # need left var and right var
        tmp_left = random.choice(self.var_can_use)
        tmp_right = random.choice(self.var_can_use)
        self.state.Gen_Assigned_And_children(left_var=tmp_left, right_var=tmp_right)
        print("===== Gen_Assignement")
        print(self.state.parents_var, self.state.assignement_type)
        print(self.state.children.arithmetic_type, self.state.children.left_var, self.state.children.right_var)
        self.state.Gen_Assignement_C_Code()
        print(self.state.state_c_code)