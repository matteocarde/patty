(define (problem prob_15_13_2)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 l12 l13 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 1)
		(= (litres l2) 23)
		(= (litres l3) 1)
		(= (litres l4) 1)
		(= (litres l5) 3)
		(= (litres l6) 3)
		(= (litres l7) 1)
		(= (litres l8) 3)
		(= (litres l9) 2)
		(= (litres l10) 3)
		(= (litres l11) 1)
		(= (litres l12) 1)
		(= (litres l13) 2)
		(= (litres r1) 0)
		(= (litres r2) 0)
	)
	(:goal
		(and
			(= (litres r1) 10)
			(= (litres r2) 35)
		)
	)
)