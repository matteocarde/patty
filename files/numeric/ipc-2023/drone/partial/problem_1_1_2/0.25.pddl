(define (problem name)
	(:domain drone)
	(:objects
		x0y0z0 x0y0z1 - location
	)
	(:init
		(= (z) 0.0)
		(= (zl x0y0z0) 0.0)
		(= (min_y) 0.0)
		(= (battery-level) 9.0)
	)
	(:goal
			(and
				(visited x0y0z0)
				(visited x0y0z1)
				(= (x) 0.0)
				(= (y) 0.0)
				(= (z) 0.0)
			)
	)
)