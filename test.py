from pwn import *

vb = ELF('vr')

p = process('./vr')
p.interactive()

