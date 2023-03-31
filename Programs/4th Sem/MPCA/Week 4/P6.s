.data
a: .word 20
odd: .asciz "ODD PARITY"
even: .asciz "EVEN PARIRY"

.text
LDR R0,=a
LDR R0,[R0]
MOV R1,#0
MOV R2,#0
MOV R3,#0
MOV R4,#0
START:
    cmp R3,#32
    BEQ END
    TST R0,#1
    BEQ CONTINUE
    ADD R2,R2,#1
CONTINUE:
    MOV R0,R0,LSR#1
    ADD R3,R3,#1
    B START
EVEN:
    LDR R0,=even
    SWI 0x02
    SWI 0x011

END:
    MOV R3,#0
    MOV R4,#0
    TST R2,#1
    BEQ EVEN
    LDR R0,=odd
    SWI 0x02
    SWI 0x011
