# for-in loop
spices = [
    'salt',
    'pepper',
    'cumin',
    'turmeric'
]
for spice in spices:
    print(spice)
print('No more boring omelettes!')

# while
i = 5
print('Count to 100 by fives')
while i <= 100:
    print(i)
    i += 5
print('List complete!')


#! for-in loop with data mutation
sink = ['bowl', 'plate', 'cup']
print(f"\nThere are {len(sink)} dishes in the sink: {sink}\n")

#* for dish in sink:    // will not perform what we expect because of indexing
for dish in list(sink):     #* make a copy list of sink
    print(f" - Put a {dish} in the dishwasher")
    sink.remove(dish)

print(f"\nThere are {len(sink)} dishes in the sink: {sink}\n")

#! using break
import random

dishwasher = ['plate', 'bowl', 'cup', 'knife', 'fork', 'spoon', 'plate', 'spoon', 'bowl', 'cup', 'cup', 'fork', 'bowl', 'fork', 'plate', 'cup', 'spoon', 'knife']

for dish in list(dishwasher):
    if not random.randint(0, 19):
        print('Out of space!')
        break
    else:
        print(f"Putting {dish} in the cabinet")
        dishwasher.remove(dish)


#! while loop with randomly condition
dirty = True
scrub_count = 0

while dirty:
    scrub_count += 1
    print(f"Scrubbed the pan {scrub_count} times.")

    print("Rinsing to check if the pen is clean...\n")

    if not random.randint(0, 9):
        print("All clean!")
        dirty = False
    else:
        print("Still dirty...")