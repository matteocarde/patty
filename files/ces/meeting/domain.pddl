(define (domain meeting)
	(:requirements :strips :equality :conditional-effects)
	(:types
		x y z - object
		robot
	)
	(:predicates
		(isNextX ?c1 - x ?c2 - x)
		(isNextY ?c1 - y ?c2 - y)
		(isNextZ ?c1 - z ?c2 - z)
		(atX ?r - robot ?x - x)
		(atY ?r - robot ?y - y)
		(atZ ?r - robot ?z - z)
	)

	(:action fwd
		:parameters (?r - robot)
		:precondition()
		:effect(and
			(forall
				(?from - x ?to - x)
				(when
					(and
						(atX ?r ?from)
						(isNextX ?from ?to)
					)
					(and
						(not (atX ?r ?from))
						(atX ?r ?to)
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
				(?from - y ?to - y)
				(when
					(and
						(atY ?r ?from)
						(isNextY ?from ?to)
					)
					(and
						(not (atY ?r ?from))
						(atY ?r ?to)
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
				(?from - z ?to - z)
				(when
					(and
						(atZ ?r ?from)
						(isNextZ ?from ?to)
					)
					(and
						(not (atZ ?r ?from))
						(atZ ?r ?to)
					)
				)
			)
		)
	)

	(:constraints
		(and
			(forall
				(?r - robot ?x1 - x ?x2 - x)
				(and
					(not (= ?x1 ?x2))
					(or (not (atX ?r ?x1))
						(not (atX ?r ?x2)))
				)
			)
			(forall
				(?r - robot ?y1 - y ?y2 - y)
				(and
					(not (= ?y1 ?y2))
					(or (not (atY ?r ?y1))
						(not (atY ?r ?y2)))
				)
			)
			(forall
				(?r - robot ?z1 - z ?z2 - z)
				(and
					(not (= ?z1 ?z2))
					(or (not (atZ ?r ?z1))
						(not (atZ ?r ?z2)))
				)
			)
		)

	)
)