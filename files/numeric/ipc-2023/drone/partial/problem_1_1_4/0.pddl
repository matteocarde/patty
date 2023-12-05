(define (problem name)
	(:domain drone)
	(:objects
		x0y0z0 x0y0z1 x0y0z2 x0y0z3 - location
	)
	(:init
	)
	(:goal
			(and
				(visited x0y0z0)
				(visited x0y0z1)
				(visited x0y0z2)
				(visited x0y0z3)
				(= (x) 0.0)
				(= (y) 0.0)
				(= (z) 0.0)
			)
	)
)