# Course:CS 2302 MW 1:30-2:50, Author:David Ayala
# Assignment:Lab #5, Instructor: Diego Aguirre
# Teaching Assistant: ????, Date of last Modification: 9/10/2019
import time
import PartA as lru
from PartA import *
import PartB as heap

print('Part A')
start1 = time.time()
notSureWhatToCallThis = lru.LRU(5)

print('Using method put.')
notSureWhatToCallThis.put(1, 1)
notSureWhatToCallThis.put(2, 2)
notSureWhatToCallThis.put(3, 3)
notSureWhatToCallThis.put(4, 4)
notSureWhatToCallThis.put(5, 5)
notSureWhatToCallThis.put(4, 16)
notSureWhatToCallThis.put(4, 9)
#notSureWhatToCallThis.put(2, 2)
#notSureWhatToCallThis.put(2, 8)
#notSureWhatToCallThis.put(3, 3)
#notSureWhatToCallThis.put(1, 6)
print()
print('Showing method get.')
print('key value:')
print(LRU.get(notSureWhatToCallThis, 1))
print(LRU.get(notSureWhatToCallThis, 2))
print(LRU.get(notSureWhatToCallThis, 3))
print(LRU.get(notSureWhatToCallThis, 4))
print(LRU.get(notSureWhatToCallThis, 5))
print()
notSureWhatToCallThis.print()
print('Current size of Keys:', LRU.size(notSureWhatToCallThis))
print('Maximum capacity of table:', notSureWhatToCallThis.maxCap)
end1 = time.time()
print('Running time:')
print(end1 - start1)
print('seconds.')
print()

print('Part B')
start2 = time.time()
file = 'testfile.txt'
heap, dictionary = heap.MaximumHeap.fileReader(file)
heap.printInDescendingOrder(heap.size())
end2 = time.time()
print('Running time:')
print(end2 - start2)
print('seconds.')
