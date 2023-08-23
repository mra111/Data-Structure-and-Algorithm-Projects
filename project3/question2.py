import heapq

n,q,k = str (input ()).split ()

n = int (n)
q = int (q)
k = int (k)

heap = str (input ()).split ()
heap = list (map (int, heap))

numbers = []
result = []

heap.sort ()

if (k <= n):
    numbers = heap[:k - 1]
    heap = heap[k - 1:]
else:
    numbers = heap
    heap = []

heapq.heapify (heap)

heap_size = len (heap)
numbers_size = len (numbers)

while (q > 0):
    command = str (input ()).split ()

    if (command[0] == "print"):
        if (heap_size > 0):
            min_element = heap[0]

            result.append (min_element)
        else:
            result.append (-1)
    elif (command[0] == "+"):
        num = int (command[1])

        if (numbers_size < k - 1):
            numbers.append (num)
            numbers_size = numbers_size + 1
        elif (heap_size == 0 or num < heap[0]):
            numbers.append (num)
            max_num = max (numbers)
            numbers.remove (max_num)
            heapq.heappush (heap, max_num)
            heap_size = heap_size + 1
        else:
            heapq.heappush (heap, num)
            heap_size = heap_size + 1

    else:
        if (heap_size > 0):
            heapq.heappop (heap)

            heap_size = heap_size - 1

    q = q - 1

print (*result, sep="\n")