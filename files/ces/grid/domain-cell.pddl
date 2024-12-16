(define (domain dig)
	(:requirements :strips :equality :conditional-effects)
	(:types
		cell ongrid - object
		robot treasure - ongrid
	)
	(:predicates
		(isLeft ?x2 - cell ?x1 - cell)
		(isDown ?x2 - cell ?x1 - cell)
		(at ?o - ongrid ?x - cell ?y - cell)
		(picked ?r - robot ?t - treasure)
	)

	(:action lft
		:parameters (?r - robot ?y - cell)
		:precondition()
		:effect(and
			(forall
				(?fromX - cell ?toX - cell) ;x2 <- x1
				(when
					(and
						(at ?r ?fromX ?y)
						(isLeft ?toX ?fromX)
					)
					(and
						(not (at ?r ?fromX ?y))
						(at ?r ?toX ?y)
					)
				)
			)
		)
	)

	(:action rgt
		:parameters (?r - robot ?y - cell)
		:precondition()
		:effect(and
			(forall
				(?fromX - cell ?toX - cell) ;x1 -> x2
				(when
					(and
						(at ?r ?fromX ?y)
						(isLeft ?fromX ?toX)
					)
					(and
						(not (at ?r ?fromX ?y))
						(at ?r ?toX ?y)
					)
				)
			)
		)
	)

	(:action up
		:parameters (?r - robot ?x - cell)
		:precondition()
		:effect(and
			(forall
				(?fromY - cell ?toY - cell)
				(when
					(and
						(at ?r ?x ?fromY)
						(isDown ?fromY ?toY)
					)
					(and
						(not (at ?r ?x ?fromY))
						(at ?r ?x ?toY)
					)
				)
			)
		)
	)

	(:action dwn
		:parameters (?r - robot ?x - cell)
		:precondition()
		:effect(and
			(forall
				(?fromY - cell ?toY - cell)
				(when
					(and
						(at ?r ?x ?fromY)
						(isDown ?toY ?fromY)
					)
					(and
						(not (at ?r ?x ?fromY))
						(at ?r ?x ?toY)
					)
				)
			)
		)
	)

	(:action pick
		:parameters (?r - robot ?t - treasure ?x - cell ?y - cell)
		:precondition(and
			(at ?r ?x ?y)
			(at ?t ?x ?y)
		)
		:effect(and
			(picked ?r ?t)
			(not (at ?t ?x ?y))
		)
	)

)