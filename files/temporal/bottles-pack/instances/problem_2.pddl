(define (problem prob_2)
(:domain shake)
	(:objects
		 b1 b2 - bottle
	)
	(:init
		(= (on-platform) 0)
	)
	(:goal
		(and
			(packed b1)
			(packed b2)
		)
	)
)