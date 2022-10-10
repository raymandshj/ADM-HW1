# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(map(int, input().split()))
for i in range(int(input())):
    cmd = input().strip().split()
    op= set(map(int, input().split())) 
    eval("A." + cmd[0] + "(op)")
print(sum(A))
