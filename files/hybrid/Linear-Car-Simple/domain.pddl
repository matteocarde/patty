(define (domain car_linear_mt_sc)
	;(:requirements :fluents :durative-actions :duration-inequalities :adl :typing :time)
	(:predicates
		(on)
	)

	(:functions
		(d)
		(v)
		(a)
		(D)
		(A)
	)

	(:action gas
		:parameters ()
		:precondition (and
			(< (a) (A))
			(on))
		:effect (and
			(increase (a) 1.0)
		)
	)

	(:action break
		:parameters ()
		:precondition (and
			(> (a) (D))
			(on)
		)
		:effect (and
			(decrease (a) 1.0)
		)
	)

	(:action turnOn
		:parameters ()
		:precondition (and
			(not (on))
		)
		:effect (and
			(on)
		)
	)

	(:event idle
		:parameters ()
		:precondition (and
			(on)
			(< (a) 0.1)
			(<= (v) 0.1)
		)
		:effect (and
			(not (on))
		)
	)

	(:process move
		:parameters ()
		:precondition (and(on))
		:effect (and
			(increase (d) (* #t (v)))
		)
	)

	(:process speed
		:parameters ()
		:precondition (and(on))
		:effect (and
			(increase (v) (* #t (a)))
		)
	)

)