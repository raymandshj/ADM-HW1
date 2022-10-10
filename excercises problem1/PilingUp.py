# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

for i in range(int(input())):
    i = input()
    blocks = deque([int(a) for a in input().split()])    
    for b in sorted(blocks, reverse=True):
        if b == blocks[0]: blocks.popleft()            
        elif b == blocks[-1]: blocks.pop()
        else: print('No'); break
    else:
        print('Yes')
