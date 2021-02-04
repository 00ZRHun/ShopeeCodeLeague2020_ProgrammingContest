import math
from pprint import pprint

counter = 0
itemsNumberAndRootStock = input().split()
itemsNumber, rootStock = itemsNumberAndRootStock[0], itemsNumberAndRootStock[1]
# print(f'itemsNumber = {itemsNumber}')
# print(f'rootStock = {rootStock}')

# bigItemDict = {}
# bigItemDict = [None]*5
bigItemDict = []

def moveDownRefresh(parentPointer):
    childPointer = bigItemDict[int(parentPointer['child'])-1]

    # ### if child array non-empty  ### #
    childPointer['stock'] = math.floor(int(parentPointer['stock']) / int(childPointer['quantity']))

def moveUpRefresh(parentPointer):
    while True:
        childPointer = parentPointer
        parentPointer = bigItemDict[int(childPointer['parent'])-1]

        # ### if child array non-empty  ### #
        parentPointer['stock'] = int(childPointer['quantity']) * int(childPointer['stock'])
        
        if  parentPointer['parent'] == None:
            break

# addItemIntoList function
def addItemIntoList(itemList):
    
    singleItemL = {
        'parent'    : itemList[1], 
        'quantity'  : itemList[2]
    }
    bigItemDict.append(singleItemL)

    pointer = len(bigItemDict)-1
    childPointer = bigItemDict[pointer]
    parentPointer = bigItemDict[int(childPointer['parent'])-1]

    if len(itemList) == 3:
        # ### conside the dynamic child ### #
        bigItemDict[int(itemList[1])-1]['child'] = len(bigItemDict)

        childPointer['type']    = 'dynamic'
        childPointer['stock']   =  math.floor(int(parentPointer['stock']) / int(childPointer['quantity']))

        # while parentPointer['parent'] != None:
        #     childPointer = bigItemDict[counter]
        #     parentPointer = bigItemDict[childPointer['parent']]

    else:

        # print(-1)
        childPointer['type'] = 'fixed'
        childPointer['stock'] = itemList[3]
        
        # print(0)

        childTotalStock = int(childPointer['quantity']) * int(childPointer['stock'])
        # parentPointer['stock'] -= childTotalStock
        parentPointer['stock'] = int(parentPointer['stock']) - int(childTotalStock)
        
        if parentPointer['parent'] == None:
            moveDownRefresh(parentPointer)
        else:
            moveUpRefresh(parentPointer)

        

    # print(f'bigItemDict: {bigItemDict}')
    # pprint(bigItemDict)

# addItemIntoList function


# root
singleItemL = {
    'parent' : None, 
    'type'   : 'fixed', 
    'stock'  : rootStock
}
bigItemDict.append(singleItemL)


for itemNumber in range(int(itemsNumber)-1):
    # usrInp = input().split()
    # print(usrInp)
    # addItemIntoList(usrInp)
    addItemIntoList(input().split())


for itemDict in bigItemDict:
    print(itemDict['stock'])