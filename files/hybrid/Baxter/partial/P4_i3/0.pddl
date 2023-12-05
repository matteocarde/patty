(define (problem example)
	(:domain paco3d)
	(:objects
		L1 L2 L3 L4 - link
		xyaxes ZAXES - axis
	)
	(:init
	)
	(:goal
			(and
				(> (angle L3 xyaxes) 5.8)
				(> (angle L3 ZAXES) 177.5)
				(< (angle L2 xyaxes) 286.5)
			)
	)
)