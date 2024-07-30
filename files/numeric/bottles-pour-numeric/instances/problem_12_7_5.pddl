(define (problem prob_12_7_5)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 - bottleleft
		 r1 r2 r3 r4 r5 - bottleright
	)
	(:init
		(= (litres l1) 3)
		(= (litres l2) 5)
		(= (litres l3) 5)
		(= (litres l4) 4)
		(= (litres l5) 4)
		(= (litres l6) 4)
		(= (litres l7) 11)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
		(= (litres r5) 0)
	)
	(:goal
		(and
			(= (litres r1) 5)
			(= (litres r2) 4)
			(= (litres r3) 3)
			(= (litres r4) 20)
			(= (litres r5) 4)
		)
	)
)