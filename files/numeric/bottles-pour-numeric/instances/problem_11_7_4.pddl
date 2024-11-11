(define (problem prob_11_7_4)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 - bottleleft
		 r1 r2 r3 r4 - bottleright
	)
	(:init
		(= (litres l1) 22)
		(= (litres l2) 1)
		(= (litres l3) 3)
		(= (litres l4) 1)
		(= (litres l5) 1)
		(= (litres l6) 2)
		(= (litres l7) 3)
		(= (litres r1) 0)
		(= (litres r2) 0)
		(= (litres r3) 0)
		(= (litres r4) 0)
	)
	(:goal
		(and
			(= (litres r1) 6)
			(= (litres r2) 7)
			(= (litres r3) 12)
			(= (litres r4) 8)
		)
	)
)