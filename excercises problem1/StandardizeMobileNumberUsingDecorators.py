def wrapper(f):
    def fun(l):
        list = []
        for item in l:
            list.append('+91 '+item[-10:-5]+' '+ item[-5:])
        return f(list)
    return fun

