(define (problem prob_2_1_1)
(:domain bottles)
	(:objects
		 l1 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (x l1) 0)
		(= (x r1) 0)
		(= (litres l1) 6)
		(= (litres r1) 0)
		(capped l1)
		(capped r1)
	)
	(:goal
		(and
			(= (litres r1) 6)
		)
	)
)