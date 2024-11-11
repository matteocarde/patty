(define (problem prob_10_7_3)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 - bottleleft
		 r1 r2 r3 - bottleright
	)
	(:init
		(= (litres l1) 14)
		(= (litres l2) 4)
		(= (litres l3) 4)
		(= (litres l4) 2)
		(= (litres l5) 1)
		(= (litres l6) 3)
		(= (litres l7) 2)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
	)
	(:goal
		(and
			(= (litres r1) 7)
			(= (litres r2) 2)
			(= (litres r3) 21)
		)
	)
)