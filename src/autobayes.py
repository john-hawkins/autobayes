# -*- coding: utf-8 -*-
 
"""src.autobayes: provides entry point main()."""
 
__version__ = "0.1.2"

import numpy as np
import pandas as pd
import sys
import os

 
def main():
    if len(sys.argv) < 4:
        print("ERROR: MISSING ARGUMENTS")
        print_usage(sys.argv)
        exit(1)
    else:
        datetime_col = sys.argv[1]
        target_col = sys.argv[2]
        train_dataset = sys.argv[3]
        output_dir = sys.argv[5]

        filesize = os.stat(train_dataset).st_size

        if filesize<max_filesize:
            prepare_results_folder(output_dir)
            prepare_data(train_dataset, datetime_col, target_col, output_dir) 
        else:
            print("Dataset too large for current version")


def print_usage(args):
    """ Command line application usage instrutions. """
    print("USAGE ")
    print(args[0], " <datetime column> <target column> <training data> <results dir> ")
    print("")


