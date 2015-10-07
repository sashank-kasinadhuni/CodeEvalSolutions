import os
import argparse


def File_size():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    print(str(os.path.getsize(args.path)).rstrip('L'))

File_size()
