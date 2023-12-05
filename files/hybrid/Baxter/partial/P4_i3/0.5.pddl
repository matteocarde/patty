(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(freeToMove L1)
		(= (angle L4 xyaxes) 271.9)
		(connected L1 L2)
		(= (speed-i) 10.0)
		(= (speed-d) 10.0)
		(connected L2 L3)
		(freeToMove L2)
		(= (angle L1 xyaxes) 67.1)
		(= (angle L4 ZAXES) 123.9)
		(= (angle L2 ZAXES) 160.5)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 5.8)
				(> (angle L3 ZAXES) 177.5)
				(< (angle L2 xyaxes) 286.5)
			)
	)
)