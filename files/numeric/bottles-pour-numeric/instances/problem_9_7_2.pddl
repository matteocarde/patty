(define (problem prob_9_7_2)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 l6 l7 - bottleleft
		 r1 r2 - bottleright
	)
	(:init
		(= (litres l1) 16)
		(= (litres l2) 1)
		(= (litres l3) 1)
		(= (litres l4) 1)
		(= (litres l5) 3)
		(= (litres l6) 2)
		(= (litres l7) 3)
		(= (litres r1) 0)
		(= (litres r2) 0)
	)
	(:goal
		(and
			(= (litres r1) 7)
			(= (litres r2) 20)
		)
	)
)