	.eqv 	Print_int,	1
	.eqv	Print,		4
	.eqv	Read,		8
	.eqv	Exit,		93
	
	.data
		buf:	.space	256
		p1:	.asciz	"Enter any text with numbers : "
		p2:	.asciz	"Result : "
	
	 .text
	 	main:
	 	
	 		la	a0,	p1
	 		li	a7,	Print
	 		ecall
	 		
	 		la	a0,	buf
	 		li	a1,	100
	 		li 	a7,	Read
	 		ecall
	 		
	 		la 	a0,	p2
	 		li 	a7,	Print
	 		ecall
	 		
	 		la	a0,	buf
	 		jal 	count_decimal
	 		
	 		mv	a0,	t1
	 		li	a7,	Print_int
	 		ecall
	 		
	 		li 	a0,	0
	 		li	a7,	Exit
	 		ecall
	 	
	 	count_decimal:
	 		mv 	t0,	a0	
	 		li	t1,	0	# used for counting
	 		li	t2,	0	# used as flag for check if it's in sequence or not 
		
		loop:
			lbu 	t3,	0(t0)
			beqz	t3,	done
			
			li	t4,	'0'
			bltu	t3,	t4,	reset
			li	t4,	'9'
			bgtu	t3,	t4,	reset
			
			beqz	t2,	new_seq
			j 	next_char
		new_seq:
			addi 	t1,	t1,	1
			li 	t2,	1
			j	next_char
		reset:
			li	t2,	0
		next_char:
			addi 	t0,	t0,	1
			j 	loop
	 	done:
	 		ret
