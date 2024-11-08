(define (problem prob_7_5_2)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 11)
		(= (litres l2) 2)
		(= (litres l3) 3)
		(= (litres l4) 2)
		(= (litres l5) 3)
		(= (litres r1) 0)
		(= (litres r2) 0)
	)
	(:goal
		(and
			(= (litres r1) 16)
			(= (litres r2) 5)
		)
	)
)