(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(freeToMove L1)
		(freeToMove L3)
		(= (angle L1 ZAXES) 27.3)
		(= (angle L2 ZAXES) 160.5)
		(= (angle L3 ZAXES) 43.0)
		(= (angle L1 xyaxes) 67.1)
		(affects L2 L4)
		(= (angle L2 xyaxes) 17.8)
		(connected L3 L4)
		(freeToMove L2)
		(= (angle L4 xyaxes) 271.9)
		(= (angle L4 ZAXES) 123.9)
		(freeToMove L4)
		(connected L2 L3)
		(connected L1 L2)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 5.8)
				(> (angle L3 ZAXES) 177.5)
				(< (angle L2 xyaxes) 286.5)
			)
	)
)