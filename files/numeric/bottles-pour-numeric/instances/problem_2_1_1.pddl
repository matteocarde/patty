(define (problem prob_2_1_1)
(:domain bottles)
	(:objects
		 l1 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (litres l1) 6)
		(= (litres r1) 0)
	)
	(:goal
		(and
			(= (litres r1) 6)
		)
	)
)