(define (domain farmland_ln)
	(:types
		object
		farm - object
	)
	(:constants
		farm0 farm1 farm2 farm3 - farm
	)
	(:predicates
		(dummy )
		(adj ?f1 - farm ?f2 - farm)
		(turn_move-by-car ?f1 - farm ?f2 - farm)
		(turn_move-slow ?f1 - farm ?f2 - farm)
		(turn_hire-car )
	)
	(:functions
		(num-of-cars )
		(cost )
		(x ?b - farm)
	)
	(:action movecursor_move-by-car_farm2_farm3_move-by-car_farm3_farm1
		:parameters ()
		:precondition 
			(and
				(turn_move-by-car farm2 farm3)
			)
		:effect (and
			(turn_move-by-car farm3 farm1)
			(not (turn_move-by-car farm2 farm3))
		)
	)
	(:action move-by-car
		:parameters (?f1 - farm ?f2 - farm)
		:precondition 
			(and
				(>= (x ?f1) (* 4.0 (num-of-cars)))
				(adj ?f1 ?f2)
				(turn_move-by-car ?f1 ?f2)
			)
		:effect (and
			(decrease (x ?f1) (* 4.0 (num-of-cars)))
			(increase (x ?f2) (* 4.0 (num-of-cars)))
			(increase (cost) (* 0.1 (* 4.0 (num-of-cars))))
		)
	)
	(:action movecursor_move-slow_farm1_farm0_move-slow_farm1_farm3
		:parameters ()
		:precondition 
			(and
				(turn_move-slow farm1 farm0)
			)
		:effect (and
			(turn_move-slow farm1 farm3)
			(not (turn_move-slow farm1 farm0))
		)
	)
	(:action movecursor_move-by-car_farm0_farm2_move-by-car_farm1_farm0
		:parameters ()
		:precondition 
			(and
				(turn_move-by-car farm0 farm2)
			)
		:effect (and
			(turn_move-by-car farm1 farm0)
			(not (turn_move-by-car farm0 farm2))
		)
	)
	(:action movecursor_move-by-car_farm2_farm0_move-by-car_farm2_farm3
		:parameters ()
		:precondition 
			(and
				(turn_move-by-car farm2 farm0)
			)
		:effect (and
			(turn_move-by-car farm2 farm3)
			(not (turn_move-by-car farm2 farm0))
		)
	)
	(:action movecursor_move-by-car_farm1_farm3_move-by-car_farm2_farm0
		:parameters ()
		:precondition 
			(and
				(turn_move-by-car farm1 farm3)
			)
		:effect (and
			(turn_move-by-car farm2 farm0)
			(not (turn_move-by-car farm1 farm3))
		)
	)
	(:action movecursor_move-by-car_farm1_farm0_move-by-car_farm1_farm3
		:parameters ()
		:precondition 
			(and
				(turn_move-by-car farm1 farm0)
			)
		:effect (and
			(turn_move-by-car farm1 farm3)
			(not (turn_move-by-car farm1 farm0))
		)
	)
	(:action movecursor_move-slow_farm3_farm2_hire-car
		:parameters ()
		:precondition 
			(and
				(turn_move-slow farm3 farm2)
			)
		:effect (and
			(turn_hire-car)
			(not (turn_move-slow farm3 farm2))
		)
	)
	(:action movecursor_move-by-car_farm0_farm1_move-by-car_farm0_farm2
		:parameters ()
		:precondition 
			(and
				(turn_move-by-car farm0 farm1)
			)
		:effect (and
			(turn_move-by-car farm0 farm2)
			(not (turn_move-by-car farm0 farm1))
		)
	)
	(:action movecursor_move-slow_farm2_farm3_move-slow_farm3_farm1
		:parameters ()
		:precondition 
			(and
				(turn_move-slow farm2 farm3)
			)
		:effect (and
			(turn_move-slow farm3 farm1)
			(not (turn_move-slow farm2 farm3))
		)
	)
	(:action move-slow
		:parameters (?f1 - farm ?f2 - farm)
		:precondition 
			(and
				(>= (x ?f1) 1.0)
				(adj ?f1 ?f2)
				(turn_move-slow ?f1 ?f2)
			)
		:effect (and
			(decrease (x ?f1) 1.0)
			(increase (x ?f2) 1.0)
		)
	)
	(:action movecursor_hire-car_move-slow_farm0_farm1
		:parameters ()
		:precondition 
			(and
				(turn_hire-car)
			)
		:effect (and
			(turn_move-slow farm0 farm1)
			(not (turn_hire-car))
		)
	)
	(:action movecursor_move-slow_farm2_farm0_move-slow_farm2_farm3
		:parameters ()
		:precondition 
			(and
				(turn_move-slow farm2 farm0)
			)
		:effect (and
			(turn_move-slow farm2 farm3)
			(not (turn_move-slow farm2 farm0))
		)
	)
	(:action movecursor_move-slow_farm3_farm1_move-slow_farm3_farm2
		:parameters ()
		:precondition 
			(and
				(turn_move-slow farm3 farm1)
			)
		:effect (and
			(turn_move-slow farm3 farm2)
			(not (turn_move-slow farm3 farm1))
		)
	)
	(:action hire-car
		:parameters ()
		:precondition 
			(and
				(not (dummy))
				(turn_hire-car)
			)
		:effect (and
			(increase (num-of-cars) 1.0)
		)
	)
	(:action movecursor_move-slow_farm0_farm1_move-slow_farm0_farm2
		:parameters ()
		:precondition 
			(and
				(turn_move-slow farm0 farm1)
			)
		:effect (and
			(turn_move-slow farm0 farm2)
			(not (turn_move-slow farm0 farm1))
		)
	)
	(:action movecursor_move-by-car_farm3_farm2_move-slow_farm2_farm0
		:parameters ()
		:precondition 
			(and
				(turn_move-by-car farm3 farm2)
			)
		:effect (and
			(turn_move-slow farm2 farm0)
			(not (turn_move-by-car farm3 farm2))
		)
	)
	(:action movecursor_move-slow_farm0_farm2_move-slow_farm1_farm0
		:parameters ()
		:precondition 
			(and
				(turn_move-slow farm0 farm2)
			)
		:effect (and
			(turn_move-slow farm1 farm0)
			(not (turn_move-slow farm0 farm2))
		)
	)
	(:action movecursor_move-slow_farm1_farm3_move-by-car_farm0_farm1
		:parameters ()
		:precondition 
			(and
				(turn_move-slow farm1 farm3)
			)
		:effect (and
			(turn_move-by-car farm0 farm1)
			(not (turn_move-slow farm1 farm3))
		)
	)
	(:action movecursor_move-by-car_farm3_farm1_move-by-car_farm3_farm2
		:parameters ()
		:precondition 
			(and
				(turn_move-by-car farm3 farm1)
			)
		:effect (and
			(turn_move-by-car farm3 farm2)
			(not (turn_move-by-car farm3 farm1))
		)
	)
)