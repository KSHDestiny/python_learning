# O(n)
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_item(item, itemlist):
    for i in range(0, len(itemlist)):
        print("loop:",i+1)
        if item == itemlist[i]:
            return i
    return None

print(find_item(87, items)) # 6
# loop: 1
# loop: 2
# loop: 3
# loop: 4
# loop: 5
# loop: 6
# loop: 7
# 6

print(find_item(250, items))    # None
# loop: 1
# loop: 2
# loop: 3
# loop: 4
# loop: 5
# loop: 6
# loop: 7
# loop: 8
# loop: 9
# loop: 10
# None