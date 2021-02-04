bigUsrQueryResultsL = []
testCase = input()

# for loop
for i in range(int(testCase)):

    itemNamesL, usrQueryResultsL = [], []

    numItemAndTotalQuery = input().split()
    numItem, totalQuery = numItemAndTotalQuery[0], numItemAndTotalQuery[1]
    # print(numItem, totalQuery)

    for i in range(int(numItem)):
        itemNamesL.append(f' {input()} ')
    
    for i in range(int(totalQuery)):
        count = 0
        usrQuery = f' {input().lower()} '

        # ### shorthand ### #
        for itemName in itemNamesL:
            if usrQuery in itemName:
                count += 1

        usrQueryResultsL.append(count)
    
    bigUsrQueryResultsL.append(usrQueryResultsL)

# for loop

# for usrQueryResultsL in bigUsrQueryResultsL:
for index, usrQueryResultsL in enumerate(bigUsrQueryResultsL):
    print(f'Case {(index+1)}: ')
    for usrQueryResult in usrQueryResultsL:
        print(usrQueryResult)

# debug
# print(itemNamesL)
# print(usrQueryResultsL)
# print(bigUsrQueryResultsL)
# print(itemNamesL, usrQueryResultsL, bigUsrQueryResultsL)  # Without newline