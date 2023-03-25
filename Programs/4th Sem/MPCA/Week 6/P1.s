@Write an ALP to find the length of a string
.data
a: .asciz "Hello World"

.text
LDR R0, =a 
MOV R1, #0
l:
    LDRB R2,[R0]
    CMP R2, #0
    ADDNE R1,R1,#1
    BEQ end
    ADD R0,R0,#1
    B l

end:
    LDR R0,=a
    SWI 0X02
    SWI 0x011
    .end