(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(= (angle L4 ZAXES) 288.1)
		(connected L2 L3)
		(= (angle L1 xyaxes) 106.9)
		(affects L3 L4)
		(freeToMove L1)
		(connected L1 L2)
		(freeToMove L3)
		(= (angle L4 xyaxes) 32.9)
		(= (speed-d) 10.0)
		(= (angle L3 ZAXES) 177.5)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 149.5)
				(> (angle L3 ZAXES) 223.7)
			)
	)
)