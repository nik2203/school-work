@Write an ALP to find how many times the given character is present in a string.
.data
a: .asciz "Hello World"
letter: .asciz "l"

.text
LDR R0, =a
LDR R1, =letter
LDRB R3, [R1]
MOV R4, #0

l:
    LDRB R2, [R0], #1
    CMP R2, R3
    ADDEQ R4, R4, #1
    CMP R2, #00
    BNE l

SWI 0x11
.end
