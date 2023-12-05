(define (problem name)
	(:domain drone)
	(:objects
		x0y0z0 x0y1z0 x0y2z0 x0y3z0 x0y4z0 x0y5z0 x0y6z0 x0y7z0 - location
	)
	(:init
	)
	(:goal
			(and
				(visited x0y0z0)
				(visited x0y1z0)
				(visited x0y2z0)
				(visited x0y3z0)
				(visited x0y4z0)
				(visited x0y5z0)
				(visited x0y6z0)
				(visited x0y7z0)
				(= (x) 0.0)
				(= (y) 0.0)
				(= (z) 0.0)
			)
	)
)