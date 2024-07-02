from collections import deque

printer_queue = deque()
printer_queue.append("TaylorSwiftTickets.pdf")
printer_queue.append("MarketingNotes.docx")
printer_queue.append("Proof.png")

while len(printer_queue) > 0:
    document = printer_queue.popleft()
    print(f'Printing {document}')
    # Printing TaylorSwiftTickets.pdf
    # Printing MarketingNotes.docx
    # Printing Proof.png 

print(printer_queue)    # deque([])

# Linear Time Complexity, Linear Space Complexity O(n)
def print_binary_numbers(n):
    if n <= 0:
        return
    
    queue = deque()
    queue.append(1)

    for i in range(n):
        binary = queue.popleft()
        print(binary)
        queue.append(binary * 10)
        queue.append(binary * 10 + 1)

print_binary_numbers(6)
print()
print_binary_numbers(-9)
print()
print_binary_numbers(0)
print()
print_binary_numbers(2)
print()
print_binary_numbers(10)