@Factorial
.data
a: .word 0

.text
LDR R0,=a
MOV R1,#10
BL fact
STR R2,[R0]
B end

fact:
    MOV R2,#1

l:
    MUL R2,R2,R1
    SUB R1,R1,#1
    CMP R1,#0
    BGT l
    MOV PC,LR

end:
    SWI 0x011