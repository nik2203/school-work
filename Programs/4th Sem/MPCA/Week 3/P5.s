@mul(add(a,b),c)
.data
a: .word 0
stk: .word 0

.text
LDR R0,=a
MOV R1,#10
MOV R2,#20
MOV R3,#30
BL mula
STR R6,[R0]
B end

mula:
    LDR R4,=stk
    STR LR,[R4]
    BL add
    MUL R6,R5,R3
    LDR LR,[R4]
    MOV PC,LR

add:
    ADD R5,R2,R1
    MOV PC,LR

end:
    SWI 0x011