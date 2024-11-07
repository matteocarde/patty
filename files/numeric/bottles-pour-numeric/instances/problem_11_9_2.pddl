(define (problem prob_11_9_2)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 3)
		(= (litres l2) 2)
		(= (litres l3) 2)
		(= (litres l4) 3)
		(= (litres l5) 16)
		(= (litres l6) 3)
		(= (litres l7) 1)
		(= (litres l8) 2)
		(= (litres l9) 1)
		(= (litres r1) 0)
		(= (litres r2) 0)
	)
	(:goal
		(and
			(= (litres r1) 11)
			(= (litres r2) 22)
		)
	)
)