# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
M = list(map(float, input().split()))
x = float(input())
print(float(np.polyval(M, x)))
