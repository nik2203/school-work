.data
a: .word 11
ODD: .ASCIZ "Odd Parity"
EVEN: .ASCIZ "Even Parity"

.text
LDR R0,=a
LDR R0,[R0]
MOV R1,#0
MOV R2,#0
MOV R3,#0
MOV R4,#0
START:
    CMP R3,#32
    BEQ END
    TST R0,#1
    BEQ ZERO
    ADD R2,R2,#1
    B CONTINUE
ZERO:
    ADD R1,R1,#1
CONTINUE:
    MOV R0,R0,LSR#1
    ADD R3,R3,#1
    B START
END:
    TST R2, #1
    LDREQ R0, =EVEN
    LDRNE R0, =ODD
    MOV R3,#0
    MOV R4,#0
    SWI 0x02
    SWI 0x11