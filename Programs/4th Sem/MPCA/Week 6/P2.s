@Write an ALP to copy string from one location to another
.data

a: .asciz "Hello World"
b: .asciz "ABCDE EFGHI"

.text
LDR R0, =a
LDR R1, =b
l:
    LDRB R2, [R0], #1
    STRB R2, [R1], #1
    CMP R2, #00
    BNE l
LDR R0, =b
SWI 0x02
SWI 0x11
.end
