#Program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple.

def main():
    inputTuples = input('Enter a list of tuples separated by comma: ') # Accepting tuples Eg. (a,a),(b,b)
    listOfTuples = []       # Initialising a list for input tuples

    for tup in inputTuples.split('),('):    # tup '(a,a)' after splitting: '(a,a'
        tup = tup.replace(')','').replace('(','')       # tup now 'a,a'
        listOfTuples.append(tuple(tup.split(',')))

    print(sort(listOfTuples))


# This function returns last element of the tuples
def returnLastElement(val):
    return val[-1]


# List of tupples is sorted based on the last element in the tuples
def sort(listOfTuples):
    return sorted(listOfTuples, key= returnLastElement)


if __name__ == "__main__":
    main()
