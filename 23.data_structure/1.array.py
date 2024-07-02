student_pet_count_list = [0,1,0,2,1,1,4,0,0,0,3,2,1,3,0,2,2,4]
NUM_OF_STUDENTS = len(student_pet_count_list)

ITEM_AT_INDEX_THREE = student_pet_count_list[3]
ITEM_THREE_FROM_BACK = student_pet_count_list[-3]

SUM = 0
for INDIVIDUAL_PET_COUNT in student_pet_count_list:
    SUM += INDIVIDUAL_PET_COUNT

AVERAGE = SUM / NUM_OF_STUDENTS
print(AVERAGE)

# Multidimensional Array
seating_chart = [
    ["Sarah", "Claire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

print(seating_chart[2][1])

for i, row in enumerate(seating_chart):
    for j, student_name in enumerate(row):
        print(f"{student_name} is in row {i+1}, seat{j+1}")