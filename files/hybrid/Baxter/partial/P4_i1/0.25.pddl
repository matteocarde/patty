(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
		(= (angle L1 ZAXES) 323.2)
		(freeToMove L1)
		(freeToMove L2)
		(freeToMove L3)
		(= (angle L1 xyaxes) 64.6)
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 3.5)
				(> (angle L3 ZAXES) 236.9)
			)
	)
)