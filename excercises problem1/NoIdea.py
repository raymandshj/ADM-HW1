# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m  = map(int,input().split())
z = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
h = 0

for x in z:
    if x in A and x not in B:
        h += 1
    elif x in B and x not in A:
        h -= 1
    else:
        pass
print(h)
