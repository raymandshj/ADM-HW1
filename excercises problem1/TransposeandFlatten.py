# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n,m = list(map(int, input().split()))
lists = []
for i in range(n):
    lists.append(input().split())
lists2 = np.array(lists, int)
lists = np.array(lists, int)
lists2 = lists2.transpose()
print(lists2)
lists = lists.flatten()
print(lists)
