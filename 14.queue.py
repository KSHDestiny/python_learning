import queue
#! Queue is FIFO (first-in first-out)

q = queue.Queue()
print(q.empty())

q.put('bag1')
print(q.empty())

q.put('bag2')
q.put('bag3')

print(q.get())
print(q.get())
print(q.get())
#print(q.get())  #* stuck in waiting for another queue since it's empty
#* queue can be added using multiple threads or processes

#* queue can be defined maxsize
q = queue.Queue(maxsize=2)
print(q.empty())
q.put('bag1')
q.put('bag2')
print(q.full())
q.put('bag3', block=False)  #* if full, return with error   # q.put_nowait('bag3')
