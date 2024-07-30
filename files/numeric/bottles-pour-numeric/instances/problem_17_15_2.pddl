(define (problem prob_17_15_2)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 l12 l13 l14 l15 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 3)
		(= (litres l2) 1)
		(= (litres l3) 2)
		(= (litres l4) 3)
		(= (litres l5) 2)
		(= (litres l6) 2)
		(= (litres l7) 3)
		(= (litres l8) 3)
		(= (litres l9) 2)
		(= (litres l10) 1)
		(= (litres l11) 2)
		(= (litres l12) 3)
		(= (litres l13) 2)
		(= (litres l14) 21)
		(= (litres l15) 1)
		(= (litres r1) 0)
		(= (litres r2) 0)
	)
	(:goal
		(and
			(= (litres r1) 38)
			(= (litres r2) 13)
		)
	)
)