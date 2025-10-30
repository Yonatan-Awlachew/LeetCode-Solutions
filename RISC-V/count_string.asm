# Count length of Text
	.eqv	Print_int,	1
	.eqv	Print,		4
	.eqv	Read,		8
	.eqv	Exit,		93
	
	.data
		buf:		.space		256
		prompt1:	.asciz		"Hello, Write any text : "
		prompt2:	.asciz		"Length : "
	
	.text
		main:
			la 	a0,	prompt1
			li 	a7,	Print
			ecall	
			
			la	a0,	buf
			li	a1,	100
			li 	a7,	Read
			ecall
			
			la	a0,	prompt2
			li	a7,	Print
			ecall
			
			la	a0,	buf
			jal	count
			
			mv	a0,	t1
			li	a7,	Print_int
			ecall
			
			li	a0,	0
			li	a7,	Exit
			ecall
		
		count:
			mv	t0,	a0
			li	t1,	0
			li	t3, '\n'
		
		loop:
			lbu	t2,	0(t0)
			addi	t0,	t0,	1
			beqz	t2,	done
			
			beq	t2,	t3,	done
			addi	t1,	t1,	1
			j loop
		done:
			ret
