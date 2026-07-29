# Radix sort
mylist = [11, 64, 34, 25, 22, 12, 42, 5, 30, 5]

def radixSort(inputlist):

    n = len(inputlist)
    if n <= 1:
        return inputlist

    max_value = max(inputlist) 
    exp = 10

    radixArray = []

    while max_value//exp > 0:
        for _ in range(n):
            radixArray.append([])

        for val in inputlist:
            index = val % exp
            radixArray[index].append(val)
        exp *= 10

    print(radixArray)

radixSort(mylist)