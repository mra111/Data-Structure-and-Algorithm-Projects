n,m,q = str (input ()).split ()
n = int (n)
m = int (m)
q = int (q)

blacks = {}
row_counts = 0
column_counts = 0
results = []

while (q > 0):
    x,y = str (input ()).split ()
    x = int (x)
    y = int (y)

    if ((x, y) not in blacks):
        blacks.update ({(x, y): 1})

        if (((x - 1, y) in blacks) and ((x + 1, y) in blacks)):
            row_counts = row_counts - 1
        elif (((x - 1, y) not in blacks) and ((x + 1, y) not in blacks)):
            row_counts = row_counts + 1
    
        if (((x, y - 1) in blacks) and ((x, y + 1) in blacks)):
            column_counts = column_counts - 1
        elif (((x, y - 1) not in blacks) and ((x, y + 1) not in blacks)):
            column_counts = column_counts + 1
    
    results.append (row_counts + column_counts)

    q = q - 1

print (*results, sep="\n")
