(define (problem prob_7_1_6)
(:domain bottles)
	(:objects
		 l1 - bottleleft
		 r1 r2  - bottleright
	)
	(:init
		(= (litres l1) 6)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(capped l1)
		(capped r1)
		(capped r2)
	)
	(:goal
		(and
			(= (litres r1) 1)
			(= (litres r2) 1)
		)
	)
)