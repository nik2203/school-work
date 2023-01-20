.text
LDR R0, =a
CMP R0, #0
MOVLT R1, #3
CMP R0, #0
MOVGT R1, #2
CMP R0, #0
MOVEQ R1, #1

.data
a: .word 1
.end