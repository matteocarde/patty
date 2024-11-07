(define (problem prob_13_7_6)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 - bottleleft
		 r1 r2 r3 r4 r5 r6 - bottleright
	)
	(:init
		(= (litres l1) 1)
		(= (litres l2) 1)
		(= (litres l3) 5)
		(= (litres l4) 2)
		(= (litres l5) 26)
		(= (litres l6) 1)
		(= (litres l7) 3)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
		(= (litres r6) 0)
	)
	(:goal
		(and
			(= (litres r1) 5)
			(= (litres r2) 6)
			(= (litres r3) 19)
			(= (litres r4) 4)
			(= (litres r5) 1)
			(= (litres r6) 4)
		)
	)
)