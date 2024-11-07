(define (problem prob_9_3_6)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 r2 r3 r4 r5 r6 - bottleright
	)
	(:init
		(= (litres l1) 25)
		(= (litres l2) 1)
		(= (litres l3) 1)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
		(= (litres r6) 0)
	)
	(:goal
		(and
			(= (litres r1) 3)
			(= (litres r2) 11)
			(= (litres r3) 4)
			(= (litres r4) 4)
			(= (litres r5) 3)
			(= (litres r6) 2)
		)
	)
)