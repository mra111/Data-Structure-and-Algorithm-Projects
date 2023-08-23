import heapq

n,t = str (input ()).split ()

n = int (n)
t = int (t)

times = str (input ()).split ()

times = list (map (int, times))

status = 0
heap = []
queue = []
queue2 = []
results = [0] * n

for i in range (len (times)):
    heap.append ((times[i], i + 1))

heapq.heapify (heap)

time = heap[0][0]

while (len (heap) > 0 or len (queue) > 0 or len (queue2) > 0):    
    if (len (queue) > 0):
        status = 1
    
    while (len (heap) > 0 and heap[0][0] <= time):
        element = heapq.heappop (heap)[1]
        
        if ((len (queue) > 0 and queue[len (queue) - 1] < element) or (len (queue2) > 0 and queue2[0] < element)):
            heapq.heappush (queue2, element)
        else:
            queue.append (element)
    
    if (status == 1):
        element = queue.pop (0)
        results[element - 1] = time
        status = 0
    
    if (len (queue) == 0 and len (queue2) > 0):
        element = heapq.heappop (queue2)
        queue.append (element)
    
    if (len (queue) > 0):
        time = time + t
    elif (len (heap) > 0):
        time = heap[0][0]

print (*results)
