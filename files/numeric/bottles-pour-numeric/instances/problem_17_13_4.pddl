(define (problem prob_17_13_4)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 l12 l13 - bottleleft
		 r1 r2 r3 r4 - bottleright
	)
	(:init
		(= (litres l1) 2)
		(= (litres l2) 1)
		(= (litres l3) 1)
		(= (litres l4) 3)
		(= (litres l5) 3)
		(= (litres l6) 1)
		(= (litres l7) 3)
		(= (litres l8) 3)
		(= (litres l9) 1)
		(= (litres l10) 2)
		(= (litres l11) 29)
		(= (litres l12) 1)
		(= (litres l13) 1)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
	)
	(:goal
		(and
			(= (litres r1) 39)
			(= (litres r2) 4)
			(= (litres r3) 1)
			(= (litres r4) 7)
		)
	)
)