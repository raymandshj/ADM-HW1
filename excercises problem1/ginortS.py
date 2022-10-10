# Enter your code here. Read input from STDIN. Print output to STDOUT
S=list(input())

number=[]
lower=[]
upper=[]
for i in S:
    if i.isdigit():
        number.append(i)
    else:
        if i.isupper():
            upper.append(i)
        else:
            lower.append(i)

a=sorted(list(map(int,number)))
b=list(map(str,sorted(a,key=lambda x:x%2==0)))

print(''.join(sorted(lower))+''.join(sorted(upper))+''.join(b))
