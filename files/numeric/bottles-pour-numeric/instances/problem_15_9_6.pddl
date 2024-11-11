(define (problem prob_15_9_6)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 - bottleleft
		 r1 r2 r3 r4 r5 r6 - bottleright
	)
	(:init
		(= (litres l1) 5)
		(= (litres l2) 5)
		(= (litres l3) 3)
		(= (litres l4) 4)
		(= (litres l5) 21)
		(= (litres l6) 1)
		(= (litres l7) 3)
		(= (litres l8) 1)
		(= (litres l9) 2)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
		(= (litres r6) 0)
	)
	(:goal
		(and
			(= (litres r1) 7)
			(= (litres r2) 5)
			(= (litres r3) 6)
			(= (litres r4) 3)
			(= (litres r5) 18)
			(= (litres r6) 6)
		)
	)
)