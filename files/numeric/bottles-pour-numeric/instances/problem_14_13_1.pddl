(define (problem prob_14_13_1)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 l12 l13 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (litres l1) 15)
		(= (litres l2) 3)
		(= (litres l3) 3)
		(= (litres l4) 3)
		(= (litres l5) 3)
		(= (litres l6) 2)
		(= (litres l7) 1)
		(= (litres l8) 3)
		(= (litres l9) 2)
		(= (litres l10) 1)
		(= (litres l11) 1)
		(= (litres l12) 3)
		(= (litres l13) 2)
		(= (litres r1) 0)
	)
	(:goal
		(and
			(= (litres r1) 42)
		)
	)
)