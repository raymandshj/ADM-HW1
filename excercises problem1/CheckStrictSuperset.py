# Enter your code here. Read input from STDIN. Print output to STDOUT
set_A = set(map(int, input().split()))
N = int(input())
list_sets = []
for i in range (N):
    list_sets.append(set(map(int,input().split())))
        
print(all(set_A.issuperset(s) for s in list_sets))
