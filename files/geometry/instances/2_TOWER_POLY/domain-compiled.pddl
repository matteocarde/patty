
(define (domain geometry_2_TOWER_POLY)

	(:types
		obstacle - object
	)

	(:functions
		(x)
		(y)
		(maxy)
		(maxx)
		(miny)
		(minx)
		(a1 ?b -obstacle)
		(b1 ?b -obstacle)
		(c1 ?b -obstacle)
		(a2 ?b -obstacle)
		(b2 ?b -obstacle)
		(c2 ?b -obstacle)
		(a3 ?b -obstacle)
		(b3 ?b -obstacle)
		(c3 ?b -obstacle)
		(a4 ?b -obstacle)
		(b4 ?b -obstacle)
		(c4 ?b -obstacle)
	)

	(:action move_1_0
		:parameters ()
		:precondition (and
			(forall
				(?b - obstacle)
				(and
					(or
						(>= (+ (* (x) (a1 ?b)) (* (y) (b1 ?b))) (c1 ?b))
						(>= (+ (* (x) (a2 ?b)) (* (y) (b2 ?b))) (c2 ?b))
						(>= (+ (* (x) (a3 ?b)) (* (y) (b3 ?b))) (c3 ?b))
						(>= (+ (* (x) (a4 ?b)) (* (y) (b4 ?b))) (c4 ?b))
					)
				)
			)
			(>= (+ (x) 1) (minx))
			(<= (+ (x) 1) (maxx))
			(>= (+ (y) 0) (miny))
			(<= (+ (y) 0) (maxy))
		)
		:effect (and
			(increase (x) 1)
			(increase (y) 0)
		)
	)

	(:action move_0_1
		:parameters ()
		:precondition (and
			; (forall
			; 	(?b - obstacle)
			; 	(or
			; 		(>= (+ (* (x) (a1 ?b)) (* (y) (b1 ?b))) (c1 ?b))
			; 		(>= (+ (* (x) (a2 ?b)) (* (y) (b2 ?b))) (c2 ?b))
			; 		(>= (+ (* (x) (a3 ?b)) (* (y) (b3 ?b))) (c3 ?b))
			; 		(>= (+ (* (x) (a4 ?b)) (* (y) (b4 ?b))) (c4 ?b))
			; 	)
			; )
			(>= (+ (x) 0) (minx))
			(<= (+ (x) 0) (maxx))
			(>= (+ (y) 1) (miny))
			(<= (+ (y) 1) (maxy))
		)
		:effect (and
			(increase (x) 0)
			(increase (y) 1)
		)
	)

	(:action move_-1_0
		:parameters ()
		:precondition (and
			; (forall
			; 	(?b - obstacle)
			; 	(or
			; 		(>= (+ (* (x) (a1 ?b)) (* (y) (b1 ?b))) (c1 ?b))
			; 		(>= (+ (* (x) (a2 ?b)) (* (y) (b2 ?b))) (c2 ?b))
			; 		(>= (+ (* (x) (a3 ?b)) (* (y) (b3 ?b))) (c3 ?b))
			; 		(>= (+ (* (x) (a4 ?b)) (* (y) (b4 ?b))) (c4 ?b))
			; 	)
			; )
			(>= (+ (x) -1) (minx))
			(<= (+ (x) -1) (maxx))
			(>= (+ (y) 0) (miny))
			(<= (+ (y) 0) (maxy))
		)
		:effect (and
			(increase (x) -1)
			(increase (y) 0)
		)
	)

	(:action move_0_-1
		:parameters ()
		:precondition (and
			; (forall
			; 	(?b - obstacle)
			; 	(or
			; 		(>= (+ (* (x) (a1 ?b)) (* (y) (b1 ?b))) (c1 ?b))
			; 		(>= (+ (* (x) (a2 ?b)) (* (y) (b2 ?b))) (c2 ?b))
			; 		(>= (+ (* (x) (a3 ?b)) (* (y) (b3 ?b))) (c3 ?b))
			; 		(>= (+ (* (x) (a4 ?b)) (* (y) (b4 ?b))) (c4 ?b))
			; 	)
			; )
			(>= (+ (x) 0) (minx))
			(<= (+ (x) 0) (maxx))
			(>= (+ (y) -1) (miny))
			(<= (+ (y) -1) (maxy))
		)
		:effect (and
			(increase (x) 0)
			(increase (y) -1)
		)
	)

	(:constraint obstacle
		:parameters (?b - obstacle)
		:condition (or
			(>= (+ (* (x) (a1 ?b)) (* (y) (b1 ?b))) (c1 ?b))
			(>= (+ (* (x) (a2 ?b)) (* (y) (b2 ?b))) (c2 ?b))
			(>= (+ (* (x) (a3 ?b)) (* (y) (b3 ?b))) (c3 ?b))
			(>= (+ (* (x) (a4 ?b)) (* (y) (b4 ?b))) (c4 ?b))
		)
	)
)