(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(affects L2 L4)
		(= (angle L4 xyaxes) 350.4)
		(connected L2 L3)
		(affects L3 L4)
		(= (angle L4 ZAXES) 153.6)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 239.3)
				(> (angle L3 ZAXES) 66.8)
				(< (angle L4 xyaxes) 148.7)
			)
	)
)