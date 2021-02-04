counter = 0
itemsNumberAndRootStock = input().split()
itemsNumber, rootStock = itemsNumberAndRootStock[0], itemsNumberAndRootStock[1]
print(f'itemsNumber = {itemsNumber}')
print(f'rootStock = {rootStock}')

# bigItemDict = {}
# bigItemDict = [None]*5
bigItemDict = []


# addItemIntoList function
def addItemIntoList(itemList):
    # print(counter)
    print(itemList)

    
    singleItemL = {
        'parent'    : itemList[1], 
        'quantity'  : itemList[2],
    }
    bigItemDict.append(singleItemL)

    pointer = len(bigItemDict)-1
    # print(pointer)
    childPointer = bigItemDict[pointer]
    # print(childPointer)
    # print(childPointer['parent'])
    parentPointer = bigItemDict[int(childPointer['parent'])-1]
    # print(parentPointer)
    

            




        


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
print(f'bigItemDict= {bigItemDict[0]}')


for itemNumber in range(int(itemsNumber)):
    # addItemIntoList(input().split(), counter)
    # counter += 1
    
    # addItemIntoList(input().split())
    usrInp = input().split()
    print(usrInp)
    addItemIntoList(usrInp)