(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(affects L2 L3)
		(= (angle L2 ZAXES) 160.5)
		(= (angle L3 ZAXES) 43.0)
		(freeToMove L2)
		(freeToMove L4)
		(affects L2 L4)
		(= (angle L2 xyaxes) 17.8)
		(connected L1 L2)
		(= (angle L1 ZAXES) 27.3)
		(affects L3 L4)
		(connected L2 L3)
		(= (speed-d) 10.0)
		(= (angle L1 xyaxes) 67.1)
		(freeToMove L3)
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