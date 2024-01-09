(define (problem prob_4_1_3)
(:domain bottles)
	(:objects
		 l1 - bottleleft
		 r1 r2 r3 - bottleright
	)
	(:init
		(= (litres l1) 20)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(capped l1)
		(capped r1)
		(capped r2)
		(capped r3)
	)
	(:goal
		(and
			(= (litres r1) 15)
			(= (litres r2) 2)
			(= (litres r3) 3)
		)
	)
)