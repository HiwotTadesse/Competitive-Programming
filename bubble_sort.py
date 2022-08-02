#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swap = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] < a[j]:
                continue
            
            temp = a[i]
            a[i] = a[j] 
            a[j] = temp
            swap +=1
            
    print("Array is sorted in " + str(swap) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[len(a)-1]))
            
    
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
