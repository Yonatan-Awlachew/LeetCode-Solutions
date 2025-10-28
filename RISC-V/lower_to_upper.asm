# To upper
.eqv Print,4
.eqv Read,8
.eqv Exit,93

.data
buffer: .space 256
p1: .asciz "Enter any Text : "
p2: .asciz "Length : "

.text 
main:
	la a0,p1
	li a7,Print
	ecall
	
	la a0,buffer
	li a1,256
	li a7,Read
	ecall
	
	la a0,buffer
	jal to_upper
	
	la a0,p2
	li a7,Print
	ecall
	
	la a0,buffer 
	li a7,Print
	ecall
	
	li a0,0 
	li a7,Exit
	ecall

to_upper:
	mv t0,a0
	mv t1,a0

loop:
	lbu t2,0(t0)
	addi t0,t0,1
	beqz t2,done
	
	li t3,' '
	beq t2,t3,copy
	
	li t3,'a'
	bltu t2,t3,check_upper
	li t3,'z'
	bgtu t2,t3,check_upper
	
	addi t2,t2,-32

check_upper:
	li t3,'A'
	bltu t2,t3,loop
	li t3,'Z'
	bleu t2,t3,copy
copy:
	sb t2,0(t1)
	addi t1,t1,1
	j loop
done:
	sb zero,0(t1)
	ret
