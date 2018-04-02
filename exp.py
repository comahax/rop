from pwn import *

vb = ELF('vb')
libc = ELF('libc.so.6')

print 'strcpy plt=' + hex(vb.plt['strcpy'])
print 'strcpy got=' + hex(vb.got['strcpy'])
print 'system plt=' + hex(libc.got['system'])
