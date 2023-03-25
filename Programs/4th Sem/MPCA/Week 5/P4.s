@Write an ALP to implement c[k] = a[i] * b[j]

.data
a: .word 1,2,3,4,5
b: .word 6,7,8,9,0
c: .word 0,0,0,0,0

.text
LDR R0,=a
LDR R1,=b 
LDR R2,=c 
MOV R6,#5
l:
    LDR R3,[R0],#4
    LDR R4,[R1],#4
    MUL R5,R3,R4
    STR R5,[R2],#4
    SUB R6,R6,#1
    CMP R6,#0
    BNE l
SWI 0x011