.text
LDR R0, =a
LDR R1, =b
LDR R4, =c
LDR R0,[R0]
LDR R1, [R1]
ADD R3,R0,R1
STR R3,[R4]

.data
a: .word 4
b: .word 16
c: .word 0
.end