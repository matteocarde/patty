(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(= (angle L4 ZAXES) 302.3)
		(= (angle L1 xyaxes) 64.6)
		(affects L2 L4)
		(= (angle L4 xyaxes) 189.6)
		(= (angle L2 ZAXES) 122.1)
		(= (angle L2 xyaxes) 261.6)
		(freeToMove L3)
		(= (speed-d) 10.0)
		(= (angle L1 ZAXES) 323.2)
		(= (angle L3 xyaxes) 10.3)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 3.5)
				(> (angle L3 ZAXES) 236.9)
			)
	)
)