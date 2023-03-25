@Write an ALP to implement C[i][j]=a[i][j]+b[i][j]

.data
a: .word 1,2,3,4,5,6,7,8,9
b: .word 9,8,7,6,5,4,3,2,1
c: .word 0,0,0,0,0,0,0,0,0

.text
LDR R0,=a 
LDR R1,=b
LDR R2,=c 
MOV R3,#3
MOV R4,#3
MOV R5,#0
MOV R6,#0
fori:
forj:
    STMFD R13!,{R5,R6}
    BL getadd
    LDMFD R13!,{R5,R6,R7}
    ADD R8,R0,R7
    ADD R9,R1,R7
    LDR R8,[R8]
    LDR R9,[R9]
    ADD R8,R8,R9
    ADD R9,R2,R7
    STR R8,[R9]
    ADD R6,R6,#1
    CMP R6,R4
    BNE forj
    MOV R6,#0
    ADD R5,R5,#1
    CMP R5,R3
    BEQ end
    B fori

getadd:
    LDMFD R13!,{R5,R6}
    MLA R8,R4,R5,R6
    MOV R9,#4
    MUL R7,R8,R9
    STMFD R13!,{R5,R6,R7}
BX LR

end:
SWI 0x011