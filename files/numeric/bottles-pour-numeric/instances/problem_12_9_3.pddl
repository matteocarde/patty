(define (problem prob_12_9_3)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 - bottleleft
		 r1 r2 r3 - bottleright
	)
	(:init
		(= (litres l1) 3)
		(= (litres l2) 2)
		(= (litres l3) 3)
		(= (litres l4) 4)
		(= (litres l5) 3)
		(= (litres l6) 15)
		(= (litres l7) 3)
		(= (litres l8) 2)
		(= (litres l9) 1)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
	)
	(:goal
		(and
			(= (litres r1) 28)
			(= (litres r2) 3)
			(= (litres r3) 5)
		)
	)
)