# Enter your code here. Read input from STDIN. Print output to STDOUT
m, n = map(int, input().split())
a_list, b_list = [], []
[a_list.append(input()) if i < m else b_list.append(input()) for i in range(m+n)]
result = []
for ch in b_list:
    num_list = ''
    for i in range(1, len(a_list)+1):
        if ch not in a_list:
            num_list += '-1'
            break
        if ch == a_list[i-1]:
            num_list += f'{i} '
    result.append(num_list)
for ele in result:
    print(ele)
