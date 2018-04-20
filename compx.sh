#/bin/bash
gcc -fno-stack-protector -z execstack -no-pie $1 -o $2
