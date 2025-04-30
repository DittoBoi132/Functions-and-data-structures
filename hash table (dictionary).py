#Start hash table
hashTab = {0:(),1:(),2:(),3:(),4:(),5:(),6:(),7:(),8:(),9:()}
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
def ConASCII(x):
     global temp3
     temp3 = 0
     if not x.isdigit():
          for item in x:
               temp2 = ord(item)
               temp3 += temp2
     else:
          temp3 = x
def hashDef():
     global keySpace
     for x in keySpace:
          #Convert to ASCII
          ConASCII(x)
          #hash function
          temp = int(temp3) % len(hashTab)
          while hashTab[temp] != ():
               temp += 1
          hashTab[temp] = x
#search hash table for value
def srchHash():
     #could write as srchHash(item) and remove following line
     x = input("What value are you lookng for? ")
     ConASCII(x)
     index = int(temp3) % len(hashTab)
     while index != len(hashTab):
          if x == hashTab[index]:
               print("The value is in the list")
               return
          index += 1
     print("The value is not in the list")
#print hash table
def prnHash():
     for key,value in hashTab.items():
          print ("index",key,":", value)
#calling functions
startList()
hashDef()
srchHash()
