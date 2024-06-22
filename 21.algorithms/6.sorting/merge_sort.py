def mergeSort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2  # Calculate midpoint correctly

        leftArr = dataset[:mid]
        rightArr = dataset[mid:]

        # Recursively break down the arrays
        print("Current: ",dataset)
        mergeSort(leftArr)
        mergeSort(rightArr)

        i = 0  # index into the left array
        j = 0  # index into the right array
        k = 0  # index into the merged array

        # Merge the two halves
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                dataset[k] = leftArr[i]
                i += 1
            else:
                dataset[k] = rightArr[j]
                j += 1
            k += 1

        # If there are any elements left in the leftArr, add them
        while i < len(leftArr):
            dataset[k] = leftArr[i]
            i += 1
            k += 1

        # If there are any elements left in the rightArr, add them
        while j < len(rightArr):
            dataset[k] = rightArr[j]
            j += 1
            k += 1

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print("Original:", items)
mergeSort(items)
print("Sorted:", items)

# Original: [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
# Current:  [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
# Current:  [6, 20, 8, 19, 56]
# Current:  [6, 20]
# Current:  [8, 19, 56]
# Current:  [19, 56]
# Current:  [23, 87, 41, 49, 53]
# Current:  [23, 87]
# Current:  [41, 49, 53]
# Current:  [49, 53]
# Sorted: [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]