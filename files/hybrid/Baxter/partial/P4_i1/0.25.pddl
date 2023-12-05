(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(connected L1 L2)
		(= (angle L1 xyaxes) 64.6)
		(= (speed-i) 10.0)
		(freeToMove L3)
		(freeToMove L2)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 3.5)
				(> (angle L3 ZAXES) 236.9)
			)
	)
)