.eqv Print_int,1
.eqv Print,4
.eqv Read,8
.eqv Exit,93

.data
message1: .asciz "Enter any Text : "
buf: .space 256
result: "Length: "

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
	jal count
		
	
	mv a0,t1
	li a7,Print_int
	ecall
	
	li a0,0
	li a7,Exit
	ecall

count:
	mv t0,a0
	li t1,0
	li t3,'\n'
loop:
	lbu t2,0(t0)
	beqz t2,end
	
	beq t2,t3,end
	
	addi t0,t0,1
	addi t1,t1,1
	j loop
	
end:
	mv a0,t1
	ret
