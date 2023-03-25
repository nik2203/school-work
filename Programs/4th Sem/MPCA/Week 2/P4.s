.data
a: .word -4
b: .word 9

.text
LDR R0, =a
LDR R0, [R0]
LDR R1, =b
LDR R1, [R1]
MOV R2, #0
MOV R3, #0

l:
    CMP R0, #0
    BEQ end
    TST R0, #1
    BEQ l1
    ADD R3, R3, R1, LSL R2

l1:
    MOV R0, R0, LSR #1
    ADD R2, R2, #1
    B l

end:
SWI 0x011