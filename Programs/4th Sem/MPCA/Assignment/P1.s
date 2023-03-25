.data
arr: .word 12,43,2,9,10,45,20,76,57,14
search: .word 20
size: .word 10

success: .asciz "Successful search"
failure: .asciz "Unsuccessful search"
 

.text 
    MOV R4,#0
    LDR R0, =arr
    LDR R7, =search
    LDR R1,[R7]
    LDR R8,=size
    LDR R2,[R8]
    SUB R3,R2,#1

binary_search:
    LDR R6,[R0]
    CMP R6,R1
    BEQ successful
    ADD R0,R0,#4
    CMP R3,R4
    BEQ unsuccessful
    ADD R4,R4,#1
    BL binary_search
    BX lr

successful:
    LDR R0,=success
    SWI 0x02
    B end

unsuccessful:
    LDR R0,=failure
    SWI 0x02
    B end

end:
    SWI 0x11