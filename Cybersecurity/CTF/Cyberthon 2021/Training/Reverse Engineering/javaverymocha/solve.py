data = [116, 104, 105, 115, 32, 105, 115, 32, 110, 111, 116, 32, 116, 104, 101, 32, 102, 108, 97, 103]

res = ""
for x in reversed(data):
    res += chr(x+1)
print(res)