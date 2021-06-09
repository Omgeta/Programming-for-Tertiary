with open("encrypted.txt", "r") as f:
    encrypted = f.read()

for key in range(1, 0xff+1):
    decrypted = "".join([chr(key ^ ord(data)) for data in encrypted])
    if decrypted.isprintable():
        print(f"Key: {key} | Flag: {decrypted}")

