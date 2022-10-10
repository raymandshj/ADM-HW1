def average(array):
    # your code goes here
    result = sum(set(array))/len(set(array))
    x = '{0: .3f}'
    result = x.format(result)
    return result
