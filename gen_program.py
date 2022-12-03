'''
Author: joessem jxxclj@gmail.com
Date: 2022-11-28 21:13:49
LastEditors: joessem jxxclj@gmail.com
LastEditTime: 2022-12-04 00:34:37
FilePath: \C-star\gen_program.py
Description: 
    The main class to generate program.
Copyright (c) 2022 by joessem jxxclj@gmail.com, All Rights Reserved. 
'''

import random
from code_blocks import  CodeBlock

class Gen_Program:
    def __init__(self) -> None:
        pass

    # generate code block
    def Gen_code_block(self):
        block = CodeBlock()
        block.Generate_Code_Blocks_var()
        block.Gen_Block_statements()
        block.Generate_C_Source_CodeBlock()

gen_program = Gen_Program()
gen_program.Gen_code_block()