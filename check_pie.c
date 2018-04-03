unsigned long sp(void){ asm("mov %esp, %eax");}  
int main(int argc, char **argv)  
{  
    unsigned long esp = sp();  
    printf("Stack pointer (ESP : 0x%lx)\n",esp);  
    return 0;  
}  
