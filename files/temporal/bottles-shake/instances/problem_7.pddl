(define (problem prob_7)
(:domain shake)
	(:objects
		 b1 b2 b3 b4 b5 b6 b7 - bottle
	)
	(:init
		(= (litres b1) 5)
		(= (litres b2) 5)
		(= (litres b3) 5)
		(= (litres b4) 5)
		(= (litres b5) 5)
		(= (litres b6) 5)
		(= (litres b7) 5)
	)
	(:goal
		(and
			(= (litres b1) 0)
			(= (litres b2) 0)
			(= (litres b3) 0)
			(= (litres b4) 0)
			(= (litres b5) 0)
			(= (litres b6) 0)
			(= (litres b7) 0)
		)
	)
)