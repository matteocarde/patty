(define (problem prob_12)
(:domain shake)
	(:objects
		 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 b11 b12 - bottle
	)
	(:init
		(= (litres b1) 5)
		(= (litres b2) 5)
		(= (litres b3) 5)
		(= (litres b4) 5)
		(= (litres b5) 5)
		(= (litres b6) 5)
		(= (litres b7) 5)
		(= (litres b8) 5)
		(= (litres b9) 5)
		(= (litres b10) 5)
		(= (litres b11) 5)
		(= (litres b12) 5)
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
			(= (litres b8) 0)
			(= (litres b9) 0)
			(= (litres b10) 0)
			(= (litres b11) 0)
			(= (litres b12) 0)
		)
	)
)