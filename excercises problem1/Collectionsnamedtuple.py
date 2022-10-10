# Enter your code here. Read input from STDIN. Print output to STDOUT
n, nt = int(input()), tuple(map(str,input().split()))
marks = [int(input().split()[nt.index('MARKS')]) for _ in range(n)]
print(sum(marks)/len(marks))
