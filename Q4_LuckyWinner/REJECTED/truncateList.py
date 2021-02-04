letters = ["x", "y", "z", "a", "b"]
# print(letters)

# Resize list to two elements at the start.
letters = letters[:2]
# print(letters)

# itemListOri = [1, 3, 2, 5, 4, 6, 8, 9, 7]
itemList    = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def findGreatest3Num(itemListOri):
    itemListOri = itemList.copy()
    itemList.sort(reverse=True)
    shortItemList = itemList[:3]

    print(itemList)
    print(shortItemList)

findGreatest3Num(itemList)