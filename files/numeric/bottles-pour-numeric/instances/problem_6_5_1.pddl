(define (problem prob_6_5_1)
(:domain bottles)
	(:objects
		 l1 l2 l3 l4 l5 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (litres l1) 1)
		(= (litres l2) 3)
		(= (litres l3) 10)
		(= (litres l4) 2)
		(= (litres l5) 2)
		(= (litres r1) 0)
	)
	(:goal
		(and
			(= (litres r1) 18)
		)
	)
)