.data
#T: .word 12
T: .word 0xABCDEF00
#T: .word -5
best_matching_score: .word -1 # best score = ? within [0, 32]
best_matching_count: .word -1 # how many patterns achieve the best score?
Pattern_Array: .word 0, 1, 2, 3, 4, -1, -2, -3, -4, -5, 0xEEEEEEEE, 0x44448888, 0x77777777, 0x33333333, 0xAAAAAAAA, 0xFFFF0000, 0xFFFF, 0xCCCCCCCC, 0x66666666, 0x99999999  
#Pattern_Array: .word 0, 1, 2, 3, 4, -1, -2, -3, -4, -5, 0xEEEEEEEE, 0x44448888, 0x77777777, 0x33333333, 0xAAAAAAAA, 0xFFFF0000, 0xFFFF, 0xCCCCCCCC, 0x66666666, 0x99999999
#Pattern_Array: .word 1, -2, 3, -4, 5, -6, 7, -8, 9, -10, -5, 5, -5, 5, -5, 1, -2, 3, -4, 5

.text
# Your code goes here
Main:
	addi $4,$4,20		#big counter $4
	addi $5,$5,0x200c	#address of the array
	addi $7,$7,1000
	j Number

Number:
	lw $3,T
	lw $6,($5)
	addi $11,$11,32
	add $12,$0,$0
	
Checker:	
	beq $11,$0,Max_checker
	andi $9,$3,0x1
	andi $10,$6,0x1
	beq $9,$10,shift
	addi $12,$12,1		# this hamming distance for the number
shift:	srl $3,$3,1
	srl $6,$6,1
	subi $11,$11,1
	j Checker
	
Max_checker:
	beq $7,$12,max_equal
	slt $13,$12,$7
	beq $13,0,shift_array
	add $7,$0,$12
	addi $8,$0,1
	j shift_array
	
max_equal:
	addi $8,$8,1
	j shift_array

shift_array:
	subi $4,$4,1
	beq  $4,0,exit
	addi $5,$5,4
	j Number

exit: 
	addi $19,$19,32
	sub  $19,$19,$7
	sw   $19, 0x2004($0)
	sw   $8,  0x2008($0)

Done: 
	j Done
	
	
		


