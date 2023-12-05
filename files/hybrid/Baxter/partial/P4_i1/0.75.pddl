(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(freeToMove L2)
		(affects L2 L4)
		(freeToMove L3)
		(= (speed-d) 10.0)
		(connected L3 L4)
		(= (angle L2 xyaxes) 261.6)
		(connected L1 L2)
		(= (angle L1 ZAXES) 323.2)
		(= (angle L3 xyaxes) 10.3)
		(freeToMove L1)
		(= (speed-i) 10.0)
		(affects L3 L4)
		(affects L2 L3)
		(= (angle L4 xyaxes) 189.6)
		(= (angle L2 ZAXES) 122.1)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 3.5)
				(> (angle L3 ZAXES) 236.9)
			)
	)
)