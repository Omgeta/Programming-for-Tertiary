# unxor
## Description
This file has been encrypted with single byte XOR cipher. Can you decrypt it? The decrypted data should be ASCII printable.

## Analysis
Since the cipher key is only 1 byte long, it only has a range from 0x00-0xff. Thus, the cipher can be cracked via bruteforce.

## Solution
```py
with open("encrypted.txt", "r") as f:
    encrypted = f.read()

for key in range(1, 0xff+1):
    decrypted = "".join([chr(key ^ ord(data)) for data in encrypted])
    if decrypted.isprintable():
        print(f"Key: {key} | Flag: {decrypted}")
```

```txt
...
Key: 158 | Flag: Hey it seems like you've successfully decrypted me! The flag is CTFSG{h3y_s33m5_l1k3_x0r_c4n_b3_r3v3r53d}
...
```

There's the flag:
```txt
CTFSG{h3y_s33m5_l1k3_x0r_c4n_b3_r3v3r53d}
```