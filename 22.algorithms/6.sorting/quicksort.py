items = [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]

def quickSort(dataset, first, last):
    if first < last:
        # calculate the split point
        pivotIdx = partition(dataset, first, last)

        # sort the two partitions
        print("Current: ", dataset)
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)

def partition(dataValues, first, last):
    # ToDo: choose the first item as the pivot value
    pivitValue = dataValues[first]

    # ToDo: establish the upper and lower indexes
    lower = first+1
    upper = last

    # start searching for the crossing point
    done = False
    while not done:
        # ToDo: advance the lower index
        while lower <= upper and dataValues[lower] <= pivitValue:
            lower = lower+1

        # ToDo: advance the upper index
        while dataValues[upper] >= pivitValue and upper >= lower:
            upper = upper - 1

        # ToDo: if the two indexes cross, we have found the split point
        if upper < lower:
            done = True
        else:
            temp = dataValues[lower]
            dataValues[lower] = dataValues[upper]
            dataValues[upper] = temp
    
    # ToDo: when the split point is found, exchange the pivot value
    temp = dataValues[first]
    dataValues[first] = dataValues[upper]
    dataValues[upper] = temp

    # ToDo: return the split point index
    return upper

print(items)
quickSort(items, 0, len(items)-1)
print(items)

# [20, 6, 8, 53, 56, 23, 87, 41, 49, 19]
# Current:  [19, 6, 8, 20, 56, 23, 87, 41, 49, 53]
# Current:  [8, 6, 19, 20, 56, 23, 87, 41, 49, 53]
# Current:  [6, 8, 19, 20, 56, 23, 87, 41, 49, 53]
# Current:  [6, 8, 19, 20, 49, 23, 53, 41, 56, 87]
# Current:  [6, 8, 19, 20, 41, 23, 49, 53, 56, 87]
# Current:  [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
# [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]