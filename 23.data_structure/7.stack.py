card_stack = []

card_stack.append("Jack of Hearts")
card_stack.append("2 of Diamonds")
card_stack.append("10 of Spades")

#! shouldn't use direct index, remove things from the middle of the stack although we could do technically but while act as a stack
top_card = card_stack.pop()
print(top_card) # 10 of Spades
top_card = card_stack[-1]
print(top_card) # 2 of Diamonds

if not card_stack:
    print("Card stack is empty")
else:
    print(len(card_stack))


# using deque as a stack since deque is Double-ended queue
from collections import deque

history_stack = deque()
history_stack.append("https://google.com")
history_stack.append("https://linkedin.com")
history_stack.append("https://stackoverflow.com")

print(history_stack[-1])    # https://stackoverflow.com
print(history_stack.pop())  # https://stackoverflow.com
print(history_stack)    # deque(['https://google.com', 'https://linkedin.com'])


def check_matching_parentheses(s):
    stack = deque()
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

print(check_matching_parentheses("()"))
print(check_matching_parentheses("(hi there)"))
print(check_matching_parentheses("(hell)o"))
print(check_matching_parentheses("((linkedin)) learning"))

print(check_matching_parentheses("(hi(there"))
print(check_matching_parentheses("()ok)"))
print(check_matching_parentheses("((increment)"))
print(check_matching_parentheses(")linkedin()"))
