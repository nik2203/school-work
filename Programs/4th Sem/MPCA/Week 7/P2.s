.data  

str: .asciz "NIKHIL G" 
del: .word 30000

.text

mov r0 , #31 
mov r1 , #7  
ldr r2 , =str

START:

swi 0x204  
bl DELAY
swi 0x206
cmp r0,#0
subne r0,r0,#1
swieq 0x11  
b START

DELAY:

ldr r9,=del
ldr r9,[r9]

LOOP:

cmp r9,#0
moveq pc,lr

sub r9,r9,#1
b LOOP

.end