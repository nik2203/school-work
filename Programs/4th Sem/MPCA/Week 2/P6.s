.data
a: .word 7

.text
LDR R0,=a
LDR R0, [R0]
MOV R1,#1
l:
    MUL R1,R0,R1
    SUBS R0,R0,#1
    BNE l

SWI 0x011