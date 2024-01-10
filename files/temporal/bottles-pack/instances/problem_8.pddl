(define (problem prob_8)
(:domain shake)
	(:objects
		 b1 b2 b3 b4 b5 b6 b7 b8 - bottle
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
			(packed b7)
			(packed b8)
		)
	)
)