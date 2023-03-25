.data
a: .word 19

.text
LDR R0, =a
LDR R0, [R0]
MVN R1, R0
ADD R2,R1,#1

SWI 0x011