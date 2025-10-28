.eqv Print,4
.eqv Read,8
.eqv Exit,93

.data
buf: .space 256
prompt1: .asciz "Enter any Text: "
prompt2: .asciz " Result : "

.text
main:
    la a0,prompt1
    li a7,Print
    ecall

    la a0,buf
    li a1,256
    li a7,Read
    ecall

    la a0,buf
    jal only_letters

    la a0,prompt2
    li a7,Print
    ecall

    la a0,buf
    li a7,Print
    ecall

    li a0,0
    li a7,Exit
    ecall

only_letters:
    mv t0,a0
    mv t1,a0
loop:
    lbu t2,0(t0)
    addi t0,t0,1
    beqz t2,end

    li t3,'A'
    bltu t2,t3,check_lower
    li t3,'Z'
    bleu t2,t3,copy

check_lower:
    li t3,'a'
    bltu t2,t3,loop
    li t3,'z'
    bleu t2,t3,copy

copy:
    sb t2,0(t1)
    addi t1,t1,1
    j loop

end:
    sb zero,0(t1)
    ret
