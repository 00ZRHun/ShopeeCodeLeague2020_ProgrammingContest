import math

counter = 0
itemsNumberAndRootStock = input().split()
itemsNumber, rootStock = itemsNumberAndRootStock[0], itemsNumberAndRootStock[1]
# print(f'itemsNumber = {itemsNumber}')
# print(f'rootStock = {rootStock}')

# bigItemDict = {}
# bigItemDict = [None]*5
bigItemDict = []


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
        
        childPointer['type']    = 'dynamic'
        childPointer['stock']   =  math.floor(int(parentPointer['stock']) / int(childPointer['quantity']))

        # while parentPointer['parent'] != None:
        #     childPointer = bigItemDict[counter]
        #     parentPointer = bigItemDict[childPointer['parent']]

    else:

        childPointer['type'] = 'fixed'
        childPointer['stock'] = itemList[3]

        childTotalStock = int(childPointer['quantity']) * int(childPointer['stock'])
        # parentPointer['stock'] -= childTotalStock
        parentPointer['stock'] = int(parentPointer['stock']) - int(childTotalStock)
        
        while parentPointer['parent'] != None:
            if parentPointer['type'] == 'dynamic':
                childPointer = parentPointer
                # parentPointer = bigItemDict[childPointer['parent']]
                parentPointer = bigItemDict[int(childPointer['parent'])]

                childTotalStock = int(childPointer['quantity']) * int(childPointer['stock'])
                parentPointer['stock'] = childTotalStock

            # if bigItemDict[bigItemDict[counter]['parent']]['type'] == 'fixed':
                # bigItemDict[bigItemDict[counter]['parent']]['quantity']  (bigItemDict[bigItemDict[counter]['parent']]['quantity']*bigItemDict[bigItemDict[counter]['parent']]['stock'])

            




        


    print(f'bigItemDict: {bigItemDict}')
    #     counter += 1


# addItemIntoList function

# root
singleItemL = {
    'parent' : None, 
    'type'   : 'fixed', 
    'stock'  : rootStock
}
bigItemDict.append(singleItemL)
# abc[counter]['parent'] = None
# abc[counter]['type'] = 'fixed'
# abc[counter]['stock'] = rootStock
# counter += 1
# print(f'bigItemDict= {bigItemDict[0]}')


for itemNumber in range(int(itemsNumber)):
    # addItemIntoList(input().split(), counter)
    # counter += 1
    
    # usrInp = input().split()
    # print(usrInp)
    # addItemIntoList(usrInp)
    addItemIntoList(input().split())


for itemDict in bigItemDict:
    print(itemDict['stock'])