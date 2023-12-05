(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(connected L2 L3)
		(= (angle L2 xyaxes) 216.6)
		(connected L1 L2)
		(freeToMove L1)
		(connected L3 L4)
		(= (angle L3 xyaxes) 143.6)
		(affects L2 L4)
		(= (angle L1 ZAXES) 243.5)
		(= (angle L1 xyaxes) 135.7)
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