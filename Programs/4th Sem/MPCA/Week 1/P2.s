.text
LDR R0, =a
LDR R0, [R0]
CMP R0, #0

ZERO:
    BNE NEGATIVE
    MOV R1, #1
    B end

NEGATIVE:
    BPL POS
    MOV R1,#3
    B end

POS:
    MOV R1, #2

end:
.data
a: .word 0

.end
