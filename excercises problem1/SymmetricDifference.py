# Enter your code here. Read input from STDIN. Print output to STDOUT
M, a=int(input()),set(map(int,input().rsplit()))
N,b=int(input()),set(map(int,input().rsplit()))
[print(i) for i in sorted(list(a.difference(b).union(b.difference(a))))]
