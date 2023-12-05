(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(= (angle L4 xyaxes) 32.9)
		(connected L1 L2)
		(= (angle L2 ZAXES) 227.0)
		(= (angle L4 ZAXES) 288.1)
		(freeToMove L2)
		(freeToMove L1)
		(= (angle L3 ZAXES) 177.5)
		(= (angle L1 xyaxes) 106.9)
		(connected L3 L4)
		(= (angle L3 xyaxes) 242.9)
		(affects L2 L3)
		(affects L3 L4)
		(= (speed-d) 10.0)
		(affects L2 L4)
		(connected L2 L3)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 149.5)
				(> (angle L3 ZAXES) 223.7)
			)
	)
)