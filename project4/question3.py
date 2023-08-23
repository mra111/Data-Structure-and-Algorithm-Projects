import sys

sys.setrecursionlimit (15000)

def find_cycle (node, last_node, vertices, visited_list, cycle, results):
    visited_list[node - 1] = 1

    for i in vertices[node - 1]:
        if (visited_list[i - 1] == 0):
            find_cycle (i, node, vertices, visited_list, cycle, results)
        elif (i != last_node):
            cycle[i - 1] = 1
            cycle[node - 1] = 1
            results[0] = i
            return
        
        if (results[0] != -1 and results[1] == 0):
            if (node == results[0]):
                results[1] = 1
                return
            else:
                cycle[node - 1] = 1
                return
        elif (results[0] != -1):
            return

def find_path (node, count, vertices, visited_list, cycle, dist):
    visited_list[node - 1] = 1

    if (cycle[node - 1] == 1):
        dist[0] = count

    for i in vertices[node - 1]:
        if (dist[0] != -1):
            break

        if (visited_list[i - 1] == 0):
            find_path (i, count + 1, vertices, visited_list, cycle, dist)

n = int (input ())

vertices = [[]] * n

for i in range (n):
    v,u = str (input ()).split ()
    v = int (v)
    u = int (u)
    vertices[v - 1] = vertices[v - 1] + [u]
    vertices[u - 1] = vertices[u - 1] + [v]

visited_list = [0] * n
cycle = [0] * n
results = [-1, 0]

find_cycle (1, -1, vertices, visited_list, cycle, results)

for i in range (n):
    visited_list = [0] * n
    dist = [-1]
    find_path (i + 1, 0, vertices, visited_list, cycle, dist)
    print (dist[0], end=" ")
