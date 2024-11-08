(define (problem prob_5_3_2)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 10)
		(= (litres l2) 3)
		(= (litres l3) 2)
		(= (litres r1) 0)
		(= (litres r2) 0)
	)
	(:goal
		(and
			(= (litres r1) 6)
			(= (litres r2) 9)
		)
	)
)