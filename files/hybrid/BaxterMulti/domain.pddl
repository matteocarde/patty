(define (domain paco3d)

	;;;; MI SONO INCASINATO CON IL DISCORSO DEL BLOCCO A 360 GRADI O MENO, E L'USO DEI 2 ANGOLI.

	;(:requirements :fluents :durative-actions :duration-inequalities :adl :typing :time)
	(:types
		link axis arm
	)

	(:predicates
		(in-use ?a - arm) ;;serve per dire se le gripper sono in uso o meno
		(connected ?l1 - link ?l2 - link)
		(affects ?l1 - link ?l2 - link)
		(belongs ?l ?a)
		(freeToMove ?l2 - link)
		(increasing_angle-baxter ?l2 - link ?x - axis)
		(decreasing_angle-baxter ?l2 - link ?x - axis)
		(increasing_angle-gravity ?l2 - link)
		(decreasing_angle-gravity ?l2 - link)
		(alwaysfalse)
		(broken ?a - arm)
	)

	(:functions
		(angle ?l2 - link ?x - axis)
		(speed-i ?a - arm)
		(speed-d ?a - arm)
	)

	;;; I MOVIMENTI SONO MODELLIZZATI USANDO AZIONE + PROCESSO + AZIONE. FUNZIONA IN INCREASE ED IN DECREASE.

	(:action start_movement_increase
		:parameters (?l1 - link ?l2 - link ?x - axis ?a - arm)
		:precondition (and
			(belongs ?l1 ?a)
			(belongs ?l2 ?a)
			(connected ?l1 ?l2)
			(not (in-use ?a))
		)
		:effect (and
			(in-use ?a)
			(not (freeToMove ?l2))
			(not (freeToMove ?l1))
			(increasing_angle-baxter ?l2 ?x)
		)
	)

	(:action stop_movement_increase
		:parameters (?l1 - link ?l2 - link ?x - axis ?a - arm)
		:precondition (and
			(belongs ?l1 ?a)
			(belongs ?l2 ?a)
			(increasing_angle-baxter ?l2 ?x)
			(connected ?l1 ?l2)
		)
		:effect (and
			(not (in-use ?a))
			(freeToMove ?l2)
			(freeToMove ?l1)
			(not (increasing_angle-baxter ?l2 ?x))
		)
	)

	(:process move_angle_increase
		:parameters (?l2 - link ?x - axis ?a - arm)
		:precondition (and
			(belongs ?l2 ?a)
			(increasing_angle-baxter ?l2 ?x)
		)
		:effect (and
			(increase (angle ?l2 ?x) (* #t (speed-i ?a)))
		)
	)

	(:action start_movement_decrease
		:parameters (?l1 - link ?l2 - link ?x - axis ?a - arm)
		:precondition (and
			(belongs ?l1 ?a)
			(belongs ?l2 ?a)
			(connected ?l1 ?l2)
			(not (in-use ?a))
		)
		:effect (and
			(in-use ?a)
			(not (freeToMove ?l2))
			(not (freeToMove ?l1))
			(decreasing_angle-baxter ?l2 ?x)
		)
	)

	(:action stop_movement_decrease
		:parameters (?l1 - link ?l2 - link ?x - axis ?a - arm)
		:precondition (and
			(belongs ?l1 ?a)
			(belongs ?l2 ?a)
			(decreasing_angle-baxter ?l2 ?x)
			(connected ?l1 ?l2)
		)
		:effect (and
			(not (in-use ?a))
			(freeToMove ?l2)
			(freeToMove ?l1)
			(not (decreasing_angle-baxter ?l2 ?x))
		)
	)

	(:process move_angle_decrease
		:parameters (?l2 - link ?x - axis ?a - arm)
		:precondition (and
			(belongs ?l2 ?a)
			(decreasing_angle-baxter ?l2 ?x)
		)
		:effect (and
			(decrease (angle ?l2 ?x) (* #t (speed-d ?a)))
		)
	)

	;;; I MOVIMENTI SONO PROPAGATI A TUTTI GLI ANGOLI AFFECTED. 

	(:process propagate_move_angle_decrease
		:parameters (?l2 - link ?l3 - link ?x - axis ?a)
		:precondition (and
			(belongs ?l2 ?a)
			(belongs ?l3 ?a)
			(decreasing_angle-baxter ?l2 ?x)
			(affects ?l2 ?l3)
		)
		:effect (and
			(decrease (angle ?l3 ?x) (* #t (speed-d ?a)))
		)
	)

	(:process propagate_move_angle_increase
		:parameters (?l2 - link ?l3 - link ?x - axis ?a - arm)
		:precondition (and
			(belongs ?l2 ?a)
			(belongs ?l3 ?a)
			(increasing_angle-baxter ?l2 ?x)
			(affects ?l2 ?l3)
		)
		:effect (and
			(increase (angle ?l3 ?x) (* #t (speed-i ?a)))
		)
	)

	;;;; I SEGUENTI EVENTI AZZERANO O METTONO A 360 -- A SECONDA DELLA DIREZIONE -- GLI ANGOLI
	
	(:event back-to-zero
		:parameters (?l3 - link ?x - axis ?a - arm)
		:precondition (and
			(> (angle ?l3 ?x) 360)
		)
		:effect (and
			(assign (angle ?l3 ?x) 0)
		)
	)

	(:event back-to-360
		:parameters (?l3 - link ?x - axis ?a - arm)
		:precondition (and
			(< (angle ?l3 ?x) 0)
		)
		:effect (and
			(assign (angle ?l3 ?x) 360)
		)
	)

)