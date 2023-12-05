(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(affects L2 L3)
		(freeToMove L2)
		(= (angle L2 xyaxes) 194.8)
		(freeToMove L1)
		(= (angle L4 ZAXES) 102.2)
		(freeToMove L4)
		(= (angle L1 ZAXES) 71.5)
		(= (angle L4 xyaxes) 137.0)
		(= (angle L2 ZAXES) 277.6)
		(= (angle L3 xyaxes) 20.2)
		(= (angle L3 ZAXES) 28.7)
		(connected L1 L2)
		(= (speed-d) 10.0)
		(= (angle L1 xyaxes) 285.1)
		(= (speed-i) 10.0)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 311.6)
				(> (angle L3 ZAXES) 277.1)
				(< (angle L3 xyaxes) 343.4)
			)
	)
)