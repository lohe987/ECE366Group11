.data

P: .word 57  # Power to be used
Q: .word 45
R: .word -1 # Result

.text
	lw 	$t3, 0x2000 		# Load Power into regsiter
	li 	$t1, 1			# Init the result regsiter to p = 0 base case
loop:

	sll	$t1, $t1, 1		# Shift by one left
	li	$t2, 0			# Place holder
	add	$t2, $t2, $t1		# $t2 = $t1 + $t1 + $t1
	add	$t2, $t2, $t1
	add	$t2, $t2, $t1
	sw	$t2, 0x2008		# Store and shift word
	lw	$t1, 0x2008	
	
	lw	$t0, 0x2004		# Load Q
	mod:	
		blt	$t1, $t0, out	# Subtract as needed
		sub	$t1, $t1, $t0
		j 	mod		# Jump in loop
	out:
		
	li	$t0, 1		# Update power see if at end
	sub	$t3, $t3, $t0
	blt	$t3, $t0, end
	j 	loop	# Jump in loop
end:
sw	$t1, 0x2008	# Save word into result space

dead: 	j dead
