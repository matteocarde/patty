(define (problem name)
	(:domain drone)
	(:objects
		x0y0z0 x0y0z1 x0y0z2 x0y1z0 x0y1z1 x0y1z2 x0y2z0 x0y2z1 x0y2z2 x0y3z0 x0y3z1 x0y3z2 x0y4z0 x0y4z1 x0y4z2 x0y5z0 x0y5z1 x0y5z2 x0y6z0 x0y6z1 x0y6z2 x0y7z0 x0y7z1 x0y7z2 x0y8z0 x0y8z1 x0y8z2 - location
	)
	(:init
		(= (xl x0y2z1) 0.0)
		(= (yl x0y8z0) 8.0)
		(= (xl x0y2z2) 0.0)
		(= (xl x0y5z1) 0.0)
		(= (xl x0y5z0) 0.0)
		(= (xl x0y5z2) 0.0)
		(= (xl x0y6z2) 0.0)
		(= (xl x0y7z1) 0.0)
		(= (max_z) 3.0)
		(= (zl x0y1z2) 2.0)
		(= (min_x) 0.0)
		(= (yl x0y8z1) 8.0)
		(= (zl x0y2z1) 1.0)
		(= (xl x0y0z0) 0.0)
		(= (yl x0y0z2) 0.0)
		(= (zl x0y8z0) 0.0)
		(= (xl x0y4z2) 0.0)
		(= (xl x0y3z0) 0.0)
		(= (zl x0y8z2) 2.0)
		(= (xl x0y3z1) 0.0)
		(= (xl x0y2z0) 0.0)
		(= (zl x0y5z0) 0.0)
		(= (yl x0y7z2) 7.0)
		(= (zl x0y6z1) 1.0)
		(= (yl x0y2z2) 2.0)
		(= (yl x0y5z1) 5.0)
		(= (xl x0y6z0) 0.0)
		(= (xl x0y7z2) 0.0)
		(= (yl x0y7z1) 7.0)
		(= (yl x0y1z2) 1.0)
		(= (zl x0y3z0) 0.0)
		(= (zl x0y7z2) 2.0)
		(= (xl x0y8z1) 0.0)
		(= (xl x0y8z0) 0.0)
		(= (yl x0y4z1) 4.0)
		(= (xl x0y0z2) 0.0)
		(= (zl x0y7z0) 0.0)
		(= (yl x0y1z0) 1.0)
		(= (xl x0y8z2) 0.0)
		(= (xl x0y4z0) 0.0)
		(= (yl x0y6z1) 6.0)
		(= (xl x0y1z2) 0.0)
		(= (min_y) 0.0)
		(= (yl x0y2z0) 2.0)
		(= (yl x0y0z0) 0.0)
		(= (yl x0y7z0) 7.0)
		(= (yl x0y6z2) 6.0)
		(= (yl x0y1z1) 1.0)
		(= (zl x0y3z2) 2.0)
		(= (xl x0y0z1) 0.0)
		(= (yl x0y3z0) 3.0)
		(= (x) 0.0)
		(= (zl x0y7z1) 1.0)
		(= (battery-level) 27.0)
		(= (yl x0y6z0) 6.0)
		(= (zl x0y1z0) 0.0)
		(= (yl x0y4z0) 4.0)
		(= (yl x0y0z1) 0.0)
		(= (xl x0y4z1) 0.0)
		(= (min_z) 0.0)
		(= (max_x) 1.0)
		(= (xl x0y7z0) 0.0)
		(= (yl x0y8z2) 8.0)
		(= (yl x0y3z2) 3.0)
		(= (zl x0y0z2) 2.0)
		(= (yl x0y5z0) 5.0)
		(= (y) 0.0)
		(= (zl x0y8z1) 1.0)
		(= (zl x0y4z0) 0.0)
	)
	(:goal
			(and
				(visited x0y0z0)
				(visited x0y0z1)
				(visited x0y0z2)
				(visited x0y1z0)
				(visited x0y1z1)
				(visited x0y1z2)
				(visited x0y2z0)
				(visited x0y2z1)
				(visited x0y2z2)
				(visited x0y3z0)
				(visited x0y3z1)
				(visited x0y3z2)
				(visited x0y4z0)
				(visited x0y4z1)
				(visited x0y4z2)
				(visited x0y5z0)
				(visited x0y5z1)
				(visited x0y5z2)
				(visited x0y6z0)
				(visited x0y6z1)
				(visited x0y6z2)
				(visited x0y7z0)
				(visited x0y7z1)
				(visited x0y7z2)
				(visited x0y8z0)
				(visited x0y8z1)
				(visited x0y8z2)
				(= (x) 0.0)
				(= (y) 0.0)
				(= (z) 0.0)
			)
	)
)