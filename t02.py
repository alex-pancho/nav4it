#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'consecutive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER num as parameter.
#

def consecutive(num):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num = int(input().strip())

    result = consecutive(num)

    fptr.write(str(result) + '\n')

    fptr.close()
