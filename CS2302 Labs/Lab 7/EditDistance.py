def EditDistance(str1, str2):
    array2D = []
    for i in range(len(str1) + 1):
        array2D.append([-1] * (len(str2) + 1))
    for i in range(len(str1) + 1):
        array2D[i][0] = i
    for i in range(len(str2) + 1):
        array2D[0][i] = i
    actualEditDistance(array2D,str1,str2)

def actualEditDistance(array2D,str1,str2):
    if array2D is None:
        return 'Error'
    else:
        for i in range(1, len(array2D)):
            for j in range(1, len(array2D[i])):
                if str1[i - 1] == str2[j - 1]:
                    array2D[i][j] = array2D[i - 1][j - 1]
                else:
                    array2D[i][j] = min(array2D[i - 1][j], array2D[i][j - 1], array2D[i - 1][j - 1]) + 1
    print(array2D)
    print()
    print('the edit distance of the two strings is:')
    lastElementOfarray2D(array2D)

def lastElementOfarray2D(array2D):
    count = 0
    for eachList in array2D:
        count += 1
        if count == (len(array2D)):
            lastElement = eachList[-1]
            print(lastElement)



