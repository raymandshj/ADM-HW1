def count_substring(string, sub_string):
    count=0
    for x in range(len(string)-len(sub_string)+1):
        A=True
        for j in range(len(sub_string)):
            if sub_string[j]==string[x+j]:A=A and True
            else:
                A=False
                break
        if A==True:count+=1
    return count

