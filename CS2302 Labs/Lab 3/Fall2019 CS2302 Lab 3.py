# Course:CS 2302 MW 1:30-2:50, Author:David Ayala
# Assignment:Lab #3, Instructor: Diego Aguirre
# Teaching Assistant: ????, Date of last Modification: 10/14/2019
# Purpose of program:write a function that reads the file and populates
# the binary search tree with all the English words contained in the file.
# Ask the user what type of binary search tree he/she wants to use
# (AVL Tree or Red-Black Tree).
# Write another function called count_anagrams that does not produce output,
# but returns the number of anagrams that a given word has.
# Finally, write another function that reads another file that contains words
# (feel free to create it yourself) and finds the
# word in the file that has the greatest number of anagrams.
from AVL import AVLNode
from AVL import AVLTree
from RedBlackT import RBT
from RedBlackT import RBTNode

def populateRBT(tempFile):
    pop = RBT()
    with open(tempFile) as file:
        for currentLine in file:
            temp = currentLine.split('\n')
            pop.insert(temp[0])
    countAnagrams(pop, 'spot')

def populateAVL(tempFile):
    pop = AVLTree()
    file = open(tempFile, 'r')
    for currentLine in file:
        temp = currentLine.split('\n')
        node = AVLNode(temp[0])
        pop.insert(node)
    countAnagrams(pop, 'spot')

def countAnagrams(tree, word, populated=True):
    listOfAnagram = []
    if populated:
        print('Anagrams: ', len(listOfAnagram))
    return listOfAnagram

def main():
    tempFile = 'words.txt'
    print('What kind of tree would you like to use?')
    print('1. AVL Tree.')
    print('2. Red AND Black Tree.')
    userInput = input()
    if userInput is '1':
        print('You have chosen a AVL Tree.')
        populateAVL(tempFile)
    elif userInput is '2':
        print('You have chosen a Red and Black Tree.')
        populateRBT(tempFile)
    else:
        print('enter either 1 or 2 for the respective tree.')
        print()
        main()

main()
