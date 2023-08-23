def find_path (node, v, vertices, dist, nodes1, nodes2):
    q = []
    visited_list = [0] * len (vertices)
    parents = [0] * len (vertices)
    status = 0
    next_node = -1
    q.append (node)

    visited_list[node - 1] = 1
    parents[node - 1] = 0

    dist[node - 1] = 0

    while (len (q) > 0):
        a = q.pop (0)
        
        for i in range (len (vertices[a - 1])):
            if ((parents[a - 1], a) in nodes1):
                index = nodes1.get ((parents[a - 1], a))
                next_node = nodes2.get (index)

            if (visited_list[vertices[a - 1][i] - 1] == 0 and vertices[a - 1][i] != next_node):
                
                visited_list[vertices[a - 1][i] - 1] = 1
                parents[vertices[a - 1][i] - 1] = a
                dist[vertices[a - 1][i] - 1] = dist[a - 1] + 1
                q.append (vertices[a - 1][i])
            
                if (vertices[a - 1][i] == v):
                    status = 1
                    break
        
        next_node = -1
        
        if (status == 1):
            break

n,m = str (input ()).split ()
n = int (n)
m = int (m)

vertices = [[]] * n

for i in range (m):
    a,b = str (input ()).split ()
    a = int (a)
    b = int (b)
    vertices[a - 1] = vertices[a - 1] + [b]
    vertices[b - 1] = vertices[b - 1] + [a]

u,v = str (input ()).split ()
u = int (u)
v = int (v)

q = int (input ())

nodes1 = {}
nodes2 = {}

for i in range (q):
    a,b,c = str (input ()).split ()
    a = int (a)
    b = int (b)
    c = int (c)

    nodes1.update ({(a, b): i + 1})
    nodes2.update ({i + 1: c})

visited_list = [0] * n
dist = [-1] * n

find_path (u, v, vertices, dist, nodes1, nodes2)

print (dist[v - 1])
