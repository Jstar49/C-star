'''
Author: joessem jxxclj@gmail.com
Date: 2022-11-28 21:13:49
LastEditors: joessem jxxclj@gmail.com
LastEditTime: 2022-12-07 23:12:02
FilePath: \C-star\gen_program.py
Description: 
    The main class to generate program.
Copyright (c) 2022 by joessem jxxclj@gmail.com, All Rights Reserved. 
'''

import random

from config import args
from code_blocks import  CodeBlock
from function import FunctionClass

class Gen_Program:
    def __init__(self) -> None:
        self.functions = []
        self.global_vars = []
        self.outfile = args.o
        self.program_code = []
        # self.program_result_vars = []

    # main function
    def main(self):
        self.Gen_main_function()
    
    # build main function
    def Gen_main_function(self):
        main_func = FunctionClass()
        main_func.Build_main_function()
        self.functions.append(main_func)
        self.program_code += main_func.function_code

    # outout c source file
    def Output(self):
        f = open(self.outfile, "w")
        for line in self.program_code:
            f.write(line + "\n")
        f.close()


# gen_program = Gen_Program()
# gen_program.main()