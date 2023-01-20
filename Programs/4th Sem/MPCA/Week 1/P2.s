.text
LDR R0, =a
LDR R1, =b
CMP R0,R1
ADDEQ R2, R0, R1
SUBNE R2, R0, R1

.data
a: .word 20
b: .word 40
.end