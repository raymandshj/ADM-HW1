
def mutate_string(string, position, character):
    a = list(string)
    a[position] = character
    return(''.join(a))
