'''
Author: joessem jxxclj@gmail.com
Date: 2022-11-26 23:53:50
LastEditors: joessem jxxclj@gmail.com
LastEditTime: 2022-12-04 23:18:37
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
        # var can be used in this block
        self.var_can_used_block = []
        self.block_statements = []
        self.block_code = []
    
    def main(self):
        pass
    
    # generate new vars
    def Generate_Code_Blocks_var(self):
        self.num_new_var = random.randint(1, self.max_init_var)
        for i in range(self.num_new_var):
            tmp_var = Get_Random_Type_Var()
            # print(tmp_var, tmp_var.val)
            tmp_var.var_name = "var_"+ str(self.block_id) + "_" + str(i)
            self.block_new_var_list.append(tmp_var)
        self.var_can_used_block += self.block_new_var_list
    
    # generate statements
    def Gen_Block_statements(self):
        statements_num = random.randint(1, 5)
        for i in range(statements_num):
            state = Statements()
            state.var_can_use = self.var_can_used_block
            state.Gen_Statements()
            self.block_statements.append(state)

    # generate C source code block
    def Generate_C_Source_CodeBlock(self):
        tmp = f'''/* ===== Block {self.block_id} ===== */'''
        self.block_code.append(tmp)
        # generate init vars
        self.Generate_Init_Vars_Source_Code()
        # statements
        for i in range(len(self.block_statements)):
            self.block_code.append(self.block_statements[i].c_code)
        self.block_code.append("")
        # print block codes
        # for i in range(len(self.block_code)):
        #     print(self.block_code[i])
    
    # generate init vars C source code
    def Generate_Init_Vars_Source_Code(self):
        print(" Generate_Init_Vars_Source_Code ", self.block_id)
        # print(" Generate_Init_Vars_Source_Code ", self.block_new_var_list)
        for var in self.block_new_var_list:
            # print(var)
            tmp_str = var.type_name.replace("_"," ") + " " + var.var_name + " = " + str(var.val) +";"
            self.block_code.append(tmp_str)
