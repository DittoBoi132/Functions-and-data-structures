import timeit
List = [6,3,1,8,4,9,2,5,7]
def insertSort():
    global sortedList
    global unsortedList
    global change
    unsortedList = List
    sortedList = []
    swap(0)
    change = 1
    while change != 0:
        if unsortedList == []:
            change = 1
        elif sortedList[0] > unsortedList[0]:
            swap(0)
        else:
            for i in range(len(sortedList)):
                if unsortedList != []:
                    if len(sortedList) == 1:
                        swap(i+1)
                        break
                    elif sortedList[-1] < unsortedList[0]:
                        swap(len(sortedList))
                        break
                    else:
                        i = 0
                        while sortedList[i] < unsortedList[0]:
                            i += 1
                        swap(i)
                        break

        if change == 1:
            change = 0
    print(sortedList,unsortedList)
def swap(s):
    global sortedList
    global unsortedList
    global change
    sortedList.insert(s,unsortedList[0])
    unsortedList.remove(List[0])
    change = 2
def bubbleSort():
    count = 0
    change = 1
    while change != 0:
        change = 1
        for i in range(len(List)-1):
            if List[i] > List[i+1]:
                temp = List[i]
                List[i] = List[i+1]
                List[i+1] = temp
                change = 2
        if change == 1:
            change = 0
    print(List)
print(timeit.timeit(insertSort, number=1))
print(timeit.timeit(bubbleSort, number=1))
