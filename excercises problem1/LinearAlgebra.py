# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
N = int(input())
M = [list(map(float, input().split())) for i in range(N)]
print(round(np.linalg.det(M),2))
