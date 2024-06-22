# Stack
stack = []

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(stack)    # [1, 2, 3, 4]

x = stack.pop()
print(x)    # 4
print(stack)    # [1, 2, 3]


# Queue
    # using regular list like stack is inefficient since removing items from the front of a list requires a big O
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print(queue)    # deque([1, 2, 3, 4])

x = queue.popleft()
print(queue)    # deque([2, 3, 4])
y = queue.pop()
print(queue)    # deque([2, 3])