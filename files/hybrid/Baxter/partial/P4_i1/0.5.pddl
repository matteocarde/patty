(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(affects L2 L3)
		(= (angle L4 ZAXES) 302.3)
		(connected L3 L4)
		(= (angle L1 ZAXES) 323.2)
		(= (angle L2 xyaxes) 261.6)
		(affects L2 L4)
		(freeToMove L2)
		(= (speed-i) 10.0)
		(= (speed-d) 10.0)
		(freeToMove L3)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 3.5)
				(> (angle L3 ZAXES) 236.9)
			)
	)
)