counter = 0
itemsNumberAndRootStock = input().split()
itemsNumber, rootStock = itemsNumberAndRootStock[0], itemsNumberAndRootStock[1]
print(f'itemsNumber = {itemsNumber}')
print(f'rootStock = {rootStock}')

# bigItemDict = {}
# bigItemDict = [None]*5
bigItemDict = []



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
print(f'bigItemDict= {bigItemDict[0]}')


for itemNumber in range(int(itemsNumber)):
    # addItemIntoList(input().split(), counter)
    # counter += 1
    addItemIntoList(input().split())



def addItemIntoList(itemList):
    # print(counter)
    if len(itemList) == 3:
        # bigItemDict[counter]['type'] = 'dynamic'
        # bigItemDict[counter]['parent'] = itemList[1]
        # bigItemDict[counter]['quantity'] = itemList[2]
        # bigItemDict[counter]['stock'] = bigItemDict[counter-1]['stock']/bigItemDict[counter]['quantity']

        # while parentPointer['parent'] != None:
        #     childPointer = bigItemDict[counter]
        #     parentPointer = bigItemDict[childPointer['parent']]


    else:
        bigItemDict[counter]['type'] = 'fixed'
        bigItemDict[counter]['parent'] = itemList[1]
        bigItemDict[counter]['quantity'] = itemList[2]
        bigItemDict[counter]['stock'] = itemList[3]
        
        childPointer = bigItemDict[counter]
        parentPointer = bigItemDict[childPointer['parent']]
        childTotalStock = childPointer['quantity'] * childPointer['stock']

        parentPointer['quantity'] -= childTotalStock
        
        while parentPointer['parent'] != None:
            if parentPointer['type'] == 'dynamic':
                childPointer = parentPointer
                parentPointer = bigItemDict[childPointer['parent']]
                childTotalStock = childPointer['quantity'] * childPointer['stock']

                parentPointer['stock'] = childTotalStock

            # if bigItemDict[bigItemDict[counter]['parent']]['type'] == 'fixed':
                # bigItemDict[bigItemDict[counter]['parent']]['quantity']  (bigItemDict[bigItemDict[counter]['parent']]['quantity']*bigItemDict[bigItemDict[counter]['parent']]['stock'])

    print(f'bigItemDict: {bigItemDict}')

            




        


    #     counter += 1
