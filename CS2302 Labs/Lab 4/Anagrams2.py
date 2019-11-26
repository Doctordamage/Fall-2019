from B_Tree import *
def fileReader():
    listOfWords = BTree()
    with open('words.txt', 'r', encoding='utf-8') as file:
        currentWord = file.readline()
        while currentWord:
            listOfWords.insert(currentWord)
            currentWord = file.readline().rstrip().lower()
    listOfWords.print_d('')
fileReader()

