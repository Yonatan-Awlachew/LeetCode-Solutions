# Remove characters preceded by digits

	.eqv	Print_int,	1
	.eqv	Print,		4
	.eqv	Read,		8
	.eqv	Exit,		93
	
	.data
		buf:		.space		256
		prompt1:	.asciz		"Hello, Write any text and digit : "
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
			jal	preceded
			
			la	a0,	buf
			li	a7,	Print
			ecall
			
			li	a0,	0
			li	a7,	Exit
			ecall
			
		preceded:
			mv	t0,	a0
			mv	t1,	a0
			li	t5,	0
		
		loop:
			lbu	t2,	0(t0)
			addi	t0,	t0,	1
			beqz	t2,	done
			
			li	t3,	'0'
			bltu	t2,	t3,	not_digit
			li	t3,	'9'
			bgtu	t2,	t3,	not_digit
			
			sb	t2,	0(t1)
			li	t5,	1
			addi	t1,	t1,	1
			j	loop
			
		not_digit:
			bnez	t5,	skip
			sb	t2,	0(t1)
			addi	t1,	t1,	1
			j	loop
			
		skip:
			li	t5,	0
			j	loop
		done:
			sb	zero,	0(t1)
			ret
