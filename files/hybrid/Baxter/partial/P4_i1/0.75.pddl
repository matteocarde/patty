(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(affects L2 L4)
		(= (angle L1 xyaxes) 64.6)
		(= (speed-d) 10.0)
		(freeToMove L3)
		(= (speed-i) 10.0)
		(= (angle L4 xyaxes) 189.6)
		(= (angle L3 xyaxes) 10.3)
		(affects L2 L3)
		(freeToMove L4)
		(= (angle L2 xyaxes) 261.6)
		(freeToMove L2)
		(= (angle L2 ZAXES) 122.1)
		(= (angle L3 ZAXES) 21.5)
		(freeToMove L1)
		(connected L3 L4)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 3.5)
				(> (angle L3 ZAXES) 236.9)
			)
	)
)