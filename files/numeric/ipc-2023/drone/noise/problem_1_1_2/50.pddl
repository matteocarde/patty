(define (problem name)
	(:domain drone)
	(:objects
		x0y0z0 x0y0z1 - location
	)
	(:init
		(= (x) -25.0)
		(= (y) -36.0)
		(= (z) 35.0)
		(= (min_x) 15.0)
		(= (max_x) 2.0)
		(= (min_y) 2.0)
		(= (max_y) -49.0)
		(= (min_z) -1.0)
		(= (max_z) 46.0)
		(= (xl x0y0z0) 26.0)
		(= (yl x0y0z0) -17.0)
		(= (zl x0y0z0) -13.0)
		(= (xl x0y0z1) 44.0)
		(= (yl x0y0z1) -36.0)
		(= (zl x0y0z1) 13.0)
		(= (battery-level) 39.0)
		(= (battery-level-full) 43.0)
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