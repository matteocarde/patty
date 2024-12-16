(define (domain grid)
	(:requirements :strips :equality :conditional-effects)
	(:types
		column row - object
		robot
	)
	(:predicates
		(isLeft ?c1 - column ?c2 - column)
		(isDown ?r2 - row ?r1 - row)
		(atColumn ?r - robot ?c - column)
		(atRow ?r - robot ?r - row)
	)

	(:action lft
		:parameters (?r - robot)
		:precondition()
		:effect(and
			(forall
				(?fromColumn - column ?toColumn - column)
				(when
					(and
						(atColumn ?r ?fromColumn)
						(isLeft ?toColumn ?fromColumn)
					)
					(and
						(not (atColumn ?r ?fromColumn))
						(atColumn ?r ?toColumn)
					)
				)
			)
		)
	)

	(:action rgt
		:parameters (?r - robot)
		:precondition()
		:effect(and
			(forall
				(?fromColumn - column ?toColumn - column)
				(when
					(and
						(atColumn ?r ?fromColumn)
						(isLeft ?fromColumn ?toColumn)
					)
					(and
						(not (atColumn ?r ?fromColumn))
						(atColumn ?r ?toColumn)
					)
				)
			)
		)
	)

	(:action up
		:parameters (?r - robot)
		:precondition()
		:effect(and
			(forall
				(?fromRow - row ?toRow - row)
				(when
					(and
						(atRow ?r ?fromRow)
						(isDown ?fromRow ?toRow)
					)
					(and
						(not (atRow ?r ?fromRow))
						(atRow ?r ?toRow)
					)
				)
			)
		)
	)

	(:action dwn
		:parameters (?r - robot)
		:precondition()
		:effect(and
			(forall
				(?fromRow - row ?toRow - row)
				(when
					(and
						(atRow ?r ?fromRow)
						(isDown ?toRow ?fromRow)
					)
					(and
						(not (atRow ?r ?fromRow))
						(atRow ?r ?toRow)
					)
				)
			)
		)
	)

)