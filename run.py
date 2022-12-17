import os
import sys

from pkg import *
from config import args
from gen_program import Gen_Program
import random

def main():
    # try:
    if args.complexity < 1 or args.complexity > 100:
        print("complexity must in range [1, 100] ")
        exit(0)
    if args.o == "":
        print("need a argment : --i <outfile>")
    if args.seed is not None:
        random.seed(args.seed)
    else:
        seed = random.randrange(sys.maxsize)
        args.seed = seed
        random.seed(args.seed)
    INFO_logging(f"seed : {args.seed}")
    
    gen_program = Gen_Program()
    gen_program.main()
    gen_program.Output()
    # except:
    #     print("Error")

if __name__ == "__main__":
    main()
    # print(sys.executable)