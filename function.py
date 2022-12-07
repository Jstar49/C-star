'''
Author: joessem jxxclj@gmail.com
Date: 2022-12-04 20:43:10
LastEditors: joessem jxxclj@gmail.com
LastEditTime: 2022-12-07 23:42:08
FilePath: \C-star\function.py
Description: 

Copyright (c) 2022 by joessem jxxclj@gmail.com, All Rights Reserved. 
'''
from code_blocks import  CodeBlock
from pkg import *
import random
import pdb

class FunctionClass:
    def __init__(self) -> None:
        self.function_name = None
        self.function_type = None
        self.function_blocks = []
        self.function_code = []
        self.var_can_used_function = []
        self.result_vars = []
    
    def main(self):
        pass
    
    # build main function
    def Build_main_function(self):
        self.function_name = "main"
        self.function_type = VarTypes.INT
        self.block_num = random.randint(1, 5)
        for i in range(self.block_num):
            self.Gen_code_block()
        print(self.result_vars)
        self.FunCode_Translation()
    
    # generate code block
    def Gen_code_block(self):
        block = CodeBlock(block_id=Get_BLOCKID())
        block.Generate_Code_Blocks_var()
        block.var_can_used_block += self.var_can_used_function
        self.var_can_used_function += block.block_new_var_list
        block.Gen_Block_statements()
        block.Generate_C_Source_CodeBlock()
        self.function_blocks.append(block)
        self.result_vars.append(random.choice(block.block_new_var_list))

    # generate c source code.
    def FunCode_Translation(self):
        tmp = self.function_type + " " + self.function_name + "() {"
        self.function_code.append(tmp)
        # pdb.set_trace()
        for block in self.function_blocks:
            for j in range(len(block.block_code)):
                self.function_code.append(INDENT + block.block_code[j])
        self.function_code.append("}")

        # print function code
        # for item in self.function_code:
        #     print(item)

