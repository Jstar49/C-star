import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--complexity", type=int, default=1,
                        help="--complexity=<n>, control program size and complexity, default 1")
    parser.add_argument("--target", choices=[32,64], type=int, default=32,
                        help="32 bit program or 64 bit program, default 32")
    parser.add_argument("--o", type=str, default="main.c",
                        help="--o <output file>")
    parser.add_argument("--seed", type=int, default=None,
                        help="--seed <random seed>")
    args = parser.parse_args()
    return args


args = parse_args()
# print(args)