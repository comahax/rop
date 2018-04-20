from pwn import *

#vr = process(['./vr',])

#gdb.attach(vr,'''b main''')
#io = gdb.debug(exe='./vr', gdbscript='''
#b main
#continue''')

io = gdb.debug('./vr', '''
break main
continue
''')
io.interactive()
#io.wait_for_close()
