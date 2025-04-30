#Start chains
a0 = []   #index 0
a1 = []   #index 1
a2 = []   #index 2
a3 = []   #index 3
a4 = []   #index 4
a5 = []   #index 5
a6 = []   #index 6
a7 = []   #index 7
a8 = []   #index 8
a9 = []   #index 9
#Hash table
#when changing size, must add more chains above
hashTab = [a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]
keySpace = []
temp = " "
temp2 = " "
#Can assign keySpace value above and ignore function bellow
def startList():
     global keySpace
     global temp
     print("Enter your list one number at a time please.\nEnter done when you finish. ")
     while temp != "done":
          temp = input()
          keySpace.append(temp)
     keySpace.pop()
#Store list in hash table
def hashDef():
     global keySpace
     for x in keySpace:
         #hash function
          temp = int(x) % len(hashTab)
          temp2 = hashTab[temp]
          temp2.append(int(x))
#search hash table for value
def srchHash():
     #could write as srchHash(item) and remove following line
     item = input("What value are you lookng for? ")
     item = int(item)
     index = int(item) % len(hashTab)
     found = False
     #selects chain
     chain = hashTab[index]
     #searches chain
     for guess in chain:
          if guess == item:
               found = True
               break
     if found:
          print("The value is in the list")
     else:
          print("The value is not in the list")
#print hash table
def prnHash():
    index = 0
    for item in hashTab:
        print("index",index,":",item)
        index+=1
#calling functions
startList()
hashDef()
srchHash()
prnHash()
