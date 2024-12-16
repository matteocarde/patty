(define (problem pb01)
	(:domain dig)
	(:objects
		r01 r02 r03 - row
		c01 c02 c03 - column
		r1 - robot
	)
	(:init
		(isLeft c01 c02)
		(isLeft c02 c03)
		(isLeft c03 c01)

		(isDown r01 r02)
		(isDown r02 r03)
		(isDown r03 r01)

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