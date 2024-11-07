(define (problem prob_12_11_1)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (litres l1) 1)
		(= (litres l2) 1)
		(= (litres l3) 3)
		(= (litres l4) 1)
		(= (litres l5) 1)
		(= (litres l6) 2)
		(= (litres l7) 1)
		(= (litres l8) 1)
		(= (litres l9) 1)
		(= (litres l10) 21)
		(= (litres l11) 3)
		(= (litres r1) 0)
	)
	(:goal
		(and
			(= (litres r1) 36)
		)
	)
)