fin = open('./test.md')

line = fin.readline()

tmp = ''

while line:
    tmp = tmp[0:len(tmp) - 1] + '\\n' + line
    line = fin.readline()

print(tmp)