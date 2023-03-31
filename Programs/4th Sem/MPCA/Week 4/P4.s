.data
arr: .word 0,3,-1,6,3,9,-4,-2,1,0

.text
LDR R0,=arr
MOV R1,#0
MOV R2,#0
MOV R3,#0
MOV R4,#0
MOV R5,#0

START:
    CMP R2,#10
    BEQ END
    LDR R1,[R0,R2,LSL#2]
    CMP R1,#0
    ADDEQ R3,R3,#1
    ADDGT R4,R4,#1
    ADDMI R5,R5,#1
    ADD R2,R2,#1
    B START
END:
    MOV R1,#0
    MOV R2,#0
    SWI 0x011