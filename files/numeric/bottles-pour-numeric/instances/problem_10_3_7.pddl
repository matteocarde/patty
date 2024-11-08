(define (problem prob_10_3_7)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 r2 r3 r4 r5 r6 r7 - bottleright
	)
	(:init
		(= (litres l1) 6)
		(= (litres l2) 20)
		(= (litres l3) 4)
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
			(= (litres r1) 16)
			(= (litres r2) 4)
			(= (litres r3) 3)
			(= (litres r4) 3)
			(= (litres r5) 1)
			(= (litres r6) 2)
			(= (litres r7) 1)
		)
	)
)