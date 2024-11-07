(define (problem prob_9_5_4)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 - bottleleft
		 r1 r2 r3 r4 - bottleright
	)
	(:init
		(= (litres l1) 2)
		(= (litres l2) 4)
		(= (litres l3) 4)
		(= (litres l4) 2)
		(= (litres l5) 15)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
	)
	(:goal
		(and
			(= (litres r1) 17)
			(= (litres r2) 3)
			(= (litres r3) 6)
			(= (litres r4) 1)
		)
	)
)