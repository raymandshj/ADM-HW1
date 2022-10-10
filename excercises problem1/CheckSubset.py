# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())
for i in range(x):
    el_A=int(input())
    A= set(map(int,input().split()))
    el_B=int(input())
    B= set(map(int,input().split()))
    inter=A.intersection(B)
    if inter==A :
        print(True)
    else:
        print(False)
