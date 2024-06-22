item1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
item2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def is_sorted(itemList):
    # ToDo: using the brute force method
    # for i in range(0, len(itemList) - 1):
    #     if (itemList[i] > itemList[i+1]):
    #         return False
    # return True

    return all(itemList[i] <= itemList[i+1] for i in range(len(itemList) - 1))


print(is_sorted(item1))
print(is_sorted(item2))