# Enter your code here. Read input from STDIN. Print output to STDOUT
s = set({})
CountCountries=int(input())
for x in range(CountCountries):
    y=input()
    s.add(y)
print(len(s))
