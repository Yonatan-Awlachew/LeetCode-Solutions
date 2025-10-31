# Remove all except the first uppercase sequences
	.eqv	Print_int,	1
	.eqv	Print,		4
	.eqv	Read,		8
	.eqv	Exit,		93
	
	.data
		buf:		.space		256
		prompt1:	.asciz		"Hello, Write any text : "
		prompt2:	.asciz		"Result : "
	
	.text
		main:
			la 	a0,	prompt1
			li 	a7,	Print
			ecall	
			
			la	a0,	buf
			li	a1,	256
			li 	a7,	Read
			ecall
			
			la	a0,	prompt2
			li	a7,	Print
			ecall
			
			la	a0,	buf
			jal	keep_first
			
			la 	a0,	buf
			li	a7,	Print
			ecall
			
			li	a0,	0
			li	a7,	Exit
			ecall
		
		keep_first:
			mv	t0,	a0
			mv	t1,	t0
			li	t5,	0
		
		loop:
			lbu	t2,	0(t0)
			addi	t0,	t0,	1
			beqz	t2,	done
			
			li	t3,	'A'
			bltu	t2,	t3,	skip
			li	t3,	'Z'
			bgtu	t2,	t3,	skip
			
			beqz	t5,	upper
			j	loop
		
		upper:
			sb	t2,	0(t1)
			addi	t1,	t1,	1
			li	t5,	1
			j	loop
		
		skip:
			sb	t2,	0(t1)
			addi	t1,	t1,	1
			li	t5,	0
			j	loop
		
		done:	
			sb	zero,	0(t1)
			ret
			
