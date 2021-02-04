from __future__ import division     # Note that this division must be at the very beginning of the file
import math

totalCostForServerL = []
testCaseNumber = input()

# for loop
for testCase in range(int(testCaseNumber)):
    serverPriceL = []

    serversNumListAndWantedServersNum = input().split()
    serversNumList, wantedServersNum = serversNumListAndWantedServersNum[0], serversNumListAndWantedServersNum[1]
    # print(f'serversNumList: {serversNumList}')
    # print(f'wantedServersNum: {wantedServersNum}')
    
    serverPrices = input().split()
    for serverPrice in serverPrices:
        serverPriceL.append(int(serverPrice))
    serverPriceL.sort()
    # print(f'serverPriceL: {serverPriceL}')

    # neededServersNum
    # wantedServersNum
    # if int(wantedServersNum)%2==1:
    #     wantedServersNum+1
    
    # shorthand -> can omit this line
    neededServersNum = math.ceil(int(wantedServersNum)/2)
    # print(neededServersNum)
    neededServersNumL = serverPriceL[:neededServersNum]
    # print(neededServersNumL)
    totalCostForServer = sum(neededServersNumL)
    # print(totalCostForServer)
    totalCostForServerL.append(totalCostForServer)

    # for i in neededServersNumL:
    #     serverPriceL
    
    ''' 
    # if odd    -> even/2
    # if even   -> /2


    +------------------+-----------------+
    | wantedServersNum | neededServersNum |
    +------------------+-----------------+
    |       1          |       1         |
    +------------------+-----------------+
    |       2          |       1         |
    +------------------+-----------------+
    |       3          |       2         |
    +------------------+-----------------+
    |       4          |       2         |
    +------------------+-----------------+
    |       5          |       3         |
    +------------------+-----------------+
    |       6          |       3         |
    +------------------+-----------------+
    |       7          |       5         |
    +------------------+-----------------+ 
    '''
# for loop



for index, totalCostForServer in enumerate(totalCostForServerL):
    print(f'Case {index+1}: {totalCostForServer}')