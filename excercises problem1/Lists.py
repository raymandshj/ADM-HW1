if __name__ == '__main__':
    N = int(input())
    list = []
    for index in range(N):
        n = input().split()
        if "insert" == str(n[0]):
            list.insert(int(n[1]),int(n[2]))
        elif "print" == str(n[0]):    
            print(list)
        elif "remove" == str(n[0]):
            list.remove(int(n[1]))
        elif "append" == str(n[0]): 
            list.append(int(n[1]))
        elif "sort" == str(n[0]):
            list.sort()
        elif "pop" == str(n[0]):
            list.pop()
        elif "reverse" == str(n[0]):
            list.reverse()
