.eqv Print_int,1
.eqv Print,4
.eqv Read,8
.eqv Exit,93

.data
message1: .asciz "Enter any Text : "
buf: .space 256
result: "Result: "

.text
main:
	la a0,message1
	li a7,Print
	ecall
	
	la a0,buf
	li a1,256
	li a7,Read
	ecall
	
	la a0,result
	li a7,Print
	ecall
	
	la a0,buf
	jal remove_space
		
	
	la a0,buf
	li a7,Print
	ecall
	
	li a0,0
	li a7,Exit
	ecall

remove_space:
	mv t0,a0
	mv t1,a0
	li t3,' '
loop:
	lbu t2,0(t0)
	addi t0,t0,1
	beqz t2,end
	
	beq t2,t3,loop
	
	sb t2,0(t1)
	addi t1,t1,1
	j loop
	
end:
	sb zero,0(t1)
	ret
