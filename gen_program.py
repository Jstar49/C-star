import os
import random

from pkg import *
from Types import *
from base_op_func import base_op_c
from config import args
from code_blocks import  CodeBlock
from function import FunctionClass


class Gen_Program:
    def __init__(self) -> None:
        self.functions = []
        self.global_vars = []
        self.outfile = args.o
        self.program_header = []
        self.program_code = []
        # self.program_result_vars = []
        self.result_variable = None
        self.function_num = 0
        # if complexity >= 3, add functions
        if args.complexity >= 3:
            self.function_num = random.randint(2, args.complexity)

    # main function
    def main(self):
        # add includes
        self.Gen_includes()
        # result variable
        self.Gen_result_variable()
        # generate some functions
        self.Gen_Functions()
        # generate main function
        self.Gen_main_function()
    
    # C code libary includes
    def Gen_includes(self):
        tmp_c = "#include <stdio.h>"
        self.program_header.append(tmp_c)
        tmp_c = "#include <stdint.h>"
        self.program_header.append(tmp_c)

    # generate result variable
    def Gen_result_variable(self):
        self.result_variable = INT64_T()
        self.result_variable.Random_values()
        self.result_variable.var_name = "result"
        tmp_c = "long long " + self.result_variable.var_name + " = " \
                + str(self.result_variable.val) + ";"
        self.program_code.append(tmp_c)
        self.global_vars.append(self.result_variable)
    
    # generate some functions
    def Gen_Functions(self):
        for i in range(self.function_num):
            fun_name = f"func_{i}"
            tmp_func = FunctionClass()
            tmp_func.function_name = fun_name
            tmp_func.function_can_called = self.functions[:]
            tmp_func.main()
            self.functions.append(tmp_func)
            self.program_code += tmp_func.function_code


    # build main function
    def Gen_main_function(self):
        main_func = FunctionClass()
        main_func.funtion_ret = self.result_variable
        main_func.function_can_called = self.functions[:]
        main_func.Build_main_function()
        self.functions.append(main_func)
        self.program_code += main_func.function_code

    # outout c source file
    def Output(self):
        header_info = ["/* "] + PROGRAM_INFO + ["*/"]
        self.program_code = header_info + self.program_header + base_op_c.Build_operator_codes() \
                             + self.program_code
        f = open(self.outfile, "w")
        for line in self.program_code:
            f.write(line + "\n")
        f.close()


# gen_program = Gen_Program()
# gen_program.main()