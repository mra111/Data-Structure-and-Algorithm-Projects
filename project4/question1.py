def bfs (node, vertices, results):
    q = []
    visited_list = [0] * len (vertices)
    q.append (node)

    visited_list[node - 1] = 1

    while (len (q) > 0):
        v = q.pop (0)
        results[0] = results[0] + 1
        results.append (v)

        for i in range (len (vertices[v - 1])):
            if (visited_list[vertices[v - 1][i] - 1] == 0):
                visited_list[vertices[v - 1][i] - 1] = 1
                q.append (vertices[v - 1][i])

def dfs (node, vertices, visited_list, results):
    visited_list[node - 1] = 1
    results[0] = results[0] + 1
    results.append (node)

    for i in range (len (vertices[node - 1])):
        if (visited_list[vertices[node - 1][i] - 1] == 0):
            dfs (vertices[node - 1][i], vertices, visited_list, results)

n,m = str (input ()).split ()
n = int (n)
m = int (m)

vertices = [[]] * n

results = [0]

for i in range (m):
    v,u = str (input ()).split ()
    v = int (v)
    u = int (u)
    vertices[v - 1] = vertices[v - 1] + [u]
    vertices[u - 1] = vertices[u - 1] + [v]

q = int (input ())

for i in range (len (vertices)):
    vertices[i].sort ()

while (q > 0):
    commands = str (input ()).split ()

    if (commands[0] == "1" and commands[1] == "BFS"):
        v = int (commands[2])

        results = [0]
        bfs (v, vertices, results)

        print (results[0])
    elif (commands[0] == "1" and commands[1] == "DFS"):
        v = int (commands[2])

        results = [0]
        visited_list = [0] * n
        dfs (v, vertices, visited_list, results)

        print (results[0])
    else:
        num = int (commands[1])

        if (num > len (results) - 1 or results[0] == 0):
            print (-1)
        else:
            print (results[num])
    
    q = q - 1
