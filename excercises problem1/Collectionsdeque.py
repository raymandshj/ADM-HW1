# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
n = int(input())
list = []

for i in range(n):
    list = [i for i in input().split()]
    
    if 'append' in list:
        d.append(int(list[1]))
    
    elif 'appendleft' in list:
        d.appendleft(int(list[1]))
        
    elif 'pop' in list:
        d.pop()
        
    elif 'popleft' in list:
        d.popleft()

for el in d:
    print(el, end=' ')
