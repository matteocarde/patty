(define (problem prob_16_13_3)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 l12 l13 - bottleleft
		 r1 r2 r3 - bottleright
	)
	(:init
		(= (litres l1) 1)
		(= (litres l2) 1)
		(= (litres l3) 2)
		(= (litres l4) 24)
		(= (litres l5) 2)
		(= (litres l6) 3)
		(= (litres l7) 3)
		(= (litres l8) 1)
		(= (litres l9) 1)
		(= (litres l10) 1)
		(= (litres l11) 3)
		(= (litres l12) 3)
		(= (litres l13) 3)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
	)
	(:goal
		(and
			(= (litres r1) 27)
			(= (litres r2) 16)
			(= (litres r3) 5)
		)
	)
)