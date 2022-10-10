# Enter your code here. Read input from STDIN. Print output to STDOUT
studs, subj = map(int,input().split())
score_list = []
for i in range(int(subj)):
    scores = list(map(float, input().split()))
    score_list.append(scores)

for i in zip(*score_list):
    print(sum(i)/subj)
