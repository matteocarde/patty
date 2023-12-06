(define (problem name)
	(:domain drone)
	(:objects
		x0y0z0 x0y0z1 - location
	)
	(:init
		(= (xl x0y0z0) 0.0)
		(= (zl x0y0z0) 0.0)
		(= (xl x0y0z1) 0.0)
		(= (max_x) 1.0)
		(= (zl x0y0z1) 1.0)
		(= (yl x0y0z1) 0.0)
		(= (y) 0.0)
		(= (max_z) 2.0)
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