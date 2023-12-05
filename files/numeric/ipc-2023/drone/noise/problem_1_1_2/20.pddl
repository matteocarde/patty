(define (problem name)
	(:domain drone)
	(:objects
		x0y0z0 x0y0z1 - location
	)
	(:init
		(= (x) -16.0)
		(= (y) -6.0)
		(= (z) -17.0)
		(= (min_x) 11.0)
		(= (max_x) -4.0)
		(= (min_y) 10.0)
		(= (max_y) 15.0)
		(= (min_z) -16.0)
		(= (max_z) 5.0)
		(= (xl x0y0z0) 6.0)
		(= (yl x0y0z0) 3.0)
		(= (zl x0y0z0) 12.0)
		(= (xl x0y0z1) 5.0)
		(= (yl x0y0z1) 0.0)
		(= (zl x0y0z1) 11.0)
		(= (battery-level) 26.0)
		(= (battery-level-full) 28.0)
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