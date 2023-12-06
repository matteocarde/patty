(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(affects L2 L3)
		(freeToMove L2)
		(= (speed-i) 10.0)
		(= (angle L1 ZAXES) 71.5)
		(freeToMove L4)
		(affects L3 L4)
		(= (angle L4 xyaxes) 137.0)
		(connected L2 L3)
		(= (angle L3 ZAXES) 28.7)
		(freeToMove L3)
		(= (angle L2 xyaxes) 194.8)
		(= (speed-d) 10.0)
		(= (angle L1 xyaxes) 285.1)
		(affects L2 L4)
		(connected L1 L2)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 311.6)
				(> (angle L3 ZAXES) 277.1)
				(< (angle L3 xyaxes) 343.4)
			)
	)
)