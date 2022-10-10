# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

n, m, p = map(int, input().split())
nexp=[]
mexp=[]

for _ in range(n):
    nexp.append(np.array(list(map(int, input().split()))))

for _ in range(m):
    mexp.append(np.array(list(map(int, input().split()))))

print(np.concatenate((nexp, mexp), axis=0))
