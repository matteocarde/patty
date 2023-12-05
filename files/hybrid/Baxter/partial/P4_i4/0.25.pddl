(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(freeToMove L3)
		(= (angle L4 ZAXES) 288.1)
		(affects L2 L4)
		(= (speed-d) 10.0)
		(freeToMove L1)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 149.5)
				(> (angle L3 ZAXES) 223.7)
			)
	)
)