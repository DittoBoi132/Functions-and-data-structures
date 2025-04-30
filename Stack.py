#Stack functions
stack = []
empty = True
full = False
maxLen = 20
top = -1
#Define max length of stack
def isEmpty():
    if len(stack) == 0:
        print("Stack underflow")
        global empty
        empty = True
        full = False
    else:
        empty = False
def isFull():
    if len(stack) == maxLen:
        print("Stack oerflow")
        global full
        full = True
        Empty = False
    else:
        full = False
def pop():
    isEmpty()
    if empty == True:
        pass
    else:
        global top
        print(stack[top])
        stack.pop(top)
        #add to list
        #item = top
        #list.append(item)
        top = top - 1
    full = False
def push(item):
    isFull()
    if full == True:
        pass
    else:
        global top
        top = top + 1
        #remove item from list here
        #list.pop(item)
        stack.append(item)
    empty = False
def peek():
    isEmpty()
    print(stack[top])
def size():
    print(len(stack))
def prinStack():
    isEmpty()
    if empty == True:
        pass
    else:
        print(stack)
isEmpty()
isFull()
push(item)
pop()
peek()
size()
prinStack()
