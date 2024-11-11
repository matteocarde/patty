(define (problem prob_14)
(:domain shake)
	(:objects
		 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 b13 b14 - bottle
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
			(packed b9)
			(packed b10)
			(packed b11)
			(packed b12)
			(packed b13)
			(packed b14)
		)
	)
)