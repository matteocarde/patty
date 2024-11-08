(define (problem prob_16_11_5)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 - bottleleft
		 r1 r2 r3 r4 r5 - bottleright
	)
	(:init
		(= (litres l1) 1)
		(= (litres l2) 2)
		(= (litres l3) 1)
		(= (litres l4) 2)
		(= (litres l5) 2)
		(= (litres l6) 3)
		(= (litres l7) 2)
		(= (litres l8) 4)
		(= (litres l9) 4)
		(= (litres l10) 3)
		(= (litres l11) 24)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
	)
	(:goal
		(and
			(= (litres r1) 39)
			(= (litres r2) 1)
			(= (litres r3) 1)
			(= (litres r4) 2)
			(= (litres r5) 5)
		)
	)
)