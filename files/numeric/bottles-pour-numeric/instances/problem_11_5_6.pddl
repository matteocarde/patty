(define (problem prob_11_5_6)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 - bottleleft
		 r1 r2 r3 r4 r5 r6 - bottleright
	)
	(:init
		(= (litres l1) 3)
		(= (litres l2) 23)
		(= (litres l3) 2)
		(= (litres l4) 2)
		(= (litres l5) 3)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
		(= (litres r6) 0)
	)
	(:goal
		(and
			(= (litres r1) 5)
			(= (litres r2) 3)
			(= (litres r3) 14)
			(= (litres r4) 1)
			(= (litres r5) 5)
			(= (litres r6) 5)
		)
	)
)