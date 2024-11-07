(define (problem prob_12_5_7)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 - bottleleft
		 r1 r2 r3 r4 r5 r6 r7 - bottleright
	)
	(:init
		(= (litres l1) 2)
		(= (litres l2) 23)
		(= (litres l3) 3)
		(= (litres l4) 4)
		(= (litres l5) 4)
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
			(= (litres r1) 4)
			(= (litres r2) 2)
			(= (litres r3) 3)
			(= (litres r4) 2)
			(= (litres r5) 5)
			(= (litres r6) 4)
			(= (litres r7) 16)
		)
	)
)