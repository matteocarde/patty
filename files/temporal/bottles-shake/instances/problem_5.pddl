(define (problem prob_5)
(:domain shake)
	(:objects
		 b1 b2 b3 b4 b5 - bottle
	)
	(:init
		(= (litres b1) 5)
		(= (litres b2) 5)
		(= (litres b3) 5)
		(= (litres b4) 5)
		(= (litres b5) 5)
	)
	(:goal
		(and
			(= (litres b1) 0)
			(= (litres b2) 0)
			(= (litres b3) 0)
			(= (litres b4) 0)
			(= (litres b5) 0)
		)
	)
)