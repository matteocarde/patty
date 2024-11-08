(define (problem prob_6_3_3)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 r2 r3 - bottleright
	)
	(:init
		(= (litres l1) 3)
		(= (litres l2) 11)
		(= (litres l3) 4)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
	)
	(:goal
		(and
			(= (litres r1) 6)
			(= (litres r2) 8)
			(= (litres r3) 4)
		)
	)
)