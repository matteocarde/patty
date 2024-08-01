(define (problem prob_4_3_1)
(:domain bottles)
	(:objects
		 l1 l2 l3 - bottleleft
		 r1 - bottleright
	)
	(:init
		(= (litres l1) 1)
		(= (litres l2) 9)
		(= (litres l3) 2)
		(= (litres r1) 0)
	)
	(:goal
		(and
			(= (litres r1) 12)
		)
	)
)