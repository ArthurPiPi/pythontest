flag = "qghx"
flaglist = []
for i in flag:
    flaglist.append(ord(i) - 97)
flags = ""
for i in flaglist:
    for j in range(0, 26):
        c = (7 * j + 7) % 26
        if (c == i):
            flags += chr(j + 97)
print(flags)
