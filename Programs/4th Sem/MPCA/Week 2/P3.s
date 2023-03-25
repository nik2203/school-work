.data
a: .byte 1,2,3,4,5,6,7,8,9,10
b: .byte 0

.text
LDR R0,=a
LDR R1,=b
MOV R4,#0
MOV R5,#0

l:
LDRB R2,[R0]
LDRB R3,[R1]
ADD R4,R2,R3
STRB R4,[R1]
ADD R0,R0,#1
ADD R5,R5,#1
CMP R5, #10
BNE l

SWI 0x011