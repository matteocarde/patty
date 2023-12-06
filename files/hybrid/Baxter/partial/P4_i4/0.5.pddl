(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(= (speed-i) 10.0)
		(connected L1 L2)
		(= (angle L1 ZAXES) 269.9)
		(connected L2 L3)
		(affects L2 L3)
		(= (angle L4 ZAXES) 288.1)
		(= (angle L1 xyaxes) 106.9)
		(= (angle L3 xyaxes) 242.9)
		(= (speed-d) 10.0)
		(connected L3 L4)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 149.5)
				(> (angle L3 ZAXES) 223.7)
			)
	)
)