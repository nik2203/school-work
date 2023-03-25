@Write an ALP to find whether a given character is present in a string

.data
a: .asciz "The dog jumped over the fox"
search: .asciz "h" @For found, h
f: .asciz "Character Found"
nf: .asciz "Character Not Found"

.text
LDR R0, =a
LDR R1, =search
LDRB R3, [R1]
l:
    LDRB R2, [R0], #1
    CMP R2, R3
    BEQ found
    CMP R2, #00
    BNE l
    B notf

found:
    LDR R0, =f
    B end

notf:
    LDR R0, =nf

end:
    SWI 0x02
    SWI 0x11
    .end
