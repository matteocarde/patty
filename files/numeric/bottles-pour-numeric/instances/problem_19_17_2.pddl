(define (problem prob_19_17_2)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 l12 l13 l14 l15 l16 l17 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 1)
		(= (litres l2) 2)
		(= (litres l3) 3)
		(= (litres l4) 3)
		(= (litres l5) 3)
		(= (litres l6) 2)
		(= (litres l7) 1)
		(= (litres l8) 1)
		(= (litres l9) 1)
		(= (litres l10) 3)
		(= (litres l11) 2)
		(= (litres l12) 2)
		(= (litres l13) 23)
		(= (litres l14) 3)
		(= (litres l15) 2)
		(= (litres l16) 2)
		(= (litres l17) 3)
		(= (litres r1) 0)
		(= (litres r2) 0)
	)
	(:goal
		(and
			(= (litres r1) 44)
			(= (litres r2) 13)
		)
	)
)