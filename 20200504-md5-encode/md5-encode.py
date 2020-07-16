import hashlib
import sys

string = sys.argv[1]

hl = hashlib.md5()
hl.update(string.encode(encoding='utf-8'))

print(string)
print(hl.hexdigest())
