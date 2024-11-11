(define (problem prob_14_9_5)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 - bottleleft
		 r1 r2 r3 r4 r5 - bottleright
	)
	(:init
		(= (litres l1) 1)
		(= (litres l2) 3)
		(= (litres l3) 3)
		(= (litres l4) 3)
		(= (litres l5) 2)
		(= (litres l6) 3)
		(= (litres l7) 22)
		(= (litres l8) 2)
		(= (litres l9) 3)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
	)
	(:goal
		(and
			(= (litres r1) 5)
			(= (litres r2) 6)
			(= (litres r3) 2)
			(= (litres r4) 21)
			(= (litres r5) 8)
		)
	)
)