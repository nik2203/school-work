.data
a: .byte 1,2,3,4,5,6,7,8,9,10
b: .byte 0,0,0,0,0,0,0,0,0,0


.text
LDR R0,=a
LDR R1,=b
MOV R4,#1
l1:
LDRB R3,[R0]
STRB R3,[R1]
ADD R0,R0,#1
ADD R1,R1,#1
ADD R4,R4,#1
CMP R4, #11
BNE l1

SWI 0x011