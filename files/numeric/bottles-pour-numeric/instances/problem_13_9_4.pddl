(define (problem prob_13_9_4)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 - bottleleft
		 r1 r2 r3 r4 - bottleright
	)
	(:init
		(= (litres l1) 3)
		(= (litres l2) 18)
		(= (litres l3) 4)
		(= (litres l4) 3)
		(= (litres l5) 3)
		(= (litres l6) 2)
		(= (litres l7) 1)
		(= (litres l8) 3)
		(= (litres l9) 2)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
	)
	(:goal
		(and
			(= (litres r1) 6)
			(= (litres r2) 6)
			(= (litres r3) 6)
			(= (litres r4) 21)
		)
	)
)