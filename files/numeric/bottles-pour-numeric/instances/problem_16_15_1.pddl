(define (problem prob_16_15_1)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 l12 l13 l14 l15 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (litres l1) 3)
		(= (litres l2) 15)
		(= (litres l3) 2)
		(= (litres l4) 3)
		(= (litres l5) 1)
		(= (litres l6) 3)
		(= (litres l7) 1)
		(= (litres l8) 3)
		(= (litres l9) 2)
		(= (litres l10) 3)
		(= (litres l11) 1)
		(= (litres l12) 2)
		(= (litres l13) 3)
		(= (litres l14) 3)
		(= (litres l15) 3)
		(= (litres r1) 0)
	)
	(:goal
		(and
			(= (litres r1) 48)
		)
	)
)