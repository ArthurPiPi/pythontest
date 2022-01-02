
import base64
print(base64.b64decode(''))
encode = 'eJxLy0lMrzYxtEi2NExOtExLMTcyTDMwMzdLNDFJsjQ0TUk0NU41rgUA4UoLJg=='

for j in range(1,26):
    decode = ''
    for i in encode:
        if(i>='a' and i<='z'):
            if(ord(i)+j>122):
                i = chr(ord(i)+j-26)
            else:
                i = chr(ord(i)+j)
        elif(i>='A' and i<='Z'):
            if(ord(i)+j>90):
                i = chr(ord(i)+j-26)
            else:
                i = chr(ord(i)+j)
        elif(i>='0' and i<='9'):
            if(ord(i)+j>57):
                i = chr((ord(i)+j) % 10 + 48)
            else:
                i = chr(ord(i)+j)
        decode += i
    print("移位数%d：%s" % (j,decode))
