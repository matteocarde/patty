(define (problem prob_14_7_7)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 - bottleleft
		 r1 r2 r3 r4 r5 r6 r7 - bottleright
	)
	(:init
		(= (litres l1) 5)
		(= (litres l2) 4)
		(= (litres l3) 1)
		(= (litres l4) 27)
		(= (litres l5) 1)
		(= (litres l6) 1)
		(= (litres l7) 3)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
		(= (litres r6) 0)
		(= (litres r7) 0)
	)
	(:goal
		(and
			(= (litres r1) 3)
			(= (litres r2) 6)
			(= (litres r3) 4)
			(= (litres r4) 15)
			(= (litres r5) 6)
			(= (litres r6) 3)
			(= (litres r7) 5)
		)
	)
)