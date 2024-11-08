(define (problem prob_3)
(:domain shake)
	(:objects
		 b1 b2 b3 - bottle
	)
	(:init
		(= (litres b1) 5)
		(= (litres b2) 5)
		(= (litres b3) 5)
	)
	(:goal
		(and
			(= (litres b1) 0)
			(= (litres b2) 0)
			(= (litres b3) 0)
		)
	)
)