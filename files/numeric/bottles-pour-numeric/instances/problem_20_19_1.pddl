(define (problem prob_20_19_1)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 l12 l13 l14 l15 l16 l17 l18 l19 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (litres l1) 2)
		(= (litres l2) 2)
		(= (litres l3) 3)
		(= (litres l4) 1)
		(= (litres l5) 1)
		(= (litres l6) 2)
		(= (litres l7) 1)
		(= (litres l8) 3)
		(= (litres l9) 3)
		(= (litres l10) 3)
		(= (litres l11) 3)
		(= (litres l12) 3)
		(= (litres l13) 2)
		(= (litres l14) 2)
		(= (litres l15) 2)
		(= (litres l16) 3)
		(= (litres l17) 19)
		(= (litres l18) 3)
		(= (litres l19) 2)
		(= (litres r1) 0)
	)
	(:goal
		(and
			(= (litres r1) 60)
		)
	)
)