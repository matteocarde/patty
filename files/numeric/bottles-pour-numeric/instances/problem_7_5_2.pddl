(define (problem prob_7_5_2)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 1)
		(= (litres l2) 1)
		(= (litres l3) 1)
		(= (litres l4) 2)
		(= (litres l5) 16)
		(= (litres r1) 0)
		(= (litres r2) 0)
	)
	(:goal
		(and
			(= (litres r1) 12)
			(= (litres r2) 9)
		)
	)
)