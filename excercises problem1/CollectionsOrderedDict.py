# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
od = OrderedDict()
for i in range(int(input())):
    n = input().split()
    name = ' '.join([n[i] for i in range(len(n) - 1)])
    price = int(n[-1])
    if name in od:
        od[name] += price
    else:
        od[name] = price
for item in od:
    print(f"{item} {od[item]}")
