@MUL using shift
.text
MOV r0,#4
MOV r2,r0,LSL #4
SUB r2,r2,r0,LSL #3
SWI 0x011