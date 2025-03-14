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

	(:constraints
		(and
			(forall
				(?r - robot ?r1 - row ?r2 - row)
				(and
					(not (= ?r1 ?r2))
					(or (not (atRow ?r ?r1))
						(not (atRow ?r ?r2)))
				)
			)
			(forall
				(?r - robot ?c1 - column ?c2 - column)
				(and
					(not (= ?c1 ?c2))
					(or (not (atColumn ?r ?c1))
						(not (atColumn ?r ?c2)))
				)
			)
			(exists
				(?r - robot ?c - column)
				(and
					(atColumn ?r ?c)
				)
			)
			(exists
				(?r - robot ?row - row)
				(and
					(atRow ?r ?row)
				)
			)
		)

	)
)