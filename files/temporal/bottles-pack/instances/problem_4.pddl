(define (problem prob_4)
(:domain shake)
	(:objects
		 b1 b2 b3 b4 - bottle
	)
	(:init
		(= (on-platform) 0)
	)
	(:goal
		(and
			(packed b1)
			(packed b2)
			(packed b3)
			(packed b4)
		)
	)
)