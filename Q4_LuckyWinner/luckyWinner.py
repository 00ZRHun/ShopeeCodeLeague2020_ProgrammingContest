itemL = []

# START getitemL function
def getitemL(columns, rows):
    # for index, column in enumerate(columns):
    for i in range(int(rows)):
        rowData = input('').split()
        
        # for index, column in enumerate(columns):
        for ii in range(int(columns)):
            itemL.append(int(rowData[ii]))
            ii += 1
    # print(itemL)

# END getitemL function



rowsColumns = input('')
columns     = rowsColumns.split()[1]
rows        = rowsColumns.split()[0]
getitemL(columns, rows)


oriItemL = itemL.copy()
itemL.sort(reverse=True)
greatestNumsL = itemL[:3]


greatestAdjacentIndexsL, greatestAdjacentNumsL = [], []
    

# START luckyWinner function
def luckyWinner(greatestNumsL):

    for greatestNum in greatestNumsL:
        greatestAdjacentIndex = findGreatestAdjancent(greatestNum)
        greatestAdjacentIndexsL.append(greatestAdjacentIndex)
        # greatestAdjacentNumsL.append(itemL[greatestAdjacentIndex])

    chkAjacentDuplicate(greatestAdjacentIndexsL)
      
# END luckyWinner function   
     
# START findGreatestAdjancent function
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

    return findGreatestIndexL

# END findGreatestAdjancent function

# START chkAjacentDuplicate function
def chkAjacentDuplicate(greatestAdjacentIndexsL):
    duplicateIndexL, duplicateIndexInGreatestAdjacentIndexsL = [], []
    # duplicateIndexL = Null        # None

    for index, greatestAdjacentIndex in enumerate(greatestAdjacentIndexsL):
    
        if index == 0:
            duplicateIndex = greatestAdjacentIndex[0]
        else:
            if duplicateIndex == greatestAdjacentIndex[0]:
                duplicateIndexL.append(greatestAdjacentIndex[0])
                duplicateIndexInGreatestAdjacentIndexsL.append(index)
            
            duplicateIndex = greatestAdjacentIndex[0]
    
    # print(duplicateIndexL)
    whichWorth(duplicateIndexInGreatestAdjacentIndexsL)

# END chkAjacentDuplicate function

# START whichWorth function
def whichWorth(duplicateIndexInGreatestAdjacentIndexsL):
    for index in duplicateIndexInGreatestAdjacentIndexsL:
        n = index

        if greatestAdjacentIndexsL[n-1][1] != greatestAdjacentIndexsL[n][1]:

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
                
    sumAll()

# END whichWorth function

# START sumAll function
def sumAll():

    result = 0

    for mainNum in greatestNumsL:
        result += mainNum
    
    for index, adjacentIndex in enumerate(greatestAdjacentIndexsL):

            # STRING CONCATENATION (3 type of syntax) 
        # print('Adjacent' + oriItemL[adjacentIndex[0]])
        # print(f'Adjacent {oriItemL[adjacentIndex[0]]}')
        # print('Adjacent : ' + str(oriItemL[adjacentIndex[0]]))
        result += oriItemL[adjacentIndex[0]]

    print(result)

# END sumAll function


luckyWinner(greatestNumsL)