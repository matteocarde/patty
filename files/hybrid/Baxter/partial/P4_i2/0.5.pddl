(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(freeToMove L4)
		(= (angle L1 ZAXES) 71.5)
		(= (speed-i) 10.0)
		(connected L3 L4)
		(= (speed-d) 10.0)
		(= (angle L4 ZAXES) 102.2)
		(= (angle L4 xyaxes) 137.0)
		(= (angle L2 ZAXES) 277.6)
		(affects L2 L4)
		(connected L2 L3)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 311.6)
				(> (angle L3 ZAXES) 277.1)
				(< (angle L3 xyaxes) 343.4)
			)
	)
)