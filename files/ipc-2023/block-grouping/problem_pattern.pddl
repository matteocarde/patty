(define (problem instance_15_25_6_3)
	(:domain mt-block-grouping)
	(:objects
		b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 b15 b16 b17 b18 b19 b20 b21 b22 b23 b24 b25 - block
	)
	(:init
		(= (y b24) 1.0)
		(= (min_x) 1.0)
		(= (x b21) 8.0)
		(= (x b11) 4.0)
		(= (y b3) 7.0)
		(= (x b15) 1.0)
		(= (y b10) 13.0)
		(= (x b7) 7.0)
		(= (x b23) 5.0)
		(= (y b19) 8.0)
		(= (min_y) 1.0)
		(= (y b5) 15.0)
		(= (y b6) 6.0)
		(= (y b12) 10.0)
		(= (max_x) 15.0)
		(= (x b19) 4.0)
		(= (y b13) 8.0)
		(= (y b18) 14.0)
		(= (y b23) 6.0)
		(= (x b24) 13.0)
		(= (y b8) 7.0)
		(= (x b3) 10.0)
		(= (y b15) 8.0)
		(= (x b2) 2.0)
		(= (x b10) 13.0)
		(= (y b9) 12.0)
		(= (max_y) 15.0)
		(= (y b20) 6.0)
		(= (y b17) 12.0)
		(= (x b12) 15.0)
		(= (x b4) 2.0)
		(= (y b22) 5.0)
		(turn_move_block_down b1)
		(= (y b11) 5.0)
		(= (y b14) 4.0)
		(= (x b16) 14.0)
		(= (y b25) 15.0)
		(= (y b7) 9.0)
		(= (y b2) 4.0)
		(= (y b16) 11.0)
		(= (x b25) 14.0)
		(= (x b22) 4.0)
		(= (x b18) 15.0)
		(= (y b21) 10.0)
		(= (x b14) 1.0)
		(= (x b13) 8.0)
		(= (x b5) 8.0)
		(= (y b4) 11.0)
		(= (y b1) 14.0)
		(= (x b1) 5.0)
		(= (x b17) 1.0)
		(= (x b8) 6.0)
		(= (x b6) 4.0)
		(= (x b9) 10.0)
		(= (x b20) 7.0)
	)
	(:goal
			(and
					(or
						(not (= (x b1) (x b2)))
						(not (= (y b1) (y b2)))
					)
					(or
						(not (= (x b1) (x b3)))
						(not (= (y b1) (y b3)))
					)
					(or
						(not (= (x b1) (x b4)))
						(not (= (y b1) (y b4)))
					)
					(or
						(not (= (x b1) (x b5)))
						(not (= (y b1) (y b5)))
					)
					(or
						(not (= (x b1) (x b6)))
						(not (= (y b1) (y b6)))
					)
					(or
						(not (= (x b1) (x b7)))
						(not (= (y b1) (y b7)))
					)
				(= (x b1) (x b8))
				(= (y b1) (y b8))
					(or
						(not (= (x b1) (x b9)))
						(not (= (y b1) (y b9)))
					)
					(or
						(not (= (x b1) (x b10)))
						(not (= (y b1) (y b10)))
					)
					(or
						(not (= (x b1) (x b11)))
						(not (= (y b1) (y b11)))
					)
					(or
						(not (= (x b1) (x b12)))
						(not (= (y b1) (y b12)))
					)
					(or
						(not (= (x b1) (x b13)))
						(not (= (y b1) (y b13)))
					)
				(= (x b1) (x b14))
				(= (y b1) (y b14))
					(or
						(not (= (x b1) (x b15)))
						(not (= (y b1) (y b15)))
					)
					(or
						(not (= (x b1) (x b16)))
						(not (= (y b1) (y b16)))
					)
					(or
						(not (= (x b1) (x b17)))
						(not (= (y b1) (y b17)))
					)
					(or
						(not (= (x b1) (x b18)))
						(not (= (y b1) (y b18)))
					)
					(or
						(not (= (x b1) (x b19)))
						(not (= (y b1) (y b19)))
					)
					(or
						(not (= (x b1) (x b20)))
						(not (= (y b1) (y b20)))
					)
					(or
						(not (= (x b1) (x b21)))
						(not (= (y b1) (y b21)))
					)
					(or
						(not (= (x b1) (x b22)))
						(not (= (y b1) (y b22)))
					)
					(or
						(not (= (x b1) (x b23)))
						(not (= (y b1) (y b23)))
					)
					(or
						(not (= (x b1) (x b24)))
						(not (= (y b1) (y b24)))
					)
					(or
						(not (= (x b1) (x b25)))
						(not (= (y b1) (y b25)))
					)
					(or
						(not (= (x b2) (x b3)))
						(not (= (y b2) (y b3)))
					)
					(or
						(not (= (x b2) (x b4)))
						(not (= (y b2) (y b4)))
					)
					(or
						(not (= (x b2) (x b5)))
						(not (= (y b2) (y b5)))
					)
					(or
						(not (= (x b2) (x b6)))
						(not (= (y b2) (y b6)))
					)
					(or
						(not (= (x b2) (x b7)))
						(not (= (y b2) (y b7)))
					)
					(or
						(not (= (x b2) (x b8)))
						(not (= (y b2) (y b8)))
					)
					(or
						(not (= (x b2) (x b9)))
						(not (= (y b2) (y b9)))
					)
				(= (x b2) (x b20))
				(= (y b2) (y b20))
					(or
						(not (= (x b2) (x b21)))
						(not (= (y b2) (y b21)))
					)
					(or
						(not (= (x b2) (x b22)))
						(not (= (y b2) (y b22)))
					)
					(or
						(not (= (x b2) (x b23)))
						(not (= (y b2) (y b23)))
					)
					(or
						(not (= (x b2) (x b24)))
						(not (= (y b2) (y b24)))
					)
					(or
						(not (= (x b2) (x b25)))
						(not (= (y b2) (y b25)))
					)
					(or
						(not (= (x b3) (x b4)))
						(not (= (y b3) (y b4)))
					)
					(or
						(not (= (x b3) (x b5)))
						(not (= (y b3) (y b5)))
					)
					(or
						(not (= (x b3) (x b6)))
						(not (= (y b3) (y b6)))
					)
				(= (x b3) (x b7))
				(= (y b3) (y b7))
					(or
						(not (= (x b3) (x b8)))
						(not (= (y b3) (y b8)))
					)
				(= (x b3) (x b9))
				(= (y b3) (y b9))
					(or
						(not (= (x b4) (x b5)))
						(not (= (y b4) (y b5)))
					)
				(= (x b4) (x b6))
				(= (y b4) (y b6))
					(or
						(not (= (x b4) (x b7)))
						(not (= (y b4) (y b7)))
					)
					(or
						(not (= (x b4) (x b8)))
						(not (= (y b4) (y b8)))
					)
					(or
						(not (= (x b4) (x b9)))
						(not (= (y b4) (y b9)))
					)
					(or
						(not (= (x b5) (x b6)))
						(not (= (y b5) (y b6)))
					)
					(or
						(not (= (x b5) (x b7)))
						(not (= (y b5) (y b7)))
					)
					(or
						(not (= (x b5) (x b8)))
						(not (= (y b5) (y b8)))
					)
					(or
						(not (= (x b5) (x b9)))
						(not (= (y b5) (y b9)))
					)
					(or
						(not (= (x b6) (x b7)))
						(not (= (y b6) (y b7)))
					)
					(or
						(not (= (x b6) (x b8)))
						(not (= (y b6) (y b8)))
					)
					(or
						(not (= (x b6) (x b9)))
						(not (= (y b6) (y b9)))
					)
					(or
						(not (= (x b7) (x b8)))
						(not (= (y b7) (y b8)))
					)
				(= (x b7) (x b9))
				(= (y b7) (y b9))
					(or
						(not (= (x b8) (x b9)))
						(not (= (y b8) (y b9)))
					)
					(or
						(not (= (x b10) (x b2)))
						(not (= (y b10) (y b2)))
					)
					(or
						(not (= (x b10) (x b3)))
						(not (= (y b10) (y b3)))
					)
				(= (x b10) (x b4))
				(= (y b10) (y b4))
					(or
						(not (= (x b10) (x b5)))
						(not (= (y b10) (y b5)))
					)
				(= (x b10) (x b6))
				(= (y b10) (y b6))
					(or
						(not (= (x b10) (x b7)))
						(not (= (y b10) (y b7)))
					)
					(or
						(not (= (x b10) (x b8)))
						(not (= (y b10) (y b8)))
					)
					(or
						(not (= (x b10) (x b9)))
						(not (= (y b10) (y b9)))
					)
				(= (x b10) (x b11))
				(= (y b10) (y b11))
					(or
						(not (= (x b10) (x b12)))
						(not (= (y b10) (y b12)))
					)
					(or
						(not (= (x b10) (x b13)))
						(not (= (y b10) (y b13)))
					)
					(or
						(not (= (x b10) (x b14)))
						(not (= (y b10) (y b14)))
					)
				(= (x b10) (x b15))
				(= (y b10) (y b15))
					(or
						(not (= (x b10) (x b16)))
						(not (= (y b10) (y b16)))
					)
					(or
						(not (= (x b10) (x b17)))
						(not (= (y b10) (y b17)))
					)
					(or
						(not (= (x b10) (x b18)))
						(not (= (y b10) (y b18)))
					)
					(or
						(not (= (x b10) (x b19)))
						(not (= (y b10) (y b19)))
					)
					(or
						(not (= (x b10) (x b20)))
						(not (= (y b10) (y b20)))
					)
					(or
						(not (= (x b10) (x b21)))
						(not (= (y b10) (y b21)))
					)
				(= (x b10) (x b22))
				(= (y b10) (y b22))
				(= (x b10) (x b23))
				(= (y b10) (y b23))
					(or
						(not (= (x b10) (x b24)))
						(not (= (y b10) (y b24)))
					)
					(or
						(not (= (x b10) (x b25)))
						(not (= (y b10) (y b25)))
					)
					(or
						(not (= (x b11) (x b2)))
						(not (= (y b11) (y b2)))
					)
					(or
						(not (= (x b11) (x b3)))
						(not (= (y b11) (y b3)))
					)
				(= (x b11) (x b4))
				(= (y b11) (y b4))
					(or
						(not (= (x b11) (x b5)))
						(not (= (y b11) (y b5)))
					)
				(= (x b11) (x b6))
				(= (y b11) (y b6))
					(or
						(not (= (x b11) (x b7)))
						(not (= (y b11) (y b7)))
					)
					(or
						(not (= (x b11) (x b8)))
						(not (= (y b11) (y b8)))
					)
					(or
						(not (= (x b11) (x b9)))
						(not (= (y b11) (y b9)))
					)
					(or
						(not (= (x b11) (x b12)))
						(not (= (y b11) (y b12)))
					)
					(or
						(not (= (x b11) (x b13)))
						(not (= (y b11) (y b13)))
					)
					(or
						(not (= (x b11) (x b14)))
						(not (= (y b11) (y b14)))
					)
				(= (x b11) (x b15))
				(= (y b11) (y b15))
					(or
						(not (= (x b11) (x b16)))
						(not (= (y b11) (y b16)))
					)
					(or
						(not (= (x b11) (x b17)))
						(not (= (y b11) (y b17)))
					)
					(or
						(not (= (x b11) (x b18)))
						(not (= (y b11) (y b18)))
					)
					(or
						(not (= (x b11) (x b19)))
						(not (= (y b11) (y b19)))
					)
					(or
						(not (= (x b11) (x b20)))
						(not (= (y b11) (y b20)))
					)
					(or
						(not (= (x b11) (x b21)))
						(not (= (y b11) (y b21)))
					)
				(= (x b11) (x b22))
				(= (y b11) (y b22))
				(= (x b11) (x b23))
				(= (y b11) (y b23))
					(or
						(not (= (x b11) (x b24)))
						(not (= (y b11) (y b24)))
					)
					(or
						(not (= (x b11) (x b25)))
						(not (= (y b11) (y b25)))
					)
				(= (x b12) (x b2))
				(= (y b12) (y b2))
					(or
						(not (= (x b12) (x b3)))
						(not (= (y b12) (y b3)))
					)
					(or
						(not (= (x b12) (x b4)))
						(not (= (y b12) (y b4)))
					)
					(or
						(not (= (x b12) (x b5)))
						(not (= (y b12) (y b5)))
					)
					(or
						(not (= (x b12) (x b6)))
						(not (= (y b12) (y b6)))
					)
					(or
						(not (= (x b12) (x b7)))
						(not (= (y b12) (y b7)))
					)
					(or
						(not (= (x b12) (x b8)))
						(not (= (y b12) (y b8)))
					)
					(or
						(not (= (x b12) (x b9)))
						(not (= (y b12) (y b9)))
					)
					(or
						(not (= (x b12) (x b13)))
						(not (= (y b12) (y b13)))
					)
					(or
						(not (= (x b12) (x b14)))
						(not (= (y b12) (y b14)))
					)
					(or
						(not (= (x b12) (x b15)))
						(not (= (y b12) (y b15)))
					)
					(or
						(not (= (x b12) (x b16)))
						(not (= (y b12) (y b16)))
					)
				(= (x b12) (x b17))
				(= (y b12) (y b17))
					(or
						(not (= (x b12) (x b18)))
						(not (= (y b12) (y b18)))
					)
					(or
						(not (= (x b12) (x b19)))
						(not (= (y b12) (y b19)))
					)
				(= (x b12) (x b20))
				(= (y b12) (y b20))
					(or
						(not (= (x b12) (x b21)))
						(not (= (y b12) (y b21)))
					)
					(or
						(not (= (x b12) (x b22)))
						(not (= (y b12) (y b22)))
					)
					(or
						(not (= (x b12) (x b23)))
						(not (= (y b12) (y b23)))
					)
					(or
						(not (= (x b12) (x b24)))
						(not (= (y b12) (y b24)))
					)
					(or
						(not (= (x b12) (x b25)))
						(not (= (y b12) (y b25)))
					)
					(or
						(not (= (x b13) (x b2)))
						(not (= (y b13) (y b2)))
					)
					(or
						(not (= (x b13) (x b3)))
						(not (= (y b13) (y b3)))
					)
					(or
						(not (= (x b13) (x b4)))
						(not (= (y b13) (y b4)))
					)
				(= (x b13) (x b5))
				(= (y b13) (y b5))
					(or
						(not (= (x b13) (x b6)))
						(not (= (y b13) (y b6)))
					)
					(or
						(not (= (x b13) (x b7)))
						(not (= (y b13) (y b7)))
					)
					(or
						(not (= (x b13) (x b8)))
						(not (= (y b13) (y b8)))
					)
					(or
						(not (= (x b13) (x b9)))
						(not (= (y b13) (y b9)))
					)
					(or
						(not (= (x b13) (x b14)))
						(not (= (y b13) (y b14)))
					)
					(or
						(not (= (x b13) (x b15)))
						(not (= (y b13) (y b15)))
					)
				(= (x b13) (x b16))
				(= (y b13) (y b16))
					(or
						(not (= (x b13) (x b17)))
						(not (= (y b13) (y b17)))
					)
					(or
						(not (= (x b13) (x b18)))
						(not (= (y b13) (y b18)))
					)
					(or
						(not (= (x b13) (x b19)))
						(not (= (y b13) (y b19)))
					)
					(or
						(not (= (x b13) (x b20)))
						(not (= (y b13) (y b20)))
					)
					(or
						(not (= (x b13) (x b21)))
						(not (= (y b13) (y b21)))
					)
					(or
						(not (= (x b13) (x b22)))
						(not (= (y b13) (y b22)))
					)
					(or
						(not (= (x b13) (x b23)))
						(not (= (y b13) (y b23)))
					)
					(or
						(not (= (x b13) (x b24)))
						(not (= (y b13) (y b24)))
					)
				(= (x b13) (x b25))
				(= (y b13) (y b25))
					(or
						(not (= (x b14) (x b2)))
						(not (= (y b14) (y b2)))
					)
					(or
						(not (= (x b14) (x b3)))
						(not (= (y b14) (y b3)))
					)
					(or
						(not (= (x b14) (x b4)))
						(not (= (y b14) (y b4)))
					)
					(or
						(not (= (x b14) (x b5)))
						(not (= (y b14) (y b5)))
					)
					(or
						(not (= (x b14) (x b6)))
						(not (= (y b14) (y b6)))
					)
					(or
						(not (= (x b14) (x b7)))
						(not (= (y b14) (y b7)))
					)
				(= (x b14) (x b8))
				(= (y b14) (y b8))
					(or
						(not (= (x b14) (x b9)))
						(not (= (y b14) (y b9)))
					)
					(or
						(not (= (x b14) (x b15)))
						(not (= (y b14) (y b15)))
					)
					(or
						(not (= (x b14) (x b16)))
						(not (= (y b14) (y b16)))
					)
					(or
						(not (= (x b14) (x b17)))
						(not (= (y b14) (y b17)))
					)
					(or
						(not (= (x b14) (x b18)))
						(not (= (y b14) (y b18)))
					)
					(or
						(not (= (x b14) (x b19)))
						(not (= (y b14) (y b19)))
					)
					(or
						(not (= (x b14) (x b20)))
						(not (= (y b14) (y b20)))
					)
					(or
						(not (= (x b14) (x b21)))
						(not (= (y b14) (y b21)))
					)
					(or
						(not (= (x b14) (x b22)))
						(not (= (y b14) (y b22)))
					)
					(or
						(not (= (x b14) (x b23)))
						(not (= (y b14) (y b23)))
					)
					(or
						(not (= (x b14) (x b24)))
						(not (= (y b14) (y b24)))
					)
					(or
						(not (= (x b14) (x b25)))
						(not (= (y b14) (y b25)))
					)
					(or
						(not (= (x b15) (x b2)))
						(not (= (y b15) (y b2)))
					)
					(or
						(not (= (x b15) (x b3)))
						(not (= (y b15) (y b3)))
					)
				(= (x b15) (x b4))
				(= (y b15) (y b4))
					(or
						(not (= (x b15) (x b5)))
						(not (= (y b15) (y b5)))
					)
				(= (x b15) (x b6))
				(= (y b15) (y b6))
					(or
						(not (= (x b15) (x b7)))
						(not (= (y b15) (y b7)))
					)
					(or
						(not (= (x b15) (x b8)))
						(not (= (y b15) (y b8)))
					)
					(or
						(not (= (x b15) (x b9)))
						(not (= (y b15) (y b9)))
					)
					(or
						(not (= (x b15) (x b16)))
						(not (= (y b15) (y b16)))
					)
					(or
						(not (= (x b15) (x b17)))
						(not (= (y b15) (y b17)))
					)
					(or
						(not (= (x b15) (x b18)))
						(not (= (y b15) (y b18)))
					)
					(or
						(not (= (x b15) (x b19)))
						(not (= (y b15) (y b19)))
					)
					(or
						(not (= (x b15) (x b20)))
						(not (= (y b15) (y b20)))
					)
					(or
						(not (= (x b15) (x b21)))
						(not (= (y b15) (y b21)))
					)
				(= (x b15) (x b22))
				(= (y b15) (y b22))
				(= (x b15) (x b23))
				(= (y b15) (y b23))
					(or
						(not (= (x b15) (x b24)))
						(not (= (y b15) (y b24)))
					)
					(or
						(not (= (x b15) (x b25)))
						(not (= (y b15) (y b25)))
					)
					(or
						(not (= (x b16) (x b2)))
						(not (= (y b16) (y b2)))
					)
					(or
						(not (= (x b16) (x b3)))
						(not (= (y b16) (y b3)))
					)
					(or
						(not (= (x b16) (x b4)))
						(not (= (y b16) (y b4)))
					)
				(= (x b16) (x b5))
				(= (y b16) (y b5))
					(or
						(not (= (x b16) (x b6)))
						(not (= (y b16) (y b6)))
					)
					(or
						(not (= (x b16) (x b7)))
						(not (= (y b16) (y b7)))
					)
					(or
						(not (= (x b16) (x b8)))
						(not (= (y b16) (y b8)))
					)
					(or
						(not (= (x b16) (x b9)))
						(not (= (y b16) (y b9)))
					)
					(or
						(not (= (x b16) (x b17)))
						(not (= (y b16) (y b17)))
					)
					(or
						(not (= (x b16) (x b18)))
						(not (= (y b16) (y b18)))
					)
					(or
						(not (= (x b16) (x b19)))
						(not (= (y b16) (y b19)))
					)
					(or
						(not (= (x b16) (x b20)))
						(not (= (y b16) (y b20)))
					)
					(or
						(not (= (x b16) (x b21)))
						(not (= (y b16) (y b21)))
					)
					(or
						(not (= (x b16) (x b22)))
						(not (= (y b16) (y b22)))
					)
					(or
						(not (= (x b16) (x b23)))
						(not (= (y b16) (y b23)))
					)
					(or
						(not (= (x b16) (x b24)))
						(not (= (y b16) (y b24)))
					)
				(= (x b16) (x b25))
				(= (y b16) (y b25))
				(= (x b17) (x b2))
				(= (y b17) (y b2))
					(or
						(not (= (x b17) (x b3)))
						(not (= (y b17) (y b3)))
					)
					(or
						(not (= (x b17) (x b4)))
						(not (= (y b17) (y b4)))
					)
					(or
						(not (= (x b17) (x b5)))
						(not (= (y b17) (y b5)))
					)
					(or
						(not (= (x b17) (x b6)))
						(not (= (y b17) (y b6)))
					)
					(or
						(not (= (x b17) (x b7)))
						(not (= (y b17) (y b7)))
					)
					(or
						(not (= (x b17) (x b8)))
						(not (= (y b17) (y b8)))
					)
					(or
						(not (= (x b17) (x b9)))
						(not (= (y b17) (y b9)))
					)
					(or
						(not (= (x b17) (x b18)))
						(not (= (y b17) (y b18)))
					)
					(or
						(not (= (x b17) (x b19)))
						(not (= (y b17) (y b19)))
					)
				(= (x b17) (x b20))
				(= (y b17) (y b20))
					(or
						(not (= (x b17) (x b21)))
						(not (= (y b17) (y b21)))
					)
					(or
						(not (= (x b17) (x b22)))
						(not (= (y b17) (y b22)))
					)
					(or
						(not (= (x b17) (x b23)))
						(not (= (y b17) (y b23)))
					)
					(or
						(not (= (x b17) (x b24)))
						(not (= (y b17) (y b24)))
					)
					(or
						(not (= (x b17) (x b25)))
						(not (= (y b17) (y b25)))
					)
					(or
						(not (= (x b18) (x b2)))
						(not (= (y b18) (y b2)))
					)
					(or
						(not (= (x b18) (x b3)))
						(not (= (y b18) (y b3)))
					)
					(or
						(not (= (x b18) (x b4)))
						(not (= (y b18) (y b4)))
					)
					(or
						(not (= (x b18) (x b5)))
						(not (= (y b18) (y b5)))
					)
					(or
						(not (= (x b18) (x b6)))
						(not (= (y b18) (y b6)))
					)
					(or
						(not (= (x b18) (x b7)))
						(not (= (y b18) (y b7)))
					)
					(or
						(not (= (x b18) (x b8)))
						(not (= (y b18) (y b8)))
					)
					(or
						(not (= (x b18) (x b9)))
						(not (= (y b18) (y b9)))
					)
				(= (x b18) (x b19))
				(= (y b18) (y b19))
					(or
						(not (= (x b18) (x b20)))
						(not (= (y b18) (y b20)))
					)
					(or
						(not (= (x b18) (x b21)))
						(not (= (y b18) (y b21)))
					)
					(or
						(not (= (x b18) (x b22)))
						(not (= (y b18) (y b22)))
					)
					(or
						(not (= (x b18) (x b23)))
						(not (= (y b18) (y b23)))
					)
				(= (x b18) (x b24))
				(= (y b18) (y b24))
					(or
						(not (= (x b18) (x b25)))
						(not (= (y b18) (y b25)))
					)
					(or
						(not (= (x b19) (x b2)))
						(not (= (y b19) (y b2)))
					)
					(or
						(not (= (x b19) (x b3)))
						(not (= (y b19) (y b3)))
					)
					(or
						(not (= (x b19) (x b4)))
						(not (= (y b19) (y b4)))
					)
					(or
						(not (= (x b19) (x b5)))
						(not (= (y b19) (y b5)))
					)
					(or
						(not (= (x b19) (x b6)))
						(not (= (y b19) (y b6)))
					)
					(or
						(not (= (x b19) (x b7)))
						(not (= (y b19) (y b7)))
					)
					(or
						(not (= (x b19) (x b8)))
						(not (= (y b19) (y b8)))
					)
					(or
						(not (= (x b19) (x b9)))
						(not (= (y b19) (y b9)))
					)
					(or
						(not (= (x b19) (x b20)))
						(not (= (y b19) (y b20)))
					)
					(or
						(not (= (x b19) (x b21)))
						(not (= (y b19) (y b21)))
					)
					(or
						(not (= (x b19) (x b22)))
						(not (= (y b19) (y b22)))
					)
					(or
						(not (= (x b19) (x b23)))
						(not (= (y b19) (y b23)))
					)
				(= (x b19) (x b24))
				(= (y b19) (y b24))
					(or
						(not (= (x b19) (x b25)))
						(not (= (y b19) (y b25)))
					)
					(or
						(not (= (x b20) (x b3)))
						(not (= (y b20) (y b3)))
					)
					(or
						(not (= (x b20) (x b4)))
						(not (= (y b20) (y b4)))
					)
					(or
						(not (= (x b20) (x b5)))
						(not (= (y b20) (y b5)))
					)
					(or
						(not (= (x b20) (x b6)))
						(not (= (y b20) (y b6)))
					)
					(or
						(not (= (x b20) (x b7)))
						(not (= (y b20) (y b7)))
					)
					(or
						(not (= (x b20) (x b8)))
						(not (= (y b20) (y b8)))
					)
					(or
						(not (= (x b20) (x b9)))
						(not (= (y b20) (y b9)))
					)
					(or
						(not (= (x b20) (x b21)))
						(not (= (y b20) (y b21)))
					)
					(or
						(not (= (x b20) (x b22)))
						(not (= (y b20) (y b22)))
					)
					(or
						(not (= (x b20) (x b23)))
						(not (= (y b20) (y b23)))
					)
					(or
						(not (= (x b20) (x b24)))
						(not (= (y b20) (y b24)))
					)
					(or
						(not (= (x b20) (x b25)))
						(not (= (y b20) (y b25)))
					)
				(= (x b21) (x b3))
				(= (y b21) (y b3))
					(or
						(not (= (x b21) (x b4)))
						(not (= (y b21) (y b4)))
					)
					(or
						(not (= (x b21) (x b5)))
						(not (= (y b21) (y b5)))
					)
					(or
						(not (= (x b21) (x b6)))
						(not (= (y b21) (y b6)))
					)
				(= (x b21) (x b7))
				(= (y b21) (y b7))
					(or
						(not (= (x b21) (x b8)))
						(not (= (y b21) (y b8)))
					)
				(= (x b21) (x b9))
				(= (y b21) (y b9))
					(or
						(not (= (x b21) (x b22)))
						(not (= (y b21) (y b22)))
					)
					(or
						(not (= (x b21) (x b23)))
						(not (= (y b21) (y b23)))
					)
					(or
						(not (= (x b21) (x b24)))
						(not (= (y b21) (y b24)))
					)
					(or
						(not (= (x b21) (x b25)))
						(not (= (y b21) (y b25)))
					)
					(or
						(not (= (x b22) (x b3)))
						(not (= (y b22) (y b3)))
					)
				(= (x b22) (x b4))
				(= (y b22) (y b4))
					(or
						(not (= (x b22) (x b5)))
						(not (= (y b22) (y b5)))
					)
				(= (x b22) (x b6))
				(= (y b22) (y b6))
					(or
						(not (= (x b22) (x b7)))
						(not (= (y b22) (y b7)))
					)
					(or
						(not (= (x b22) (x b8)))
						(not (= (y b22) (y b8)))
					)
					(or
						(not (= (x b22) (x b9)))
						(not (= (y b22) (y b9)))
					)
				(= (x b22) (x b23))
				(= (y b22) (y b23))
					(or
						(not (= (x b22) (x b24)))
						(not (= (y b22) (y b24)))
					)
					(or
						(not (= (x b22) (x b25)))
						(not (= (y b22) (y b25)))
					)
					(or
						(not (= (x b23) (x b3)))
						(not (= (y b23) (y b3)))
					)
				(= (x b23) (x b4))
				(= (y b23) (y b4))
					(or
						(not (= (x b23) (x b5)))
						(not (= (y b23) (y b5)))
					)
				(= (x b23) (x b6))
				(= (y b23) (y b6))
					(or
						(not (= (x b23) (x b7)))
						(not (= (y b23) (y b7)))
					)
					(or
						(not (= (x b23) (x b8)))
						(not (= (y b23) (y b8)))
					)
					(or
						(not (= (x b23) (x b9)))
						(not (= (y b23) (y b9)))
					)
					(or
						(not (= (x b23) (x b24)))
						(not (= (y b23) (y b24)))
					)
					(or
						(not (= (x b23) (x b25)))
						(not (= (y b23) (y b25)))
					)
					(or
						(not (= (x b24) (x b3)))
						(not (= (y b24) (y b3)))
					)
					(or
						(not (= (x b24) (x b4)))
						(not (= (y b24) (y b4)))
					)
					(or
						(not (= (x b24) (x b5)))
						(not (= (y b24) (y b5)))
					)
					(or
						(not (= (x b24) (x b6)))
						(not (= (y b24) (y b6)))
					)
					(or
						(not (= (x b24) (x b7)))
						(not (= (y b24) (y b7)))
					)
					(or
						(not (= (x b24) (x b8)))
						(not (= (y b24) (y b8)))
					)
					(or
						(not (= (x b24) (x b9)))
						(not (= (y b24) (y b9)))
					)
					(or
						(not (= (x b24) (x b25)))
						(not (= (y b24) (y b25)))
					)
					(or
						(not (= (x b25) (x b3)))
						(not (= (y b25) (y b3)))
					)
					(or
						(not (= (x b25) (x b4)))
						(not (= (y b25) (y b4)))
					)
				(= (x b25) (x b5))
				(= (y b25) (y b5))
					(or
						(not (= (x b25) (x b6)))
						(not (= (y b25) (y b6)))
					)
					(or
						(not (= (x b25) (x b7)))
						(not (= (y b25) (y b7)))
					)
					(or
						(not (= (x b25) (x b8)))
						(not (= (y b25) (y b8)))
					)
					(or
						(not (= (x b25) (x b9)))
						(not (= (y b25) (y b9)))
					)
			)
	)
)