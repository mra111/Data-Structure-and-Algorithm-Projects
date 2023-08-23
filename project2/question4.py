def get_inputs (chars):
    a = str (input ()).split ()
    if (a[0] == "push"):
        chars.append (a[1])
    else:
        chars.remove (chars[0])

def find_p (chars):
    count = 0
    strings = []

    for i in range (len (chars)):
        for j in range (i + 1):
            chars2 = chars[j:i + 1]
            chars2.reverse ()
            if (chars[j:i + 1] == chars2 and chars2 not in strings):
                strings.append (chars2)
                count = count + 1
    
    return count

n = int (input ())

chars = []
counts = []

for i in range (n):
    get_inputs (chars)
    counts.append (find_p (chars))

for i in counts:
    print (i)
