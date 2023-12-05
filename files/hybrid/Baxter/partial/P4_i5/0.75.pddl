(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(= (angle L2 ZAXES) 338.0)
		(connected L2 L3)
		(freeToMove L4)
		(freeToMove L3)
		(= (speed-i) 10.0)
		(= (angle L3 ZAXES) 205.9)
		(= (angle L1 xyaxes) 135.7)
		(affects L2 L3)
		(= (angle L4 xyaxes) 350.4)
		(affects L2 L4)
		(connected L1 L2)
		(freeToMove L1)
		(= (angle L2 xyaxes) 216.6)
		(= (angle L3 xyaxes) 143.6)
		(= (speed-d) 10.0)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 239.3)
				(> (angle L3 ZAXES) 66.8)
				(< (angle L4 xyaxes) 148.7)
			)
	)
)