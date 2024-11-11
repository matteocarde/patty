(define (problem prob_4)
(:domain shake)
	(:objects
		 b1 b2 b3 b4 - bottle
	)
	(:init
		(= (litres b1) 5)
		(= (litres b2) 5)
		(= (litres b3) 5)
		(= (litres b4) 5)
	)
	(:goal
		(and
			(= (litres b1) 0)
			(= (litres b2) 0)
			(= (litres b3) 0)
			(= (litres b4) 0)
		)
	)
)