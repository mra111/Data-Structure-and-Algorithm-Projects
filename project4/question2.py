def bfs (char1, char2, vertices):
    q = []
    visited_list = [0] * len (vertices)
    q.append (char1)

    visited_list[char1 - 1] = 1

    while (len (q) > 0):
        v = q.pop (0)

        for i in range (len (vertices[v - 1])):
            if (char2 == vertices[v - 1][i]):
                return True
            
            if (visited_list[vertices[v - 1][i] - 1] == 0):
                visited_list[vertices[v - 1][i] - 1] = 1
                q.append (vertices[v - 1][i])
    
    return False

s = str (input ())
t = str (input ())

size = len (s)

chars = {}
num = 1
count = 0

for i in range (size):
    if (s[i] != t[i]):
        if (s[i] not in chars):
            chars.update ({s[i]: num})
            num = num + 1
        
        if (t[i] not in chars):
            chars.update ({t[i]: num})
            num = num + 1

n = num - 1

vertices = [[]] * n

for i in range (size):
    if (s[i] != t[i]):
        n1 = chars[s[i]]
        n2 = chars[t[i]]

        if (bfs (n1, n2, vertices) == False):
            vertices[n1 - 1] = vertices[n1 - 1] + [n2]
            vertices[n2 - 1] = vertices[n2 - 1] + [n1]
            count = count + 1

print (count)
