import time
from EditDistance import *
str1 = 'miners'
str2 = 'money'

print('the first string (word) is:')
print(str1)
print()
print('the second string (word) is:')
print(str2)
print()
start = time.time()
EditDistance(str1, str2)
end = time.time()
print('Running time:')
print(end - start)
print('seconds.')

