# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
l = list(map(int,input().split()))

m = int(input())
s = 0
for i in range(m):
    a, b = tuple(map(int,input().split()))
    if a in l:
        s += b
        l.remove(a)
print(s)
