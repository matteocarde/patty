(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(= (angle L3 ZAXES) 43.0)
		(connected L3 L4)
		(affects L2 L3)
		(= (angle L2 ZAXES) 160.5)
		(affects L2 L4)
		(freeToMove L2)
		(= (angle L2 xyaxes) 17.8)
		(= (angle L1 ZAXES) 27.3)
		(connected L1 L2)
		(= (angle L3 xyaxes) 101.6)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 5.8)
				(> (angle L3 ZAXES) 177.5)
				(< (angle L2 xyaxes) 286.5)
			)
	)
)