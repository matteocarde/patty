(define (problem pb01)
	(:domain dig)
	(:objects
		c01 c02 c03 c04 c05 c06 c07 - cell
		r1 - robot
	)
	(:init
		(isLeft c01 c02)
		(isLeft c02 c03)
		(isLeft c03 c04)
		(isLeft c04 c05)
		(isLeft c05 c06)
		(isLeft c06 c07)
		(isLeft c07 c01)

		(isDown c01 c02)
		(isDown c02 c03)
		(isDown c03 c04)
		(isDown c04 c05)
		(isDown c05 c06)
		(isDown c06 c07)
		(isDown c07 c01)

		(at r1 c05 c05)
	)
	(:goal
		(and (at r1 c01 c01))
	)
)