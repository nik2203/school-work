.data
a: .word 1,2,3,4,5,6,7,8,9
b: .word 0

.text
LDR R0,=a
LDR R1,=b
MOV R2,#3
MOV R3,#3
MOV R4,#0
MOV R5,#0

fori:
forj:
    STMFD R13!, {R4,R5}
    BL get_add
    LDMFD R13!, {R4,R5,R6}
    ADD R7,R0,R6
    ADD R8,R1,R6
    LDR R6,[R7]
    STR R6,[R8]
    ADD R5,R5,#1
    CMP R5,R3
    BNE forj
    mov R5,#0
    ADD R4,R4,#1
    CMP R4,R2
    BEQ end
    B fori

get_add:
    LDMFD R13!, {R4,R5}
    MLA R7,R3,R4,R5
    MOV R8,#4
    MUL R6,R7,R8
    STMFD R13!,{R4,R5,R6}
BX lr

end:
SWI 0x011