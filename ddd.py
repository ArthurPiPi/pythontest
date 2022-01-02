a = 'h1oh0v54vh9jqc0c473v7hhvc8881'  # 密文
a1 = []
for i in a:
    a2 = ord(i) - 97
    a1.append(a2)
aa = ''
for i in a1:
    for j in range(0, 26):
        c = (7 * j + 7) % 26  # 仿射加密公式，自行更改
        if (c == i):
            aa += chr(j + 97)
print(aa)

