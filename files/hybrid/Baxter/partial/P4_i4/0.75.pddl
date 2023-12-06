(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(freeToMove L4)
		(= (angle L4 ZAXES) 288.1)
		(= (angle L3 xyaxes) 242.9)
		(= (angle L3 ZAXES) 177.5)
		(connected L2 L3)
		(connected L1 L2)
		(= (speed-i) 10.0)
		(affects L2 L3)
		(= (angle L2 ZAXES) 227.0)
		(affects L3 L4)
		(= (angle L1 ZAXES) 269.9)
		(freeToMove L2)
		(= (angle L4 xyaxes) 32.9)
		(connected L3 L4)
		(= (angle L2 xyaxes) 249.0)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 149.5)
				(> (angle L3 ZAXES) 223.7)
			)
	)
)