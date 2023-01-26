.text
LDR R0, =a
LDR R1, =b
LDR R0,[R0]
LDR R1,[R1]
CMP R0,R1
ADDEQ R2,R1,R0
SUBNE R2,R1,R0

.data
a: .word 20
b: .word 10
.end