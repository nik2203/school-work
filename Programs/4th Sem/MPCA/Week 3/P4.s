@Convolution using MLA
.data
a: .word 1,2,3,4,5,6,7,8,9
b: .word 10,20,30,40,50,60,70,80,90
c: .word 0

.text
LDR R0,=a
LDR R1,=b
LDR R2,=c
MOV R5,#0
MOV R6,#1
l:
    LDR R3,[R0],#4
    LDR R4,[R1],#4
    MLA R5,R3,R4,R5
    ADD R6,R6,#1
    CMP R6,#10
    BNE l
    B end
end:
    STR R5,[R2]
    SWI 0x11