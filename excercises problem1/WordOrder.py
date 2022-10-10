# Enter your code here. Read input from STDIN. Print output to STDOUT
words = {}
n = int(input())
for i in range(n):
    word = input()
    words[word] = words.get(word, 0) +1
print(len(words))
for i in words.values():
    print(i,end= ' ')
