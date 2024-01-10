(define (problem prob_6)
(:domain shake)
	(:objects
		 b1 b2 b3 b4 b5 b6 - bottle
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
			(packed b5)
			(packed b6)
		)
	)
)