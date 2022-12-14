'''
Author: joessem jxxclj@gmail.com
Date: 2022-12-04 20:43:10
LastEditors: joessem jxxclj@gmail.com
LastEditTime: 2022-12-11 22:45:57
FilePath: \C-star\function.py
Description: 

Copyright (c) 2022 by joessem jxxclj@gmail.com, All Rights Reserved. 
'''
import random
import pdb

from code_statements import *
from code_blocks import  CodeBlock
from pkg import *


class FunctionClass:
    def __init__(self) -> None:
        self.function_name = None
        self.function_type = None
        self.function_blocks = []
        self.function_code = []
        self.var_can_used_function = []
        self.function_var_backup = []
        self.funtion_ret = None
    
    def main(self):
        pass
    
    # build main function
    def Build_main_function(self):
        self.function_name = "main"
        self.function_type = VarTypes.INT
        tmp = self.function_type + " " + self.function_name + "() {"
        self.function_code.append(tmp)
        self.block_num = random.randint(1, 5)
        for i in range(self.block_num):
            self.Gen_code_block()
        # block => c code
        self.FunCode_Translation()
        # print result
        self.Function_end_code()
        self.function_code.append("}")
    
    # generate code block
    def Gen_code_block(self):
        block = CodeBlock(block_id=Get_BLOCKID())
        block.Generate_Code_Blocks_var()
        block.var_can_used_block += self.var_can_used_function
        self.var_can_used_function += block.block_new_var_list
        block.Gen_Block_statements()
        block.Generate_C_Source_CodeBlock()
        self.function_blocks.append(block)
        if self.function_name == "main":
            self.function_var_backup.append(random.choice(block.block_new_var_list))

    # function ending code, return or printf
    def Function_end_code(self):
        if self.function_name == "main":
            print("self.funtion_ret.var_name", self.funtion_ret.var_name)
            tmp_c = Assignement(parents_var=self.funtion_ret)
            tmp_c.Gen_Assigned_And_children(self.function_var_backup)
            self.function_code.append(INDENT + tmp_c.state_c_code)
            tmp_c = f'''printf("RESULT : %llu\\n", result);'''
            self.function_code.append(INDENT + tmp_c)
        else:
            pass

    # generate c source code.
    def FunCode_Translation(self):
        # pdb.set_trace()
        for block in self.function_blocks:
            for j in range(len(block.block_code)):
                self.function_code.append(INDENT + block.block_code[j])
        

        # print function code
        # for item in self.function_code:
        #     print(item)

