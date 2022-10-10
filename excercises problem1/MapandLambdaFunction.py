cube = lambda x: x**3
def fibonacci(n):
    if n < 2:
        return [x for x in range(n)]
    else:
        lst = [0, 1]
        for i in range(2,n):
            lst.append(lst[i-1] + lst[i-2])
        return lst
