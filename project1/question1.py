n,m = str (input ()).split ()
n = int (n)
m = int (m)
k = n
table = []
title = str (input ()).split (",")
while (k > 0):
    info = str (input ()).split (",")
    table.append (info)
    k = k - 1
sort = str (input ()).split ()[2]
index = title.index (sort)
table.sort (key=lambda x:x[index])
for i in range (n):
    for j in range (m):
        if (j < m - 1):
            print (table[i][j], end=",")
        else:
            print (table[i][j])


        
