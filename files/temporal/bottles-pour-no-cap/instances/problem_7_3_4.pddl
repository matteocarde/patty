(define (problem prob_7_3_4)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 r2 r3 r4 - bottleright
	)
	(:init
		(= (litres l1) 5)
		(= (litres l2) 14)
		(= (litres l3) 2)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
	)
	(:goal
		(and
			(= (litres r1) 14)
			(= (litres r2) 2)
			(= (litres r3) 2)
			(= (litres r4) 3)
		)
	)
)