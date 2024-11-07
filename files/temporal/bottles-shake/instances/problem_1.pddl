(define (problem prob_1)
(:domain shake)
	(:objects
		 b1 - bottle
	)
	(:init
		(= (litres b1) 5)
	)
	(:goal
		(and
			(= (litres b1) 0)
		)
	)
)