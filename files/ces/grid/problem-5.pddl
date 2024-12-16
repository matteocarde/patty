(define (problem pb01)
	(:domain dig)
	(:objects
		r01 r02 r03 r04 r05 - row
		c01 c02 c03 c04 c05 - column
		r1 - robot
	)
	(:init
		(isLeft c01 c02)
		(isLeft c02 c03)
		(isLeft c03 c04)
		(isLeft c04 c05)
		(isLeft c05 c01)

		(isDown r01 r02)
		(isDown r02 r03)
		(isDown r03 r04)
		(isDown r04 r05)
		(isDown r05 r01)

		(atColumn r1 c01)
		(atRow r1 r01)
	)
	(:goal
		(and
			(atColumn r1 c03)
			(atRow r1 r03)
		)
	)
)