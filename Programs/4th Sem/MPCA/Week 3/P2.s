@Smallest number
.data
a: .word 9,53,1,7,33,56,48,93,90,51 
b: .word -1

.text
LDR R0,=a
LDR R1,[R0],#4
LDR R4,=b
MOV R3,#1
l:
    LDR R2,[R0],#4
    CMP R1,R2
    MOVGT R1,R2
    ADD R3,R3,#1
    CMP R3,#9
    BNE l
    B exit
    
exit:
    STR R1,[R4]
    SWI 0x11