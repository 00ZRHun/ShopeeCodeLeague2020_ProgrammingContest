# itemListOri = [1, 3, 2, 5, 4, 6, 8, 9, 7]
# itemList    = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# itemList = [1, 3, 2, 
#             5, 4, 6, 
#             8, 9, 7]
itemList = [100, -9, -1,
            -1, 3, 2, 
            -9, 2, 3,
            2, 5, 1,
            3, 3, 4]
itemListOri = itemList.copy()

itemList.sort(reverse=True)
greatestNums = itemList[:3]
print(f'itemListOri =  {itemListOri}')
print(f'itemList = {itemList}')

# (greatestAdjacentIndexs, greatestAdjacentNums) = []
greatestAdjacentIndexs  = []
greatestAdjacentNums    = []

# def findGreatest3Num(itemListOri):
#     itemListOri = itemList.copy()
#     itemList.sort(reverse=True)
    # print(itemList)
    

def storeListofGreatest3NumAndIndexes(greatestNums):
    # greatestNums = itemList[:3]
    # print(itemListWith3GreatestNum)
    print(f'greatestNums = {greatestNums}')

    for greatestNum in greatestNums:
        greatestAdjacentIndex = findGreatestAdjancent(greatestNum)
        greatestAdjacentIndexs.append(greatestAdjacentIndex)
        # greatestAdjacentNums.append(itemList[greatestAdjacentIndex])

    print(f'greatestAdjacentIndexs = {greatestAdjacentIndexs}')
    chkAjacentDuplicate(greatestAdjacentIndexs)
        



def findGreatestAdjancent(number):
    findGreatestList = []
    index = itemListOri.index(number)
    # print(index)

    upIndex     = index-3
    downIndex   = index+3
    backIndex   = index-1
    fontIndex   = index+1

    if(upIndex>=0): 
        findGreatestList.append(itemListOri[upIndex])
    if(downIndex<len(itemListOri)): 
        findGreatestList.append(itemListOri[downIndex])
    if(backIndex<len(itemListOri) and backIndex%3!=2): 
        findGreatestList.append(itemListOri[backIndex])
    if(fontIndex>=0 and fontIndex%3!=0): 
        findGreatestList.append(itemListOri[fontIndex])

    findGreatestList.sort(reverse=True)

    print(f'Adjacent = {findGreatestList}')
    print(f'Number = {findGreatestList[0]}')
    print(f'Index = {itemListOri.index(max(findGreatestList))}')
    # print(findGreatestList)
    return itemListOri.index(max(findGreatestList))


def chkAjacentDuplicate(greatestAdjacentIndexs):
    print(123)


def find(number):
    findGreatestList = []
    index = itemListOri.index(number)
    # if(upIndex     = index-3 >0):
    upIndex     = index-3
    downIndex   = index+3
    fontIndex   = index+1
    backIndex   = index-1
    
    # testingIndex = backIndex

    # *** shorthand
    # for index in indexs
    if(upIndex>=0): 
        findGreatestList.append(itemListOri[upIndex])
    if(downIndex>=0): 
        findGreatestList.append(itemListOri[downIndex])
    # if(fontIndex>=0 & fontIndex%3!=0): 
    # if(fontIndex%3!=0 and fontIndex>=0): 
    if(fontIndex>=0 and fontIndex%3!=0): 
        findGreatestList.append(itemListOri[fontIndex])
    # if(backIndex>=0 & backIndex%3!=2): 
    # if(backIndex>=0 & backIndex%3==0): 
    # if(backIndex%3!=2 & backIndex>=0): 
    # if(backIndex>=0 and backIndex%3!=2): 
    if(backIndex%3!=2 and backIndex>=0): 
        findGreatestList.append(itemListOri[backIndex])

    findGreatestList.sort(reverse=True)

    print(findGreatestList)
    

storeListofGreatest3NumAndIndexes(greatestNums)