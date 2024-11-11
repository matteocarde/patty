(define (problem prob_18_15_3)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 l12 l13 l14 l15 - bottleleft
		 r1 r2 r3 - bottleright
	)
	(:init
		(= (litres l1) 1)
		(= (litres l2) 3)
		(= (litres l3) 24)
		(= (litres l4) 2)
		(= (litres l5) 2)
		(= (litres l6) 3)
		(= (litres l7) 2)
		(= (litres l8) 2)
		(= (litres l9) 3)
		(= (litres l10) 1)
		(= (litres l11) 2)
		(= (litres l12) 2)
		(= (litres l13) 3)
		(= (litres l14) 2)
		(= (litres l15) 2)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
	)
	(:goal
		(and
			(= (litres r1) 1)
			(= (litres r2) 2)
			(= (litres r3) 51)
		)
	)
)