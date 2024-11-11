(define (problem prob_8_3_5)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 r2 r3 r4 r5 - bottleright
	)
	(:init
		(= (litres l1) 2)
		(= (litres l2) 8)
		(= (litres l3) 14)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
	)
	(:goal
		(and
			(= (litres r1) 4)
			(= (litres r2) 15)
			(= (litres r3) 2)
			(= (litres r4) 1)
			(= (litres r5) 2)
		)
	)
)