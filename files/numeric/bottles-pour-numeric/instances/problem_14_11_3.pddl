(define (problem prob_14_11_3)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 - bottleleft
		 r1 r2 r3 - bottleright
	)
	(:init
		(= (litres l1) 27)
		(= (litres l2) 2)
		(= (litres l3) 2)
		(= (litres l4) 1)
		(= (litres l5) 1)
		(= (litres l6) 3)
		(= (litres l7) 1)
		(= (litres l8) 1)
		(= (litres l9) 1)
		(= (litres l10) 1)
		(= (litres l11) 2)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
	)
	(:goal
		(and
			(= (litres r1) 8)
			(= (litres r2) 26)
			(= (litres r3) 8)
		)
	)
)