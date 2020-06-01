#!/bin/python3

import math
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
     
    temp=a[:d]
    rest = a[d:]
    a[0:(n-d)] = rest
    a[(n-d):] = temp
    for i in a:
        print(i,end=" ")
