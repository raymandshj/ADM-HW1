

def person_lister(f):
    def inner(people):
        for person in people:
            person[2] = int(person[2])
        return map(f, sorted(people, key=operator.itemgetter(2)))
    return inner

