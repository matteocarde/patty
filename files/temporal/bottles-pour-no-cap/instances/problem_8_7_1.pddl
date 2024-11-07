(define (problem prob_8_7_1)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (litres l1) 3)
		(= (litres l2) 3)
		(= (litres l3) 1)
		(= (litres l4) 13)
		(= (litres l5) 2)
		(= (litres l6) 1)
		(= (litres l7) 1)
		(= (litres r1) 0)
	)
	(:goal
		(and
			(= (litres r1) 24)
		)
	)
)