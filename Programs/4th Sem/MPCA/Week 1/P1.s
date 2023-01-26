.text
LDR R0,=a
LDR R0, [R0]
ANDS R1,R0,#1
BEQ even
BNE odd
even:
    MOV R2,#0
    B end
odd:
    MOV R2, #255
    B end
end:
.data
a: .word 21
.end