(define (problem prob_13_5_8)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 - bottleleft
		 r1 r2 r3 r4 r5 r6 r7 r8 - bottleright
	)
	(:init
		(= (litres l1) 20)
		(= (litres l2) 4)
		(= (litres l3) 5)
		(= (litres l4) 3)
		(= (litres l5) 7)
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
			(= (litres r1) 3)
			(= (litres r2) 3)
			(= (litres r3) 2)
			(= (litres r4) 4)
			(= (litres r5) 21)
			(= (litres r6) 2)
			(= (litres r7) 2)
			(= (litres r8) 2)
		)
	)
)