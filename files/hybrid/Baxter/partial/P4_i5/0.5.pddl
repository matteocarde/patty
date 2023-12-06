(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(= (angle L2 xyaxes) 216.6)
		(= (angle L4 xyaxes) 350.4)
		(= (speed-i) 10.0)
		(= (angle L1 xyaxes) 135.7)
		(= (angle L3 ZAXES) 205.9)
		(affects L2 L4)
		(connected L2 L3)
		(= (angle L2 ZAXES) 338.0)
		(freeToMove L1)
		(freeToMove L4)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 239.3)
				(> (angle L3 ZAXES) 66.8)
				(< (angle L4 xyaxes) 148.7)
			)
	)
)