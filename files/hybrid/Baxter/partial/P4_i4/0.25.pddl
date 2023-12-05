(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(freeToMove L1)
		(affects L2 L3)
		(= (angle L3 ZAXES) 177.5)
		(= (angle L3 xyaxes) 242.9)
		(= (angle L2 xyaxes) 249.0)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 149.5)
				(> (angle L3 ZAXES) 223.7)
			)
	)
)