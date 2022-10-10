

def arrays(arr):
    ar1 = []
    for i in arr:
        ar1.append(float(i))
    return numpy.array(ar1[::-1])
