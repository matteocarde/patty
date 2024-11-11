(define (problem prob_11_3_8)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 r2 r3 r4 r5 r6 r7 r8 - bottleright
	)
	(:init
		(= (litres l1) 3)
		(= (litres l2) 1)
		(= (litres l3) 29)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
		(= (litres r6) 0)
		(= (litres r7) 0)
		(= (litres r8) 0)
	)
	(:goal
		(and
			(= (litres r1) 4)
			(= (litres r2) 4)
			(= (litres r3) 2)
			(= (litres r4) 1)
			(= (litres r5) 10)
			(= (litres r6) 4)
			(= (litres r7) 4)
			(= (litres r8) 4)
		)
	)
)