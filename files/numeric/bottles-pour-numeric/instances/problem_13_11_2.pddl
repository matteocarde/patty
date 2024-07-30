(define (problem prob_13_11_2)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 2)
		(= (litres l2) 3)
		(= (litres l3) 1)
		(= (litres l4) 3)
		(= (litres l5) 2)
		(= (litres l6) 1)
		(= (litres l7) 3)
		(= (litres l8) 1)
		(= (litres l9) 3)
		(= (litres l10) 3)
		(= (litres l11) 17)
		(= (litres r1) 0)
		(= (litres r2) 0)
	)
	(:goal
		(and
			(= (litres r1) 9)
			(= (litres r2) 30)
		)
	)
)