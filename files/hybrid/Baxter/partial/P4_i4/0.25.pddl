(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(= (speed-d) 10.0)
		(freeToMove L3)
		(= (angle L4 xyaxes) 32.9)
		(connected L2 L3)
		(freeToMove L2)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 149.5)
				(> (angle L3 ZAXES) 223.7)
			)
	)
)