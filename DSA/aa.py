from queue import Queue

def qinfo(q):
    print("elements:",q.queue)
    print("size:",q.qsize())
    print("empty:",q.empty())
    print("full:",q.full())
    print()
    return

q=Queue(maxsize=5)
print(type(q))
qinfo(q)

q.put(11)
qinfo(q)

q.put(33);q.put(55)
q.put(77);q.put(99)
qinfo(q)

print("Deleted element: ",q.get())
qinfo(q)

q.get()
print("Deleted element: ",q.get())
q.get()
qinfo(q)

print("Deleted element: ",q.get())
qinfo(q)

del q

'''
output:

<class 'queue.Queue'>
elements: deque([])
size: 0
empty: True
full: False

elements: deque([11])
size: 1
empty: False
full: False

elements: deque([11, 33, 55, 77, 99])
size: 5
empty: False
full: True

Deleted element:  11
elements: deque([33, 55, 77, 99])
size: 4
empty: False
full: False

Deleted element:  55
elements: deque([99])
size: 1
empty: False
full: False

Deleted element:  99
elements: deque([])
size: 0
empty: True
full: False

'''
