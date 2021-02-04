# Header
itemL = []


def getitemL(columns, rows):
    for i in range(int(rows)):
        rowData = input('').split()
        print(rowData)
        
        for ii in range(int(columns)):
            # print(rowData[ii])
            itemL.append(int(rowData[ii]))
            ii += 1
    
    # print(itemL)


rowsColumns = input('')
columns     = rowsColumns.split()[1]
rows        = rowsColumns.split()[0]
# print(f'Columns: {columns}')
# print(f'Rows: {rows}')

getitemL(columns, rows)



# Header
# Body

oriItemL = itemL.copy()

itemL.sort(reverse=True)
greatestNumsL = itemL[:3]
# print(f'oriItemL =  {oriItemL}')
# print(f'itemL = {itemL}')

greatestAdjacentIndexsL, greatestAdjacentNumsL = [], []
    

def luckyWinner(greatestNumsL):
    # print(f'greatestNumsL = {greatestNumsL}')

    for greatestNum in greatestNumsL:
        greatestAdjacentIndex = findGreatestAdjancent(greatestNum)
        greatestAdjacentIndexsL.append(greatestAdjacentIndex)
        greatestAdjacentNumsL.append(oriItemL[greatestAdjacentIndex])

    # print(f'greatestAdjacentIndexsL = {greatestAdjacentIndexsL}')
    chkAjacentDuplicate(greatestAdjacentIndexsL)
        

def findGreatestAdjancent(number):
    findGreatestNumL, findGreatestIndexL = [], []
    index = oriItemL.index(number)

    upIndex     = index-3
    downIndex   = index+3
    backIndex   = index-1
    fontIndex   = index+1

    if(upIndex>=0): 
        findGreatestNumL.append(oriItemL[upIndex])
    if(downIndex<len(oriItemL)): 
        findGreatestNumL.append(oriItemL[downIndex])
    if(backIndex<len(oriItemL) and backIndex%3!=2): 
        findGreatestNumL.append(oriItemL[backIndex])
    if(fontIndex>=0 and fontIndex%3!=0): 
        findGreatestNumL.append(oriItemL[fontIndex])

    findGreatestNumL.sort(reverse=True)

    for num in findGreatestNumL:
        findGreatestIndexL.append(oriItemL.index(num))

    print(f'Adjacent = {findGreatestNumL}')
    print(f'Number = {findGreatestNumL[0]}')
    print(f'Index = {oriItemL.index(max(findGreatestNumL))}')

    # print(findGreatestNumL)
    # return oriItemL.index(max(findGreatestNumL))
    return findGreatestIndexL


def chkAjacentDuplicate(greatestAdjacentIndexsL):
    duplicateIndexL, duplicateIndexInGreatestAdjacentIndexsL = [], []
    # duplicateIndexL = Null        # None (is null type in Python)

    for index, greatestAdjacentIndex in enumerate(greatestAdjacentIndexsL):

        if index == 0:
            duplicateIndex = greatestAdjacentIndex[0]
        else:
            if duplicateIndex == greatestAdjacentIndex[0]:
                duplicateIndexL.append(greatestAdjacentIndex[0])
                duplicateIndexInGreatestAdjacentIndexsL.append(index)
            
            duplicateIndex = greatestAdjacentIndex[0]
    
    print(duplicateIndexL)
    whichWorth(duplicateIndexInGreatestAdjacentIndexsL)



# ############### #
def whichWorth(duplicateIndexInGreatestAdjacentIndexsL):
    for index in duplicateIndexInGreatestAdjacentIndexsL:
        # print(index)
        # print(greatestAdjacentNumsL)
        # print(greatestAdjacentIndexsL)
        # print(f'HERE: {greatestNumsL}')
        # print(f'HERE: ')
        
        n = index
        if greatestAdjacentIndexsL[n-1][1] != greatestAdjacentIndexsL[n][1]:
            # x = greatestAdjacentIndexsL
            x = oriItemL[greatestAdjacentIndexsL[n-1][0]] + oriItemL[greatestAdjacentIndexsL[n][1]]
            y = oriItemL[greatestAdjacentIndexsL[n-1][1]] + oriItemL[greatestAdjacentIndexsL[n][0]]

            if(x>y):
                xTemp = greatestAdjacentIndexsL[n][0]
                greatestAdjacentIndexsL[n][0] = greatestAdjacentIndexsL[n][1]
                greatestAdjacentIndexsL[n][1] = xTemp
            else:
                yTmp = greatestAdjacentIndexsL[n-1][0]
                greatestAdjacentIndexsL[n-1][0] = greatestAdjacentIndexsL[n-1][1]
                greatestAdjacentIndexsL[n-1][1] = yTmp
                
    # print(greatestAdjacentIndexsL)
    sumAll()


def sumAll():
    result = 0

    for mainNum in greatestNumsL:
        # print(f'Num {mainNum}')
        result += mainNum
    
    # for adjacentIndex in greatestAdjacentIndexsL:
    for index, adjacentIndex in enumerate(greatestAdjacentIndexsL):
            # 3 TYPE of STRING CONCATENATION
        # print(f'Adjacent {oriItemL[adjacentIndex[0]]}')
        # print('Adjacent' + oriItemL[adjacentIndex[0]])
        # print('Adjacent : ' + str(oriItemL[adjacentIndex[0]]))
        result += oriItemL[adjacentIndex[0]]

    print(result)





luckyWinner(greatestNumsL)

# Body