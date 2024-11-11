(define (problem prob_2)
(:domain shake)
	(:objects
		 b1 b2 - bottle
	)
	(:init
		(= (litres b1) 5)
		(= (litres b2) 5)
	)
	(:goal
		(and
			(= (litres b1) 0)
			(= (litres b2) 0)
		)
	)
)