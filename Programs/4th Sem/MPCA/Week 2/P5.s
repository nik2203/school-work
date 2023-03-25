.data
a: .word 2
b: .word 3
c: .word 4
d: .word 0
e: .word 0

.text
LDR R0, =a
LDR R1, =b
LDR R2, =c
LDR R3, =d
LDR R4, =e

LDR R0, [R0]
LDR R1, [R1]
LDR R5, [R2]

TEQ R0, R1
BEQ l
TEQ R1, R5
BEQ l1

MUL R6, R0, R1
STR R6, [R4]
B end

l:
    ADD R6, R0, R1
    STR R6, [R2]
    B end
l1:
    SUB R6, R0, R1
    STR R6, [R3]
    B end

end:
SWI 0x011