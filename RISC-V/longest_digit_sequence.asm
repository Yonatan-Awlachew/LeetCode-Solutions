# Display longest digit sequence

	.eqv	Print_int,	1
	.eqv	Print,		4
	.eqv	Read,		8
	.eqv	Exit,		93
	
	.data
		buf:		.space		256
		output:		.space		256
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
			la	a1,	output
			jal	longest
			
			la	a0,	output
			li	a7,	Print
			ecall
			
			li	a0,	0
			li	a7,	Exit
			ecall
			
		longest:
			mv	t0,	a0
			li	t1,	0
			li	t2,	0
		loop:
			lbu	t3,	0(t0)
			beqz	t3,	extract
			
			li	t4,	'0'
			bltu	t3,	t4,	skip
			li	t4,	'9'
			bgtu	t3,	t4,	skip
			
			mv	t5,	t0
			li	t6,	0
		count:
			lbu	t3,	0(t0)
			
			li	t4,	'0'
			bltu	t3,	t4,	check_max
			li	t4,	'9'
			bgtu	t3,	t4,	check_max
			
			addi	t6,	t6,	1
			addi	t0,	t0,	1
			j	count
			
		check_max:
			bltu	t6,	t1,	loop
			mv	t1,	t6
			mv	t2,	t5
			j	loop
		skip:	
			addi	t0,	t0,	1
			j	loop
		extract:
			beqz	t1,	empty
			mv	t0,	t2	
			mv	t3,	a1
			mv	t4,	t1
		copy_loop:
			beqz	t4,	done
			lbu	t5,	0(t0)
			sb	t5,	0(t3)
			addi	t0,	t0,	1
			addi	t3,	t3,	1
			addi	t4,	t4,	-1
			j	copy_loop
		done:
			sb	zero,	0(t3)
			ret
		empty:
			sb	zero,	0(a1)
			ret
