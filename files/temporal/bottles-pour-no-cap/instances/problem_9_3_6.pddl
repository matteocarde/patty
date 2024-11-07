(define (problem prob_9_3_6)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 r2 r3 r4 r5 r6 - bottleright
	)
	(:init
		(= (litres l1) 15)
		(= (litres l2) 5)
		(= (litres l3) 7)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
		(= (litres r6) 0)
	)
	(:goal
		(and
			(= (litres r1) 4)
			(= (litres r2) 15)
			(= (litres r3) 2)
			(= (litres r4) 1)
			(= (litres r5) 4)
			(= (litres r6) 1)
		)
	)
)