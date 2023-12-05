(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(affects L2 L4)
		(= (angle L4 ZAXES) 288.1)
		(= (speed-i) 10.0)
		(connected L2 L3)
		(= (angle L1 xyaxes) 106.9)
		(= (angle L2 ZAXES) 227.0)
		(freeToMove L2)
		(freeToMove L3)
		(= (angle L3 xyaxes) 242.9)
		(= (speed-d) 10.0)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 149.5)
				(> (angle L3 ZAXES) 223.7)
			)
	)
)