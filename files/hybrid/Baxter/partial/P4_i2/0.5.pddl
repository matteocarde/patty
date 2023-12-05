(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(freeToMove L1)
		(affects L3 L4)
		(= (speed-i) 10.0)
		(affects L2 L4)
		(= (angle L1 xyaxes) 285.1)
		(= (angle L4 ZAXES) 102.2)
		(= (angle L3 ZAXES) 28.7)
		(connected L1 L2)
		(affects L2 L3)
		(= (angle L2 xyaxes) 194.8)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 311.6)
				(> (angle L3 ZAXES) 277.1)
				(< (angle L3 xyaxes) 343.4)
			)
	)
)