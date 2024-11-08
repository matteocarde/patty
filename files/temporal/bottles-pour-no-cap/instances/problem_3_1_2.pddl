(define (problem prob_3_1_2)
(:domain bottles)
	(:objects
		 l1 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 9)
		(= (litres r1) 0)
		(= (litres r2) 0)
	)
	(:goal
		(and
			(= (litres r1) 2)
			(= (litres r2) 7)
		)
	)
)