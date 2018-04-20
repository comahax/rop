from pwn import *

p = process('./hw')
gdb.attach(p, '''
b main
c
''')
