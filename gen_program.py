'''
Author: joessem jxxclj@gmail.com
Date: 2022-11-28 21:13:49
LastEditors: joessem jxxclj@gmail.com
LastEditTime: 2022-12-04 21:54:30
FilePath: \C-star\gen_program.py
Description: 
    The main class to generate program.
Copyright (c) 2022 by joessem jxxclj@gmail.com, All Rights Reserved. 
'''

import random
from code_blocks import  CodeBlock
from function import FunctionClass

class Gen_Program:
    def __init__(self) -> None:
        self.functions = []
        self.global_vars = []
    
    # main function
    def main(self):
        self.Gen_main_function()
    
    # build main function
    def Gen_main_function(self):
        main_func = FunctionClass()
        main_func.Build_main_function()
        self.functions.append(main_func)


gen_program = Gen_Program()
gen_program.main()