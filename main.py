# Insertion sort - treat the first element as the initial sorted element, and rest are unsorted elements
mylist = [11, 5, 64, 34, 25, 22, 12, 42, 5, 50, 90, 100]

# i = 1 (current_value=5, index=1), j=0(index=0), mylist[1] = 11, mylist[0]=5
# mylist = [5, 11, 64, 34, 25, 22, 12, 42, 5, 50, 90, 100]
# # i = 2 (current_value=64, index=2), j=1, j=0
# # mylist = [5, 11, 64, 34, 25, 22, 12, 42, 5, 50, 90, 100]
# # # i = 3 (current_value=34, index=3), j=2(index=2), mylist[3] = 64, mylist[2] = 34
# # # mylist = [5, 11, 34, 64, 25, 22, 12, 42, 5, 50, 90, 100]
# # # # i = 4, (current)

 
n = len(mylist)
print(mylist)

for i in range(1, n):
    current_value = mylist[i] 
    index = i

    for j in range(i - 1, -1, -1):
        print(mylist[j], mylist[i])

        if mylist[i] < mylist[j]: # if unsorted element is smaller than sorted element:
            index = j
            mylist[j+1] = mylist[j]
    if index != i:
        mylist[index] = current_value

        """
        if mylist[i] < mylist[j]: # if unsorted element is smaller than sorted element
            pop_value = mylist.pop(i) # remove it from unsorted portion => elements after index i shifted to left by 1 
            mylist.insert(j, pop_value) # insert it into the sorted portion => elements after index j shifted to right by 1
            break
        """

    print(mylist)


