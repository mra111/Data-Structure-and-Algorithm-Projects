n = int (input ())
chars = []
counts = []
sorted_chars = []
while (n > 0):
    word = str (input ())
    char = word[0]
    if (char in chars):
        index = chars.index (char)
        counts[index] = counts[index] + 1
    else:
        chars.append (char)
        counts.append (1)
    n = n - 1
for i in range (len (chars)):
    if (counts[i] >= 5):
        sorted_chars.append (chars[i])
sorted_chars.sort ()
for i in range (len (sorted_chars)):
    print (sorted_chars[i], end="")
if (len (sorted_chars) == 0):
    print ("How long must I suffer")

