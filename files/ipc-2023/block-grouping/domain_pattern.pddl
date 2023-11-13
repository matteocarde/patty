(define (domain mt-block-grouping)
	(:types
		object
		block - object
	)
	(:constants
		b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 b16 b17 b18 b19 b20 b21 b22 b23 b24 b25 - block
	)
	(:predicates
		(turn_move_block_left ?b - block)
		(turn_move_block_up ?b - block)
		(turn_move_block_right ?b - block)
		(turn_move_block_down ?b - block)
	)
	(:functions
		(max_y )
		(x ?b - block)
		(min_x )
		(min_y )
		(y ?b - block)
		(max_x )
	)
	(:action movecursor_move_block_up_b8_move_block_up_b9
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b8)
			)
		:effect (and
			(turn_move_block_up b9)
			(not (turn_move_block_up b8))
		)
	)
	(:action movecursor_move_block_down_b12_move_block_down_b13
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b12)
			)
		:effect (and
			(turn_move_block_down b13)
			(not (turn_move_block_down b12))
		)
	)
	(:action movecursor_move_block_up_b3_move_block_up_b4
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b3)
			)
		:effect (and
			(turn_move_block_up b4)
			(not (turn_move_block_up b3))
		)
	)
	(:action movecursor_move_block_down_b2_move_block_down_b20
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b2)
			)
		:effect (and
			(turn_move_block_down b20)
			(not (turn_move_block_down b2))
		)
	)
	(:action movecursor_move_block_left_b17_move_block_right_b12
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b17)
			)
		:effect (and
			(turn_move_block_right b12)
			(not (turn_move_block_left b17))
		)
	)
	(:action movecursor_move_block_right_b16_move_block_right_b17
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b16)
			)
		:effect (and
			(turn_move_block_right b17)
			(not (turn_move_block_right b16))
		)
	)
	(:action movecursor_move_block_down_b23_move_block_down_b25
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b23)
			)
		:effect (and
			(turn_move_block_down b25)
			(not (turn_move_block_down b23))
		)
	)
	(:action movecursor_move_block_left_b16_move_block_left_b18
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b16)
			)
		:effect (and
			(turn_move_block_left b18)
			(not (turn_move_block_left b16))
		)
	)
	(:action move_block_right
		:parameters (?b - block)
		:precondition 
			(and
				(<= (+ (x ?b) 1.0) (max_x))
				(turn_move_block_right ?b)
			)
		:effect (and
			(increase (x ?b) 1.0)
		)
	)
	(:action movecursor_move_block_down_b6_move_block_down_b7
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b6)
			)
		:effect (and
			(turn_move_block_down b7)
			(not (turn_move_block_down b6))
		)
	)
	(:action movecursor_move_block_right_b1_move_block_right_b10
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b1)
			)
		:effect (and
			(turn_move_block_right b10)
			(not (turn_move_block_right b1))
		)
	)
	(:action movecursor_move_block_right_b21_move_block_right_b22
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b21)
			)
		:effect (and
			(turn_move_block_right b22)
			(not (turn_move_block_right b21))
		)
	)
	(:action movecursor_move_block_up_b14_move_block_up_b15
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b14)
			)
		:effect (and
			(turn_move_block_up b15)
			(not (turn_move_block_up b14))
		)
	)
	(:action movecursor_move_block_down_b11_move_block_down_b12
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b11)
			)
		:effect (and
			(turn_move_block_down b12)
			(not (turn_move_block_down b11))
		)
	)
	(:action movecursor_move_block_down_b21_move_block_down_b22
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b21)
			)
		:effect (and
			(turn_move_block_down b22)
			(not (turn_move_block_down b21))
		)
	)
	(:action movecursor_move_block_left_b20_move_block_left_b21
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b20)
			)
		:effect (and
			(turn_move_block_left b21)
			(not (turn_move_block_left b20))
		)
	)
	(:action movecursor_move_block_right_b17_move_block_right_b19
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b17)
			)
		:effect (and
			(turn_move_block_right b19)
			(not (turn_move_block_right b17))
		)
	)
	(:action move_block_up
		:parameters (?b - block)
		:precondition 
			(and
				(<= (+ (y ?b) 1.0) (max_y))
				(turn_move_block_up ?b)
			)
		:effect (and
			(increase (y ?b) 1.0)
		)
	)
	(:action movecursor_move_block_left_b22_move_block_left_b23
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b22)
			)
		:effect (and
			(turn_move_block_left b23)
			(not (turn_move_block_left b22))
		)
	)
	(:action movecursor_move_block_down_b3_move_block_down_b4
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b3)
			)
		:effect (and
			(turn_move_block_down b4)
			(not (turn_move_block_down b3))
		)
	)
	(:action movecursor_move_block_up_b1_move_block_up_b10
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b1)
			)
		:effect (and
			(turn_move_block_up b10)
			(not (turn_move_block_up b1))
		)
	)
	(:action movecursor_move_block_right_b23_move_block_right_b24
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b23)
			)
		:effect (and
			(turn_move_block_right b24)
			(not (turn_move_block_right b23))
		)
	)
	(:action movecursor_move_block_right_b10_move_block_right_b11
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b10)
			)
		:effect (and
			(turn_move_block_right b11)
			(not (turn_move_block_right b10))
		)
	)
	(:action movecursor_move_block_down_b20_move_block_down_b21
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b20)
			)
		:effect (and
			(turn_move_block_down b21)
			(not (turn_move_block_down b20))
		)
	)
	(:action movecursor_move_block_up_b25_move_block_up_b5
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b25)
			)
		:effect (and
			(turn_move_block_up b5)
			(not (turn_move_block_up b25))
		)
	)
	(:action movecursor_move_block_down_b24_move_block_left_b14
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b24)
			)
		:effect (and
			(turn_move_block_left b14)
			(not (turn_move_block_down b24))
		)
	)
	(:action movecursor_move_block_right_b9_move_block_up_b1
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b9)
			)
		:effect (and
			(turn_move_block_up b1)
			(not (turn_move_block_right b9))
		)
	)
	(:action movecursor_move_block_right_b12_move_block_right_b18
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b12)
			)
		:effect (and
			(turn_move_block_right b18)
			(not (turn_move_block_right b12))
		)
	)
	(:action movecursor_move_block_left_b9_move_block_right_b1
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b9)
			)
		:effect (and
			(turn_move_block_right b1)
			(not (turn_move_block_left b9))
		)
	)
	(:action movecursor_move_block_up_b18_move_block_up_b19
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b18)
			)
		:effect (and
			(turn_move_block_up b19)
			(not (turn_move_block_up b18))
		)
	)
	(:action movecursor_move_block_right_b18_move_block_up_b25
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b18)
			)
		:effect (and
			(turn_move_block_up b25)
			(not (turn_move_block_right b18))
		)
	)
	(:action movecursor_move_block_up_b21_move_block_up_b22
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b21)
			)
		:effect (and
			(turn_move_block_up b22)
			(not (turn_move_block_up b21))
		)
	)
	(:action movecursor_move_block_right_b19_move_block_right_b2
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b19)
			)
		:effect (and
			(turn_move_block_right b2)
			(not (turn_move_block_right b19))
		)
	)
	(:action movecursor_move_block_right_b8_move_block_right_b9
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b8)
			)
		:effect (and
			(turn_move_block_right b9)
			(not (turn_move_block_right b8))
		)
	)
	(:action movecursor_move_block_up_b15_move_block_up_b16
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b15)
			)
		:effect (and
			(turn_move_block_up b16)
			(not (turn_move_block_up b15))
		)
	)
	(:action movecursor_move_block_down_b22_move_block_down_b23
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b22)
			)
		:effect (and
			(turn_move_block_down b23)
			(not (turn_move_block_down b22))
		)
	)
	(:action movecursor_move_block_down_b14_move_block_down_b15
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b14)
			)
		:effect (and
			(turn_move_block_down b15)
			(not (turn_move_block_down b14))
		)
	)
	(:action movecursor_move_block_down_b15_move_block_down_b16
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b15)
			)
		:effect (and
			(turn_move_block_down b16)
			(not (turn_move_block_down b15))
		)
	)
	(:action movecursor_move_block_left_b1_move_block_left_b10
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b1)
			)
		:effect (and
			(turn_move_block_left b10)
			(not (turn_move_block_left b1))
		)
	)
	(:action movecursor_move_block_right_b13_move_block_right_b14
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b13)
			)
		:effect (and
			(turn_move_block_right b14)
			(not (turn_move_block_right b13))
		)
	)
	(:action movecursor_move_block_down_b19_move_block_down_b2
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b19)
			)
		:effect (and
			(turn_move_block_down b2)
			(not (turn_move_block_down b19))
		)
	)
	(:action movecursor_move_block_left_b3_move_block_left_b4
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b3)
			)
		:effect (and
			(turn_move_block_left b4)
			(not (turn_move_block_left b3))
		)
	)
	(:action movecursor_move_block_up_b6_move_block_up_b7
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b6)
			)
		:effect (and
			(turn_move_block_up b7)
			(not (turn_move_block_up b6))
		)
	)
	(:action movecursor_move_block_down_b4_move_block_down_b5
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b4)
			)
		:effect (and
			(turn_move_block_down b5)
			(not (turn_move_block_down b4))
		)
	)
	(:action movecursor_move_block_down_b7_move_block_down_b8
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b7)
			)
		:effect (and
			(turn_move_block_down b8)
			(not (turn_move_block_down b7))
		)
	)
	(:action movecursor_move_block_up_b10_move_block_up_b11
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b10)
			)
		:effect (and
			(turn_move_block_up b11)
			(not (turn_move_block_up b10))
		)
	)
	(:action movecursor_move_block_left_b11_move_block_left_b12
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b11)
			)
		:effect (and
			(turn_move_block_left b12)
			(not (turn_move_block_left b11))
		)
	)
	(:action move_block_down
		:parameters (?b - block)
		:precondition 
			(and
				(>= (- (y ?b) 1.0) (min_y))
				(turn_move_block_down ?b)
			)
		:effect (and
			(decrease (y ?b) 1.0)
		)
	)
	(:action movecursor_move_block_left_b10_move_block_left_b11
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b10)
			)
		:effect (and
			(turn_move_block_left b11)
			(not (turn_move_block_left b10))
		)
	)
	(:action movecursor_move_block_left_b15_move_block_left_b17
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b15)
			)
		:effect (and
			(turn_move_block_left b17)
			(not (turn_move_block_left b15))
		)
	)
	(:action movecursor_move_block_down_b18_move_block_down_b19
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b18)
			)
		:effect (and
			(turn_move_block_down b19)
			(not (turn_move_block_down b18))
		)
	)
	(:action movecursor_move_block_down_b1_move_block_down_b10
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b1)
			)
		:effect (and
			(turn_move_block_down b10)
			(not (turn_move_block_down b1))
		)
	)
	(:action movecursor_move_block_down_b25_move_block_down_b3
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b25)
			)
		:effect (and
			(turn_move_block_down b3)
			(not (turn_move_block_down b25))
		)
	)
	(:action move_block_left
		:parameters (?b - block)
		:precondition 
			(and
				(>= (- (x ?b) 1.0) (min_x))
				(turn_move_block_left ?b)
			)
		:effect (and
			(decrease (x ?b) 1.0)
		)
	)
	(:action movecursor_move_block_left_b23_move_block_left_b24
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b23)
			)
		:effect (and
			(turn_move_block_left b24)
			(not (turn_move_block_left b23))
		)
	)
	(:action movecursor_move_block_up_b13_move_block_up_b14
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b13)
			)
		:effect (and
			(turn_move_block_up b14)
			(not (turn_move_block_up b13))
		)
	)
	(:action movecursor_move_block_up_b9_move_block_down_b24
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b9)
			)
		:effect (and
			(turn_move_block_down b24)
			(not (turn_move_block_up b9))
		)
	)
	(:action movecursor_move_block_right_b14_move_block_right_b15
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b14)
			)
		:effect (and
			(turn_move_block_right b15)
			(not (turn_move_block_right b14))
		)
	)
	(:action movecursor_move_block_up_b22_move_block_up_b23
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b22)
			)
		:effect (and
			(turn_move_block_up b23)
			(not (turn_move_block_up b22))
		)
	)
	(:action movecursor_move_block_left_b21_move_block_left_b22
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b21)
			)
		:effect (and
			(turn_move_block_left b22)
			(not (turn_move_block_left b21))
		)
	)
	(:action movecursor_move_block_down_b16_move_block_down_b17
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b16)
			)
		:effect (and
			(turn_move_block_down b17)
			(not (turn_move_block_down b16))
		)
	)
	(:action movecursor_move_block_left_b25_move_block_left_b3
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b25)
			)
		:effect (and
			(turn_move_block_left b3)
			(not (turn_move_block_left b25))
		)
	)
	(:action movecursor_move_block_down_b8_move_block_down_b9
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b8)
			)
		:effect (and
			(turn_move_block_down b9)
			(not (turn_move_block_down b8))
		)
	)
	(:action movecursor_move_block_left_b4_move_block_left_b5
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b4)
			)
		:effect (and
			(turn_move_block_left b5)
			(not (turn_move_block_left b4))
		)
	)
	(:action movecursor_move_block_up_b16_move_block_up_b17
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b16)
			)
		:effect (and
			(turn_move_block_up b17)
			(not (turn_move_block_up b16))
		)
	)
	(:action movecursor_move_block_left_b6_move_block_left_b7
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b6)
			)
		:effect (and
			(turn_move_block_left b7)
			(not (turn_move_block_left b6))
		)
	)
	(:action movecursor_move_block_up_b5_move_block_down_b1
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b5)
			)
		:effect (and
			(turn_move_block_down b1)
			(not (turn_move_block_up b5))
		)
	)
	(:action movecursor_move_block_right_b25_move_block_right_b3
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b25)
			)
		:effect (and
			(turn_move_block_right b3)
			(not (turn_move_block_right b25))
		)
	)
	(:action movecursor_move_block_up_b19_move_block_up_b2
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b19)
			)
		:effect (and
			(turn_move_block_up b2)
			(not (turn_move_block_up b19))
		)
	)
	(:action movecursor_move_block_up_b17_move_block_up_b18
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b17)
			)
		:effect (and
			(turn_move_block_up b18)
			(not (turn_move_block_up b17))
		)
	)
	(:action movecursor_move_block_left_b5_move_block_left_b6
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b5)
			)
		:effect (and
			(turn_move_block_left b6)
			(not (turn_move_block_left b5))
		)
	)
	(:action movecursor_move_block_right_b11_move_block_right_b13
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b11)
			)
		:effect (and
			(turn_move_block_right b13)
			(not (turn_move_block_right b11))
		)
	)
	(:action movecursor_move_block_down_b10_move_block_down_b11
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b10)
			)
		:effect (and
			(turn_move_block_down b11)
			(not (turn_move_block_down b10))
		)
	)
	(:action movecursor_move_block_up_b23_move_block_up_b24
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b23)
			)
		:effect (and
			(turn_move_block_up b24)
			(not (turn_move_block_up b23))
		)
	)
	(:action movecursor_move_block_up_b12_move_block_up_b13
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b12)
			)
		:effect (and
			(turn_move_block_up b13)
			(not (turn_move_block_up b12))
		)
	)
	(:action movecursor_move_block_left_b19_move_block_left_b2
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b19)
			)
		:effect (and
			(turn_move_block_left b2)
			(not (turn_move_block_left b19))
		)
	)
	(:action movecursor_move_block_down_b17_move_block_down_b18
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b17)
			)
		:effect (and
			(turn_move_block_down b18)
			(not (turn_move_block_down b17))
		)
	)
	(:action movecursor_move_block_up_b20_move_block_up_b21
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b20)
			)
		:effect (and
			(turn_move_block_up b21)
			(not (turn_move_block_up b20))
		)
	)
	(:action movecursor_move_block_left_b8_move_block_left_b9
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b8)
			)
		:effect (and
			(turn_move_block_left b9)
			(not (turn_move_block_left b8))
		)
	)
	(:action movecursor_move_block_left_b24_move_block_left_b25
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b24)
			)
		:effect (and
			(turn_move_block_left b25)
			(not (turn_move_block_left b24))
		)
	)
	(:action movecursor_move_block_left_b14_move_block_left_b15
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b14)
			)
		:effect (and
			(turn_move_block_left b15)
			(not (turn_move_block_left b14))
		)
	)
	(:action movecursor_move_block_left_b7_move_block_left_b8
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b7)
			)
		:effect (and
			(turn_move_block_left b8)
			(not (turn_move_block_left b7))
		)
	)
	(:action movecursor_move_block_right_b15_move_block_right_b16
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b15)
			)
		:effect (and
			(turn_move_block_right b16)
			(not (turn_move_block_right b15))
		)
	)
	(:action movecursor_move_block_right_b3_move_block_right_b4
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b3)
			)
		:effect (and
			(turn_move_block_right b4)
			(not (turn_move_block_right b3))
		)
	)
	(:action movecursor_move_block_up_b4_move_block_up_b6
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b4)
			)
		:effect (and
			(turn_move_block_up b6)
			(not (turn_move_block_up b4))
		)
	)
	(:action movecursor_move_block_left_b2_move_block_left_b20
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b2)
			)
		:effect (and
			(turn_move_block_left b20)
			(not (turn_move_block_left b2))
		)
	)
	(:action movecursor_move_block_right_b5_move_block_right_b6
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b5)
			)
		:effect (and
			(turn_move_block_right b6)
			(not (turn_move_block_right b5))
		)
	)
	(:action movecursor_move_block_right_b7_move_block_right_b8
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b7)
			)
		:effect (and
			(turn_move_block_right b8)
			(not (turn_move_block_right b7))
		)
	)
	(:action movecursor_move_block_up_b7_move_block_up_b8
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b7)
			)
		:effect (and
			(turn_move_block_up b8)
			(not (turn_move_block_up b7))
		)
	)
	(:action movecursor_move_block_up_b11_move_block_up_b12
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b11)
			)
		:effect (and
			(turn_move_block_up b12)
			(not (turn_move_block_up b11))
		)
	)
	(:action movecursor_move_block_up_b24_move_block_up_b3
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b24)
			)
		:effect (and
			(turn_move_block_up b3)
			(not (turn_move_block_up b24))
		)
	)
	(:action movecursor_move_block_left_b18_move_block_left_b19
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b18)
			)
		:effect (and
			(turn_move_block_left b19)
			(not (turn_move_block_left b18))
		)
	)
	(:action movecursor_move_block_right_b20_move_block_right_b21
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b20)
			)
		:effect (and
			(turn_move_block_right b21)
			(not (turn_move_block_right b20))
		)
	)
	(:action movecursor_move_block_right_b22_move_block_right_b23
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b22)
			)
		:effect (and
			(turn_move_block_right b23)
			(not (turn_move_block_right b22))
		)
	)
	(:action movecursor_move_block_right_b6_move_block_right_b7
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b6)
			)
		:effect (and
			(turn_move_block_right b7)
			(not (turn_move_block_right b6))
		)
	)
	(:action movecursor_move_block_right_b24_move_block_right_b25
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b24)
			)
		:effect (and
			(turn_move_block_right b25)
			(not (turn_move_block_right b24))
		)
	)
	(:action movecursor_move_block_left_b13_move_block_left_b16
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b13)
			)
		:effect (and
			(turn_move_block_left b16)
			(not (turn_move_block_left b13))
		)
	)
	(:action movecursor_move_block_right_b4_move_block_right_b5
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b4)
			)
		:effect (and
			(turn_move_block_right b5)
			(not (turn_move_block_right b4))
		)
	)
	(:action movecursor_move_block_up_b2_move_block_up_b20
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b2)
			)
		:effect (and
			(turn_move_block_up b20)
			(not (turn_move_block_up b2))
		)
	)
	(:action movecursor_move_block_down_b9_move_block_left_b1
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b9)
			)
		:effect (and
			(turn_move_block_left b1)
			(not (turn_move_block_down b9))
		)
	)
	(:action movecursor_move_block_down_b13_move_block_down_b14
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b13)
			)
		:effect (and
			(turn_move_block_down b14)
			(not (turn_move_block_down b13))
		)
	)
	(:action movecursor_move_block_left_b12_move_block_left_b13
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b12)
			)
		:effect (and
			(turn_move_block_left b13)
			(not (turn_move_block_left b12))
		)
	)
	(:action movecursor_move_block_right_b2_move_block_right_b20
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b2)
			)
		:effect (and
			(turn_move_block_right b20)
			(not (turn_move_block_right b2))
		)
	)
	(:action movecursor_move_block_down_b5_move_block_down_b6
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b5)
			)
		:effect (and
			(turn_move_block_down b6)
			(not (turn_move_block_down b5))
		)
	)
)