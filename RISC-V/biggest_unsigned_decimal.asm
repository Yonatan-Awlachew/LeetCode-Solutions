# Find biggest unsigned decimal number 

	.eqv	Print_int,	1
	.eqv	Print,		4
	.eqv	Read,		8
	.eqv	Exit,		93
	
	.data
		buf:		.space		256
		prompt1:	.asciz		"Hello, Write any text including numbers : "
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
			jal	largest

			li	a7,	Print_int
			ecall
			
			li	a0,	0
			li	a7,	Exit
			ecall
		
		largest:
			mv	t0,	a0
			li	t1,	0
		loop:
			lbu	t2,	0(t0)
			beqz	t2,	done
			
			li	t3,	'0'
			bltu	t2,	t3,	skip
			li	t3,	'9'
			bgtu	t2,	t3,	skip
			
			li	t3,	0
		parse:
			lbu	t2,	0(t0)
			li	t4,	'0'
			bltu	t2,	t4,	check_max
			li	t4,	'9'
			bgtu	t2,	t4,	check_max
			
			# t3 = t3 * 10 + (t2 - '0')
			li	t4,	10
			mul	t3,	t3,	t4
			li	t4,	'0'
			sub	t2,	t2,	t4
			add	t3,	t3,	t2
			
			addi	t0,	t0,	1
			j 	parse
		check_max:
			ble	t3,	t1,	loop
			mv	t1,	t3
			j	loop	
		skip:
			addi	t0,	t0,	1
			j	loop
		
		done:
			mv 	a0,	t1
			ret
