'''
Author: joessem jxxclj@gmail.com
Date: 2022-11-22 23:41:03
LastEditors: joessem jxxclj@gmail.com
LastEditTime: 2022-12-13 22:20:47
FilePath: \C-star\config.py
Description: 
    configs
Copyright (c) 2022 by joessem jxxclj@gmail.com, All Rights Reserved. 
'''

import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--complexity", type=int, default=1,
                        help="--complexity=<n>, control program size and complexity, default 1")
    parser.add_argument("--target", choices=[32,64], type=int, default=32,
                        help="32 bit program or 64 bit program, default 32")
    parser.add_argument("--o", type=str, default="main.c",
                        help="--o <output file>")
    args = parser.parse_args()
    return args


args = parse_args()
# print(args)