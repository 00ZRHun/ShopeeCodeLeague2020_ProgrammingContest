# oriItemL = [1, 3, 2, 5, 4, 6, 8, 9, 7]
# itemL    = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# itemL = [1, 3, 2, 
#             5, 4, 6, 
#             8, 9, 7]
itemL = [100, -9, -1,
            -1, 3, 2, 
            -9, 2, 3,
            2, 5, 1,
            3, 3, 4]
oriItemL = itemL.copy()

itemL.sort(reverse=True)
greatestNumsL = itemL[:3]
print(f'oriItemL =  {oriItemL}')
print(f'itemL = {itemL}')

# (greatestAdjacentIndexsL, greatestAdjacentNumsL) = []
greatestAdjacentIndexsL  = []
greatestAdjacentNumsL    = []

# def findGreatest3Num(oriItemL):
#     oriItemL = itemL.copy()
#     itemL.sort(reverse=True)
    # print(itemL)
    

def storeListofGreatest3NumAndIndexes(greatestNumsL):
    # greatestNumsL = itemL[:3]
    # print(itemLWith3GreatestNum)
    print(f'greatestNumsL = {greatestNumsL}')

    for greatestNum in greatestNumsL:
        greatestAdjacentIndex = findGreatestAdjancent(greatestNum)
        greatestAdjacentIndexsL.append(greatestAdjacentIndex)
        # greatestAdjacentNumsL.append(itemL[greatestAdjacentIndex])

    print(f'greatestAdjacentIndexsL = {greatestAdjacentIndexsL}')
    chkAjacentDuplicate(greatestAdjacentIndexsL)
        



def findGreatestAdjancent(number):
    findGreatestNumL, findGreatestIndexL = [], []
    index = oriItemL.index(number)
    # print(index)

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
    # duplicateIndexL = Null

    # for greatestAdjacentIndex in greatestAdjacentIndexsL:
    for index, greatestAdjacentIndex in enumerate(greatestAdjacentIndexsL):
        # print(index, greatestAdjacentIndex)
    
        if index == 0:
            duplicateIndex = greatestAdjacentIndex[0]
        else:
            if duplicateIndex == greatestAdjacentIndex[0]:
                duplicateIndexL.append(greatestAdjacentIndex[0])
                duplicateIndexInGreatestAdjacentIndexsL.append(index)
            
            duplicateIndex = greatestAdjacentIndex[0]
    
    print(duplicateIndexL)
    whichWorth(duplicateIndexInGreatestAdjacentIndexsL)


def whichWorth(duplicateIndexInGreatestAdjacentIndexsL):
    for index in duplicateIndexInGreatestAdjacentIndexsL:
        print(index)
        print(greatestAdjacentNumsL)
        print(greatestAdjacentIndexsL)
        
        n = index
        if greatestAdjacentIndexsL[n-1][1] != greatestAdjacentIndexsL[n][1]:
            # x = greatestAdjacentIndexsL
            x = oriItemL[greatestAdjacentIndexsL[n-1][0]] + greatestAdjacentIndexsL[n][1]
            y = oriItemL[greatestAdjacentIndexsL[n-1][1]] + greatestAdjacentIndexsL[n][0]

            if(x>y):
                xTemp = greatestAdjacentIndexsL[n][0]
                greatestAdjacentIndexsL[n][0] = greatestAdjacentIndexsL[n][1]
                greatestAdjacentIndexsL[n][1] = xTemp
            else:
                yTmp = greatestAdjacentIndexsL[n-1][0]
                greatestAdjacentIndexsL[n-1][0] = greatestAdjacentIndexsL[n-1][1]
                greatestAdjacentIndexsL[n-1][1] = yTmp
                


    print(greatestAdjacentIndexsL)
    # x = 




def find(number):
    findGreatestNumL = []
    index = oriItemL.index(number)
    # if(upIndex     = index-3 >0):
    upIndex     = index-3
    downIndex   = index+3
    fontIndex   = index+1
    backIndex   = index-1
    
    # testingIndex = backIndex

    # *** shorthand
    # for index in indexs
    if(upIndex>=0): 
        findGreatestNumL.append(oriItemL[upIndex])
    if(downIndex>=0): 
        findGreatestNumL.append(oriItemL[downIndex])
    # if(fontIndex>=0 & fontIndex%3!=0): 
    # if(fontIndex%3!=0 and fontIndex>=0): 
    if(fontIndex>=0 and fontIndex%3!=0): 
        findGreatestNumL.append(oriItemL[fontIndex])
    # if(backIndex>=0 & backIndex%3!=2): 
    # if(backIndex>=0 & backIndex%3==0): 
    # if(backIndex%3!=2 & backIndex>=0): 
    # if(backIndex>=0 and backIndex%3!=2): 
    if(backIndex%3!=2 and backIndex>=0): 
        findGreatestNumL.append(oriItemL[backIndex])

    findGreatestNumL.sort(reverse=True)

    print(findGreatestNumL)
    

storeListofGreatest3NumAndIndexes(greatestNumsL)