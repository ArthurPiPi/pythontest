import zlib
import base64

message= "eJxLy0lMrzYxtEi2NExOtExLMTcyTDMwMzdLNDFJsjQ0TUk0NU41rgUA4UoLJg=="

a = base64.b64decode(message)

de = zlib.decompress(a)

print(de)