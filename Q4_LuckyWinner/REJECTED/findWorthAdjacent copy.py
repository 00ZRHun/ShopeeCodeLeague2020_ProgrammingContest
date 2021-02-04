itemListOri = [1, 3, 2, 5, 4, 6, 8, 9, 7]
itemList    = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def findGreatest3Num(itemListOri):
    itemListOri = itemList.copy()
    itemList.sort(reverse=True)

    storeListofGreatest3NumAndIndexes(itemList)
    # print(itemList)
    

def storeListofGreatest3NumAndIndexes(itemList):
    itemListWith3GreatestNum = itemList[:3]
    print(itemListWith3GreatestNum)



def findGreatestAdjancent(number):
    findGreatestList = []
    index = itemListOri.index(number)
    # print(index)

    upIndex     = index-3
    downIndex   = index+3
    fontIndex   = index+1
    backIndex   = index-1

    if(upIndex>=0): 
        findGreatestList.append(itemListOri[upIndex])
    if(downIndex<len(itemListOri)): 
        findGreatestList.append(itemListOri[downIndex])
    if(fontIndex>=0 and fontIndex%3!=0): 
        findGreatestList.append(itemListOri[fontIndex])
    if(backIndex<len(itemListOri) and backIndex%3!=2): 
        findGreatestList.append(itemListOri[backIndex])

    findGreatestList.sort(reverse=True)

    print(findGreatestList)
    print(findGreatestList[0])


def chkConflict(listOfIndex):
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
    
# print(itemListOri[2])

    # TEST RESULT
    # testingIndex = 0
    # print(testingIndex>=0 & testingIndex%3!=0)
    # print(testingIndex)
    # print(testingIndex%3!=2 & testingIndex>=0)

# findGreatest3Num(itemListOri)
# findGreatestAdjancent(1)
# findGreatestAdjancent(2)
# findGreatestAdjancent(3)
# findGreatestAdjancent(4)

# findGreatestAdjancent(5)
# findGreatestAdjancent(6)
# findGreatestAdjancent(7)
# findGreatestAdjancent(8)
# findGreatestAdjancent(9)

# print(itemListOri.index(7))

# itemList.equals(itemListOri)
# print(set(itemList) == set(itemListOri))














# # Check the equality
# l1 = [10, 20, 30, 40, 50, 60] 
# l3 = [50, 10, 30, 20, 40] 
 
# a = set(l1)
# b = set(l3)
 
# if a == b:
#     print("Lists l1 and l3 are equal")
# else:
#     print("Lists l1 and l3 are not equal")