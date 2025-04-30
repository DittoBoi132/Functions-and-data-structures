#Bubble sort
List = []
i = 0
print("Enter the items for the list, enter -1 when done. \n")
while i != -1:
    i = int(input())
    if i == -1:
        pass
    else:
        List.append(i)
print(List)
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
bubbleSort()
