# digits to 2's complement
.eqv Print,4
.eqv Read,8
.eqv Exit,93

.data
buffer: .space 256
p1: .asciz "Enter any Text : "
p2: .asciz "Result : "

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
	jal complement
	
	la a0,p2
	li a7,Print
	ecall
	
	la a0,buffer 
	li a7,Print
	ecall
	
	li a0,0 
	li a7,Exit
	ecall

complement:
	mv t0,a0
	mv t1,a0

loop: 
	lbu t2,0(t0)
	addi t0,t0,1
	beqz t2,done
	
	li t3,'0'
	bltu t2,t3,copy
	li t3,'9'
	bgtu t2,t3,copy
	
	sub t2,t3,t2
	addi t2,t2,'0'
	
copy:
	sb t2,0(t1)
	addi t1,t1,1
	j loop

done:
	sb zero,0(t0)
	ret

