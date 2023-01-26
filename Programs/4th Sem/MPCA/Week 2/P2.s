.text

ldr r0,=a
ldr r1,=b
ldr r2,=c

ldrh r3,[r0]
ldrh r4,[r1]
add r5,r3,r4
strh r5,[r2]

.data

a: .hword 10 
b: .hword 20 
c: .hword 0


.end