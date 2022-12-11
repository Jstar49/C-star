'''
Author: joessem jxxclj@gmail.com
Date: 2022-11-28 21:13:49
LastEditors: joessem jxxclj@gmail.com
LastEditTime: 2022-12-11 22:45:12
FilePath: \C-star\gen_program.py
Description: 
    The main class to generate program.
Copyright (c) 2022 by joessem jxxclj@gmail.com, All Rights Reserved. 
'''

import os
import random

from Types import *
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
        self.result_variable = None

    # main function
    def main(self):
        # add includes
        self.Gen_includes()
        # result variable
        self.Gen_result_variable()
        # generate main function
        self.Gen_main_function()
    
    # C code libary includes
    def Gen_includes(self):
        tmp_c = "#include <stdio.h>"
        self.program_code.append(tmp_c)

    # generate result variable
    def Gen_result_variable(self):
        self.result_variable = LLong_t()
        self.result_variable.Random_values()
        self.result_variable.var_name = "result"
        tmp_c = "long long " + self.result_variable.var_name + " = " \
                + str(self.result_variable.val) + ";"
        self.program_code.append(tmp_c)
        self.global_vars.append(self.result_variable)

    # build main function
    def Gen_main_function(self):
        main_func = FunctionClass()
        main_func.funtion_ret = self.result_variable
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