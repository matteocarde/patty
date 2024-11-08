(define (problem prob_8_7_1)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (litres l1) 10)
		(= (litres l2) 1)
		(= (litres l3) 3)
		(= (litres l4) 3)
		(= (litres l5) 2)
		(= (litres l6) 2)
		(= (litres l7) 3)
		(= (litres r1) 0)
	)
	(:goal
		(and
			(= (litres r1) 24)
		)
	)
)