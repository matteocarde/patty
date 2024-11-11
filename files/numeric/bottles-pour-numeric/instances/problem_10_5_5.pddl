(define (problem prob_10_5_5)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 - bottleleft
		 r1 r2 r3 r4 r5 - bottleright
	)
	(:init
		(= (litres l1) 1)
		(= (litres l2) 15)
		(= (litres l3) 5)
		(= (litres l4) 5)
		(= (litres l5) 4)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
	)
	(:goal
		(and
			(= (litres r1) 6)
			(= (litres r2) 3)
			(= (litres r3) 6)
			(= (litres r4) 2)
			(= (litres r5) 13)
		)
	)
)