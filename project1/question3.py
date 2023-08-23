
n,m = str (input ()).split ()
n = int (n)
m = int (m)

k = n // m
r = n - (m * k)

if (r == 0):
    cuts = 0
else:
    cuts = 0
    remain = [m] * r
    t = r
    index = 0
    
    while (1 == 1):
        if (remain[index] > t):
            remain[index] = remain[index] - t
            t = 0
            cuts = cuts + 1
        elif (remain[index] == t):
            remain[index] = 0
            t = 0
        else:
            t = t - remain[index]
            remain[index] = 0
        
        if (remain[index] == 0 and t == 0):
            break
    
        if (remain[index] == 0):
            index = index + 1
        
        if (t == 0):
            t = r
        
    cuts = cuts * int (r / (index + 1))

print (cuts)