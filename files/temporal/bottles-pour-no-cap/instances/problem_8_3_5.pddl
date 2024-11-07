(define (problem prob_8_3_5)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 r2 r3 r4 r5 - bottleright
	)
	(:init
		(= (litres l1) 8)
		(= (litres l2) 9)
		(= (litres l3) 7)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
	)
	(:goal
		(and
			(= (litres r1) 1)
			(= (litres r2) 1)
			(= (litres r3) 3)
			(= (litres r4) 16)
			(= (litres r5) 3)
		)
	)
)