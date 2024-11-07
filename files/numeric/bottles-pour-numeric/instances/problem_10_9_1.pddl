(define (problem prob_10_9_1)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (litres l1) 3)
		(= (litres l2) 3)
		(= (litres l3) 1)
		(= (litres l4) 3)
		(= (litres l5) 12)
		(= (litres l6) 2)
		(= (litres l7) 2)
		(= (litres l8) 1)
		(= (litres l9) 3)
		(= (litres r1) 0)
	)
	(:goal
		(and
			(= (litres r1) 30)
		)
	)
)