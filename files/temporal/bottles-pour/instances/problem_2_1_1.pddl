(define (problem prob_2_1_1)
(:domain bottles)
	(:objects
		 l1 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (litres l1) 10)
		(= (litres r1) 0)
		(capped l1)
		(capped r1)
	)
	(:goal
		(and
			(= (litres r1) 10)
		)
	)
)