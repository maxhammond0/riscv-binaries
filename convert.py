import binascii

filename = 'malloc2'

ls = []
with open('textfiles/' + filename + '.txt', 'r') as f:
    for line in f:
        ls.append(binascii.unhexlify(line.strip()))

with open('examples/' + filename + '.mi', 'wb') as f:
    for line in ls:
        f.write(line)
