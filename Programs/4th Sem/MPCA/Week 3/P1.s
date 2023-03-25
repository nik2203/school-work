@ Fibonacci Sequence
.data
fib: .word 0,0,0,0,0,0,0,0,0,0

.text
MOV R3,#10
LDR R0, =fib
MOV R1, #0
MOV R2, #1
STR R1,[R0],#4
STR R2,[R0],#4
loop:
    ADD R4,R1,R2
    STR R4,[R0],#4
    MOV R1,R2
    MOV R2,R4
    SUB R3,R3,#1
    CMP R3,#2
    BNE loop

SWI 0x011

