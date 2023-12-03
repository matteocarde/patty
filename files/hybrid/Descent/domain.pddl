;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (domain car)

	;(:requirements :fluents :durative-actions :duration-inequalities :adl :typing :time)
	(:predicates
		(alwaysfalse)
		(landed)
		(landing)
		(thrusting)
		(stop)
		(block)
	)
	(:functions
		(M)
		(q)
		(d)
		(g)
		(v)
		(M_min)
		(ISP)
		(d_final)
		(v_margin)
		(d_margin)
		(falling-time)
		(thrust-duration)
	)

	(:process falling
		:parameters ()
		:precondition (and
			(< (falling-time) 40)
			(landing)
			(< (d) (d_final))
			(not (block))
		)
		:effect (and
			(increase (d) (* #t (* 0.5 (v))) )
			(increase (v) (* #t (g)))
			(increase (falling-time) (* #t 1.0))
		)
	)

	(:process thrust
		:parameters ()
		:precondition (and
			(landing)
			(thrusting)
			(not (block))
			(> (M) 0)
		)
		:effect (and
			(decrease
				(v)
				(* #t (* (* (ISP) (g)) (/ (q) (M)))))
			(decrease (M) (* #t (q)))
			(increase (thrust-duration) (* #t 1.0))
		)
	)

	(:action start_descent
		:parameters()
		:precondition (and
			(stop)
			(not (block))
		)
		:effect (and
			(landing)
			(assign (falling-time) 0)
			(not (stop))
		)
	)

	(:action land
		:parameters ()
		:precondition (and
			(not (block))
			(landing)
			(< (v) (v_margin)) (< (d) (d_final))
			(> (d) (- (d_final) (d_margin)))
		)
		:effect (and
			(landed)
			(not (landing))
		)
	)

	(:action start-thrust
		:parameters ()
		:precondition (and
			(not (thrusting))
			(landing)
			(not (block))
		)
		:effect (and
			(thrusting)
			(assign (thrust-duration) 0)
		)
	)

	(:action stop-thrust
		:parameters ()
		:precondition (and (thrusting) (not (block)))
		:effect (and
			(not (thrusting))
		)
	)

	(:event thrust-finished
		:parameters ()
		:precondition (and
			(thrusting)
			(>= (thrust-duration) (/ (- (M) (M_min)) (q)))
		)
		:effect (and
			(not (thrusting))
		)
	)

	(:event anti-crash1
		:parameters()
		:precondition (and
			(> (d) (d_final))
			(not (block)))
		:effect (and (block))
	)

	(:event anti-crash2
		:parameters()
		:precondition (and
			(< (M) (M_min))
			(not (block)))
		:effect (and (block))
	)

	; (:event anti-crash
	; 	:parameters()
	; 	:precondition (and
	; 		(and
	; 			(< (d) (d_final))
	; 		)
	; 		(not (and
	; 				(< (d) (d_final)) ;not ((d < df) and (M > Min)) = (d > df) or (M < Min)
	; 				(> (M) (M_min))))
	; 		(not (block)))
	; 	:effect (and (block))
	; )

)