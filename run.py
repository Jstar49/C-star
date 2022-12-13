'''
Author: joessem jxxclj@gmail.com
Date: 2022-11-22 21:02:50
LastEditors: joessem jxxclj@gmail.com
LastEditTime: 2022-12-13 22:36:27
FilePath: \C-star\run.py
Description: 
    Run the program to generate C source code.
Copyright (c) 2022 by joessem jxxclj@gmail.com, All Rights Reserved. 
'''

import os
import sys

from config import args
from gen_program import Gen_Program

def main():
    # try:
    if args.complexity < 1 or args.complexity > 100:
        print("complexity must in range [1, 100] ")
        exit(0)
    if args.o == "":
        print("need a argment : --i <outfile>")
    gen_program = Gen_Program()
    gen_program.main()
    gen_program.Output()
    # except:
    #     print("Error")

if __name__ == "__main__":
    main()
    # print(sys.executable)