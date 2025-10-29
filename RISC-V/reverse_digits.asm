# reverse digit order
.eqv Print,4
.eqv Read,8
.eqv Exit,93

.data
buf: .space 256
prompt1: .asciz "Enter any text combined with letters : "
prompt2: .asciz " Result = "

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
	jal reverse
	
	la a0,prompt2
	li a7,Print
	ecall
	
	la a0, buf
	li a7,Print
	ecall
		
	li a0,0
	li a7,Exit
	ecall

reverse:
	mv t0,a0
loop:
	lbu t2,0(t0)
	beqz t2,done
	
	li t3,'0'
	bltu t2,t3,skip
	li t3,'9'
	bgtu t2,t3,skip
	
	mv t1,t0
find_end:
	addi t0,t0,1
	lbu t2,0(t0)
	
	li t3,'0'
	bleu t2,t3,rev_seq
	li t3,'9'
	bleu t2,t3,find_end

rev_seq:
	addi t0,t0,-1

rev_loop:
	bgt t1,t0,resume
	lbu t2,0(t1)
	lbu t3,0(t0)
	sb t3,0(t1)
	sb t2,0(t0)
	
	addi t1,t1,1
	addi t0,t0,-1
	j rev_loop
resume:
	addi t0,t0,2
	j loop
skip:
	addi t0,t0,1
	j loop
done:
	ret
