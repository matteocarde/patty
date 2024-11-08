(define (problem prob_18_17_1)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 l12 l13 l14 l15 l16 l17 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (litres l1) 3)
		(= (litres l2) 2)
		(= (litres l3) 2)
		(= (litres l4) 2)
		(= (litres l5) 3)
		(= (litres l6) 19)
		(= (litres l7) 3)
		(= (litres l8) 2)
		(= (litres l9) 3)
		(= (litres l10) 1)
		(= (litres l11) 3)
		(= (litres l12) 1)
		(= (litres l13) 1)
		(= (litres l14) 1)
		(= (litres l15) 3)
		(= (litres l16) 2)
		(= (litres l17) 3)
		(= (litres r1) 0)
	)
	(:goal
		(and
			(= (litres r1) 54)
		)
	)
)