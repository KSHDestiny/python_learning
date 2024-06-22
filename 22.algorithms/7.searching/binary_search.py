items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarySearch(item, itemList):
    # get the list size
    listSize = len(itemList) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listSize

    while lowerIdx <= upperIdx:
        # ToDo: calculate the middle point
        midPt = (lowerIdx + upperIdx) // 2
        print("Lower item:",itemList[lowerIdx])
        print("Mid item:",itemList[midPt])
        print("Upper item:",itemList[upperIdx])
        print("one loop is ended. __________")

        # ToDo: if item is found, return the index
        if itemList[midPt] == item:
            return midPt

        # ToDo: otherwise get the next midpoint
        if item > itemList[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1

    if lowerIdx > upperIdx:
        return None
    

print(binarySearch(23, items))
# Lower item: 6
# Mid item: 23
# Upper item: 87
# one loop is ended. __________
# 4

print(binarySearch(87, items))
# Lower item: 6
# Mid item: 23
# Upper item: 87
# one loop is ended. __________
# Lower item: 41
# Mid item: 53
# Upper item: 87
# one loop is ended. __________
# Lower item: 56
# Mid item: 56
# Upper item: 87
# one loop is ended. __________
# Lower item: 87
# Mid item: 87
# Upper item: 87
# one loop is ended. __________
# 9

print(binarySearch(21, items))
# Lower item: 6
# Mid item: 23
# Upper item: 87
# one loop is ended. __________
# Lower item: 6
# Mid item: 8
# Upper item: 20
# one loop is ended. __________
# Lower item: 19
# Mid item: 19
# Upper item: 20
# one loop is ended. __________
# Lower item: 20
# Mid item: 20
# Upper item: 20
# one loop is ended. __________
# None