(define (problem prob_5_1_4)
(:domain bottles)
	(:objects
		 l1 - bottleleft
		 r1 r2 r3 r4 - bottleright
	)
	(:init
		(= (litres l1) 15)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
	)
	(:goal
		(and
			(= (litres r1) 1)
			(= (litres r2) 2)
			(= (litres r3) 9)
			(= (litres r4) 3)
		)
	)
)