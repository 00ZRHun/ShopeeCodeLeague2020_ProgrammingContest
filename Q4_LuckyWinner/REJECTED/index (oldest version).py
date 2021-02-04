def append3in1ContentIntoList(itemList3in1Split):
    itemList.append(int(itemList3in1Split[0]))
    itemList.append(int(itemList3in1Split[1]))
    itemList.append(int(itemList3in1Split[2]))
    # print(itemList3in1Split)

def find(number):
    index = itemListOri.index(number)
    fontIndex = index-1


    
# print(123)

# itemList = [2, 3, 4, 1, 5]
itemList = []

itemListRange = input('')
print(f'Item List Range: {itemListRange}')

# for i in range(0, 5):
for i in range(0, int(itemListRange)):
    # itemListContent = input('')
    # itemList.append(int(itemListContent))
    # itemList.append(int(input().split))
    itemList3in1 = input('')
    # print(itemList3in1)
    itemList3in1Split = itemList3in1.split()
    # print(itemList3in1Split)
    append3in1ContentIntoList(itemList3in1Split)




itemListOri = itemList.copy()
itemList.sort(reverse=True)

print(f'itemListOri: {itemListOri}')
print(f'itemList: {itemList}')



