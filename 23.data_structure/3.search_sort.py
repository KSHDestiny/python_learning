# Linear Search

my_list = [8, 5, 0, 3, 9, 7]
ITEM = 7

def search(item, listy):
    for element in listy:
        if element == item:
            return True
    return False

print(search(ITEM, my_list))

# using index func is simple but make sure you need it since this search is a linear search
ITEM_INDEX = my_list.index(ITEM)


#! if we're going to search many different items, it might be worth sorting the list first in order to make each search faster.
# array
my_list = [1, 7, 3]
print(sorted(my_list, reverse=True))

# tuple
student_grades = [('Sarah', 89), ('Rebecca', 82), ('Matt', 91)]
print(sorted(student_grades))   # [('Matt', 91), ('Rebecca', 82), ('Sarah', 89)] // order by Name
print(sorted(student_grades, key=lambda x:x[1], reverse=True))  # [('Matt', 91), ('Sarah', 89), ('Rebecca', 82)] // descending order by Marks

# find second smallest item
# Timsort Algorithm (n log(n))
def find_second_smallest(my_list):
    if len(my_list) < 2:
        return None
    sorted_list = sorted(my_list)
    return sorted_list[1]

# only iterate once // better performance than first func
def find_second_smallest_v2(my_list):
    if len(my_list) < 2:
        return None
    smallest = float('inf')
    second_smallest = float('inf')
    for num in my_list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest

print(find_second_smallest([5, 8, 3, 2, 6]))
print(find_second_smallest_v2([5, 8, 3, 2, 6]))