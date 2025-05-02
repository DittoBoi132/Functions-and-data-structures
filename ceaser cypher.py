#ceaser cypher
word = input("Please enter a word: ")

def ceaserCypher(cyph):
    global newWord
    wordNum = []
    encryptWord=[]
    newWord = ""
    for i in word:
        wordNum.append(ord(i))
    for i in wordNum:
        encryptWord.append(chr(i+cyph))
    for i in encryptWord:
        newWord += i
    print(wordNum)
    print(encryptWord)
    print(newWord)

ceaserCypher(20)
word = newWord
ceaserCypher(-20)
