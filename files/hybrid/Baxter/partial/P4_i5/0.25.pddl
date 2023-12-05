(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(freeToMove L4)
		(= (angle L3 ZAXES) 205.9)
		(connected L3 L4)
		(= (angle L4 ZAXES) 153.6)
		(connected L1 L2)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 239.3)
				(> (angle L3 ZAXES) 66.8)
				(< (angle L4 xyaxes) 148.7)
			)
	)
)