(define (problem name)
	(:domain drone)
	(:objects
		x0y0z0 x0y0z1 x0y0z2 x0y0z3 - location
	)
	(:init
		(= (zl x0y0z2) 2.0)
		(= (battery-level) 13.0)
		(= (max_z) 4.0)
		(= (max_y) 1.0)
		(= (y) 0.0)
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