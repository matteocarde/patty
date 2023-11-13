(define (domain mt-block-grouping)
	(:types
		object
		block - object
	)
	(:constants
		b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 - block
	)
	(:predicates
		(turn_move_block_down ?b - block)
		(turn_move_block_right ?b - block)
		(turn_move_block_up ?b - block)
		(turn_move_block_left ?b - block)
	)
	(:functions
		(min_x )
		(y ?b - block)
		(x ?b - block)
		(max_y )
		(min_y )
		(max_x )
	)
	(:action movecursor_move_block_down_b1_move_block_down_b15
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b1)
			)
		:effect (and
			(turn_move_block_down b15)
			(not (turn_move_block_down b1))
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
	(:action movecursor_move_block_down_b7_move_block_left_b2
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b7)
			)
		:effect (and
			(turn_move_block_left b2)
			(not (turn_move_block_down b7))
		)
	)
	(:action movecursor_move_block_right_b12_move_block_right_b13
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b12)
			)
		:effect (and
			(turn_move_block_right b13)
			(not (turn_move_block_right b12))
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
	(:action movecursor_move_block_right_b3_move_block_right_b5
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b3)
			)
		:effect (and
			(turn_move_block_right b5)
			(not (turn_move_block_right b3))
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
	(:action movecursor_move_block_left_b4_move_block_left_b8
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b4)
			)
		:effect (and
			(turn_move_block_left b8)
			(not (turn_move_block_left b4))
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
	(:action movecursor_move_block_left_b13_move_block_left_b14
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b13)
			)
		:effect (and
			(turn_move_block_left b14)
			(not (turn_move_block_left b13))
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
	(:action movecursor_move_block_right_b4_move_block_down_b10
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b4)
			)
		:effect (and
			(turn_move_block_down b10)
			(not (turn_move_block_right b4))
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
	(:action movecursor_move_block_down_b15_move_block_down_b5
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b15)
			)
		:effect (and
			(turn_move_block_down b5)
			(not (turn_move_block_down b15))
		)
	)
	(:action movecursor_move_block_up_b2_move_block_up_b3
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b2)
			)
		:effect (and
			(turn_move_block_up b3)
			(not (turn_move_block_up b2))
		)
	)
	(:action movecursor_move_block_left_b7_move_block_right_b4
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b7)
			)
		:effect (and
			(turn_move_block_right b4)
			(not (turn_move_block_left b7))
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
	(:action movecursor_move_block_up_b4_move_block_up_b5
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b4)
			)
		:effect (and
			(turn_move_block_up b5)
			(not (turn_move_block_up b4))
		)
	)
	(:action movecursor_move_block_left_b15_move_block_left_b3
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b15)
			)
		:effect (and
			(turn_move_block_left b3)
			(not (turn_move_block_left b15))
		)
	)
	(:action movecursor_move_block_right_b2_move_block_right_b3
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b2)
			)
		:effect (and
			(turn_move_block_right b3)
			(not (turn_move_block_right b2))
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
	(:action movecursor_move_block_down_b4_move_block_down_b6
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b4)
			)
		:effect (and
			(turn_move_block_down b6)
			(not (turn_move_block_down b4))
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
	(:action movecursor_move_block_right_b15_move_block_right_b2
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b15)
			)
		:effect (and
			(turn_move_block_right b2)
			(not (turn_move_block_right b15))
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
	(:action movecursor_move_block_down_b14_move_block_down_b2
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b14)
			)
		:effect (and
			(turn_move_block_down b2)
			(not (turn_move_block_down b14))
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
	(:action movecursor_move_block_right_b11_move_block_right_b12
		:parameters ()
		:precondition 
			(and
				(turn_move_block_right b11)
			)
		:effect (and
			(turn_move_block_right b12)
			(not (turn_move_block_right b11))
		)
	)
	(:action movecursor_move_block_down_b2_move_block_down_b3
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b2)
			)
		:effect (and
			(turn_move_block_down b3)
			(not (turn_move_block_down b2))
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
	(:action movecursor_move_block_up_b15_move_block_up_b2
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b15)
			)
		:effect (and
			(turn_move_block_up b2)
			(not (turn_move_block_up b15))
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
	(:action movecursor_move_block_up_b5_move_block_up_b6
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b5)
			)
		:effect (and
			(turn_move_block_up b6)
			(not (turn_move_block_up b5))
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
	(:action movecursor_move_block_left_b2_move_block_left_b5
		:parameters ()
		:precondition 
			(and
				(turn_move_block_left b2)
			)
		:effect (and
			(turn_move_block_left b5)
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
	(:action movecursor_move_block_up_b9_move_block_down_b1
		:parameters ()
		:precondition 
			(and
				(turn_move_block_up b9)
			)
		:effect (and
			(turn_move_block_down b1)
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
	(:action movecursor_move_block_down_b5_move_block_down_b7
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b5)
			)
		:effect (and
			(turn_move_block_down b7)
			(not (turn_move_block_down b5))
		)
	)
	(:action movecursor_move_block_down_b6_move_block_down_b8
		:parameters ()
		:precondition 
			(and
				(turn_move_block_down b6)
			)
		:effect (and
			(turn_move_block_down b8)
			(not (turn_move_block_down b6))
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
)