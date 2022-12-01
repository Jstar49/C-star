'''
Author: joessem jxxclj@gmail.com
Date: 2022-11-26 23:53:50
LastEditors: joessem jxxclj@gmail.com
LastEditTime: 2022-11-28 22:52:20
FilePath: \C-star\code_blocks.py
Description: 
    Code Blocks 
Copyright (c) 2022 by joessem jxxclj@gmail.com, All Rights Reserved. 
'''

from Types import *
from code_statements import *
import random

class CodeBlock:
    def __init__(self, block_id = 0, max_init_var = 5) -> None:
        # bock id
        self.block_id = block_id
        # num of new vars
        self.max_init_var = max_init_var
        self.num_new_var = None
        # var init queue
        self.block_new_var_list = []
        self.c_source_block = []
    
    # generate new vars
    def Generate_Code_Blocks_var(self):
        self.num_new_var = random.randint(1, self.max_init_var)
        for i in range(self.num_new_var):
            tmp_var = Get_Random_Type_Var()
            # print(tmp_var, tmp_var.val)
            tmp_var.var_name = "var_"+ str(self.block_id) + "_" + str(i)
            self.block_new_var_list.append(tmp_var)
    
    # generate statements
    def Gen_statements(self):
        state = Statements()
        state.var_can_use = self.block_new_var_list
        state.Gen_Statements()

    # generate C source code block
    def Generate_C_Source_CodeBlock(self):
        # generate init vars
        self.Generate_Init_Vars_Source_Code()
    
    # generate init vars C source code
    def Generate_Init_Vars_Source_Code(self):
        print(" Generate_Init_Vars_Source_Code ", self.block_id)
        # print(" Generate_Init_Vars_Source_Code ", self.block_new_var_list)
        for var in self.block_new_var_list:
            # print(var)
            tmp_str = var.type_name + " " + var.var_name + " = " + str(var.val) +";"
            self.c_source_block.append(tmp_str)
            print(tmp_str)
