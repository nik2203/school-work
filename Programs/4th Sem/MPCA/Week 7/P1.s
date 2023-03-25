@ Q1
@ PES2UG21CS334

.data

del: .word 100000
arr: .byte 0xED, 0x60, 0xCE, 0xEA, 0x63, 0xAB, 0xAF, 0xE0, 0xEF, 0xE3, 0xE7, 0x2F, 0x8D, 0x6E, 0x8F, 0x87
PES: .byte 0xC7, 0x8F, 0xAB

.text

up:
LDR R1,=arr
MOV R3,#0

ul:
LDRB R0,[R1]
SWI 0x200

BL delay

CMP R3,#15
BEQ down
ADD R3,R3,#1
ADD R1,R1,#1
B ul

down:
LDR R1,=PES
SUB R1,R1,#1
MOV R3,#0

dl:
LDRB R0,[R1]
SWI 0x200

BL delay

CMP R3,#15
BEQ pes
ADD R3,R3,#1
SUB R1,R1,#1
B dl

pes:
LDR R1,=PES
MOV R3,#0

pl:
LDRB R0,[R1]
SWI 0x200

BL delay

CMP R3,#15
BEQ end
ADD R3,R3,#1
ADD R1,R1,#1
B pl

delay:
LDR R2,=del
LDR R2,[R2]

l:
CMP R2,#0
MOVEQ PC,LR 

SUB R2,R2,#1
B l 

end:
MOV R0,#0
SWI 0x200
SWI 0x011
.end

