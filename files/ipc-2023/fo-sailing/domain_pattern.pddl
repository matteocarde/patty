(define (domain sailing_ln)
	(:types
		object
		boat - object
		person - object
	)
	(:constants
		b0 - boat
		p0 - person
	)
	(:predicates
		(saved ?t - person)
		(dummy )
		(turn_go_est ?b - boat)
		(turn_go_south_east ?b - boat)
		(turn_save_person ?b - boat ?t - person)
		(turn_decelerate ?b - boat)
		(turn_go_south ?b - boat)
		(turn_accelerate ?b - boat)
		(turn_go_west ?b - boat)
		(turn_go_north_east ?b - boat)
		(turn_go_south_west ?b - boat)
		(turn_go_north_west ?b - boat)
	)
	(:functions
		(d ?t - person)
		(x ?b - boat)
		(y ?b - boat)
		(v ?b - boat)
	)
	(:action movecursor_go_est_b0_go_north_east_b0
		:parameters ()
		:precondition 
			(and
				(turn_go_est b0)
			)
		:effect (and
			(turn_go_north_east b0)
			(not (turn_go_est b0))
		)
	)
	(:action movecursor_go_west_b0_decelerate_b0
		:parameters ()
		:precondition 
			(and
				(turn_go_west b0)
			)
		:effect (and
			(turn_decelerate b0)
			(not (turn_go_west b0))
		)
	)
	(:action accelerate
		:parameters (?b - boat)
		:precondition 
			(and
				(<= (+ (v ?b) 1.0) 3.0)
				(turn_accelerate ?b)
			)
		:effect (and
			(increase (v ?b) 1.0)
		)
	)
	(:action movecursor_accelerate_b0_go_est_b0
		:parameters ()
		:precondition 
			(and
				(turn_accelerate b0)
			)
		:effect (and
			(turn_go_est b0)
			(not (turn_accelerate b0))
		)
	)
	(:action go_south
		:parameters (?b - boat)
		:precondition 
			(and
				(not (dummy))
				(turn_go_south ?b)
			)
		:effect (and
			(decrease (y ?b) (* (v ?b) 2.0))
		)
	)
	(:action save_person
		:parameters (?b - boat ?t - person)
		:precondition 
			(and
				(>= (+ (x ?b) (y ?b)) (d ?t))
				(>= (- (y ?b) (x ?b)) (d ?t))
				(<= (+ (x ?b) (y ?b)) (+ (d ?t) 25.0))
				(<= (- (y ?b) (x ?b)) (+ (d ?t) 25.0))
				(<= (v ?b) 1.0)
				(turn_save_person ?b ?t)
			)
		:effect (and
			(saved ?t)
		)
	)
	(:action decelerate
		:parameters (?b - boat)
		:precondition 
			(and
				(>= (- (v ?b) 1.0) 1.0)
				(turn_decelerate ?b)
			)
		:effect (and
			(decrease (v ?b) 1.0)
		)
	)
	(:action movecursor_go_north_east_b0_go_north_west_b0
		:parameters ()
		:precondition 
			(and
				(turn_go_north_east b0)
			)
		:effect (and
			(turn_go_north_west b0)
			(not (turn_go_north_east b0))
		)
	)
	(:action movecursor_go_south_b0_go_south_east_b0
		:parameters ()
		:precondition 
			(and
				(turn_go_south b0)
			)
		:effect (and
			(turn_go_south_east b0)
			(not (turn_go_south b0))
		)
	)
	(:action go_north_west
		:parameters (?b - boat)
		:precondition 
			(and
				(not (dummy))
				(turn_go_north_west ?b)
			)
		:effect (and
			(decrease (x ?b) (* (v ?b) 1.5))
			(increase (y ?b) (* (v ?b) 1.5))
		)
	)
	(:action go_est
		:parameters (?b - boat)
		:precondition 
			(and
				(not (dummy))
				(turn_go_est ?b)
			)
		:effect (and
			(increase (x ?b) (* (v ?b) 3.0))
		)
	)
	(:action movecursor_save_person_b0_p0_accelerate_b0
		:parameters ()
		:precondition 
			(and
				(turn_save_person b0 p0)
			)
		:effect (and
			(turn_accelerate b0)
			(not (turn_save_person b0 p0))
		)
	)
	(:action go_south_east
		:parameters (?b - boat)
		:precondition 
			(and
				(not (dummy))
				(turn_go_south_east ?b)
			)
		:effect (and
			(decrease (x ?b) (* (v ?b) 2.0))
			(decrease (y ?b) (* (v ?b) 2.0))
		)
	)
	(:action go_south_west
		:parameters (?b - boat)
		:precondition 
			(and
				(not (dummy))
				(turn_go_south_west ?b)
			)
		:effect (and
			(increase (x ?b) (* (v ?b) 2.0))
			(decrease (y ?b) (* (v ?b) 2.0))
		)
	)
	(:action go_north_east
		:parameters (?b - boat)
		:precondition 
			(and
				(not (dummy))
				(turn_go_north_east ?b)
			)
		:effect (and
			(increase (x ?b) (* (v ?b) 1.5))
			(increase (y ?b) (* (v ?b) 1.5))
		)
	)
	(:action movecursor_go_south_west_b0_go_west_b0
		:parameters ()
		:precondition 
			(and
				(turn_go_south_west b0)
			)
		:effect (and
			(turn_go_west b0)
			(not (turn_go_south_west b0))
		)
	)
	(:action go_west
		:parameters (?b - boat)
		:precondition 
			(and
				(not (dummy))
				(turn_go_west ?b)
			)
		:effect (and
			(decrease (x ?b) (* (v ?b) 3.0))
		)
	)
	(:action movecursor_go_north_west_b0_go_south_b0
		:parameters ()
		:precondition 
			(and
				(turn_go_north_west b0)
			)
		:effect (and
			(turn_go_south b0)
			(not (turn_go_north_west b0))
		)
	)
	(:action movecursor_decelerate_b0_save_person_b0_p0
		:parameters ()
		:precondition 
			(and
				(turn_decelerate b0)
			)
		:effect (and
			(turn_save_person b0 p0)
			(not (turn_decelerate b0))
		)
	)
	(:action movecursor_go_south_east_b0_go_south_west_b0
		:parameters ()
		:precondition 
			(and
				(turn_go_south_east b0)
			)
		:effect (and
			(turn_go_south_west b0)
			(not (turn_go_south_east b0))
		)
	)
)