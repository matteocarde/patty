(define (problem prob_15_11_4)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 - bottleleft
		 r1 r2 r3 r4 - bottleright
	)
	(:init
		(= (litres l1) 4)
		(= (litres l2) 3)
		(= (litres l3) 1)
		(= (litres l4) 3)
		(= (litres l5) 3)
		(= (litres l6) 2)
		(= (litres l7) 19)
		(= (litres l8) 4)
		(= (litres l9) 3)
		(= (litres l10) 2)
		(= (litres l11) 1)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
	)
	(:goal
		(and
			(= (litres r1) 26)
			(= (litres r2) 7)
			(= (litres r3) 8)
			(= (litres r4) 4)
		)
	)
)