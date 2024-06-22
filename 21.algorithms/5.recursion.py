def countdown(x):
    if x == 0:
        print("Done!")
        return
    else:
        print(x, "...")
        countdown(x-1)
        print("hey!", x)

countdown(5)


# ToDo: 2^4 = 2*2*2*2 = 16
def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return (num * power(num, pwr-1))

# ToDo: 5! = 5*4*3*2*1 (Special Case - 0! is 1 according to Math)
def factorial(num):
    if num == 0:
        return 1
    else:
        return (num * factorial(num-1))

print(f"5 to the power of 3 is {power(5, 3)}")  # 5 to the power of 3 is 125
print(f"2 to the power of 4 is {power(2, 4)}")  # 2 to the power of 4 is 16
print(f"4! is {factorial(4)}")  # 4! is 24
print(f"0! is {factorial(0)}")  # 0! is 1