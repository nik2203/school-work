.data
a: .word -15
p: .ASCIZ "positive"
n: .ASCIZ "negative"


.text
LDR R1,=a
LDR R2,[R1]
CMP R2, #0
BLT min
LDR R0, =p
B END

min:
    LDR R0, =n

END:
    SWI 0x02
    SWI 0x11
    .end