(define (domain paco3d)

	;;;; MI SONO INCASINATO CON IL DISCORSO DEL BLOCCO A 360 GRADI O MENO, E L'USO DEI 2 ANGOLI.

	;(:requirements :fluents :durative-actions :duration-inequalities :adl :typing :time)
	(:types
		link axis arm
	)

	(:predicates
		(in-use ?a - arm) ;;serve per dire se le gripper sono in uso o meno
		(connected ?a - arm ?l1 - link ?l2 - link)
		(affects ?a - arm ?l1 - link ?l2 - link)
		(freeToMove ?a - arm ?l2 - link)
		(increasing_angle-baxter ?a - arm ?l2 - link ?x - axis)
		(decreasing_angle-baxter ?a - arm ?l2 - link ?x - axis)
	)

	(:functions
		(angle ?a - arm ?l2 - link ?x - axis)
		(speed-i ?a - arm)
		(speed-d ?a - arm)
	)

	;;; I MOVIMENTI SONO MODELLIZZATI USANDO AZIONE + PROCESSO + AZIONE. FUNZIONA IN INCREASE ED IN DECREASE.

	(:action start_movement_increase
		:parameters (?a - arm ?l1 - link ?l2 - link ?x - axis)
		:precondition (and
			(connected ?a ?l1 ?l2)
			(not (in-use ?a))
		)
		:effect (and
			(in-use ?a)
			(not (freeToMove ?a ?l2))
			(not (freeToMove ?a ?l1))
			(increasing_angle-baxter ?a ?l2 ?x)
		)
	)

	(:action stop_movement_increase
		:parameters (?a - arm ?l1 - link ?l2 - link ?x - axis)
		:precondition (and
			(increasing_angle-baxter ?a ?l2 ?x)
			(connected ?a ?l1 ?l2)
		)
		:effect (and
			(not (in-use ?a))
			(freeToMove ?a ?l2)
			(freeToMove ?a ?l1)
			(not (increasing_angle-baxter ?a ?l2 ?x))
		)
	)

	(:process move_angle_increase
		:parameters (?a - arm ?l2 - link ?x - axis)
		:precondition (and
			(increasing_angle-baxter ?a ?l2 ?x)
		)
		:effect (and
			(increase (angle ?a ?l2 ?x) (* #t (speed-i ?a)))
		)
	)

	(:action start_movement_decrease
		:parameters (?a - arm ?l1 - link ?l2 - link ?x - axis)
		:precondition (and
			(connected ?a ?l1 ?l2)
			(not (in-use ?a))
		)
		:effect (and
			(in-use ?a)
			(not (freeToMove ?a ?l2))
			(not (freeToMove ?a ?l1))
			(decreasing_angle-baxter ?a ?l2 ?x)
		)
	)

	(:action stop_movement_decrease
		:parameters (?a - arm ?l1 - link ?l2 - link ?x - axis)
		:precondition (and
			(decreasing_angle-baxter ?a ?l2 ?x)
			(connected ?a ?l1 ?l2)
		)
		:effect (and
			(not (in-use ?a))
			(freeToMove ?a ?l2)
			(freeToMove ?a ?l1)
			(not (decreasing_angle-baxter ?a ?l2 ?x))
		)
	)

	(:process move_angle_decrease
		:parameters (?a - arm ?l2 - link ?x - axis)
		:precondition (and
			(decreasing_angle-baxter ?a ?l2 ?x)
		)
		:effect (and
			(decrease (angle ?a ?l2 ?x) (* #t (speed-d ?a)))
		)
	)

	;;; I MOVIMENTI SONO PROPAGATI A TUTTI GLI ANGOLI AFFECTED. 

	(:process propagate_move_angle_decrease
		:parameters (?a - arm ?l2 - link ?l3 - link ?x - axis)
		:precondition (and
			(decreasing_angle-baxter ?a ?l2 ?x)
			(affects ?a ?l2 ?l3)
		)
		:effect (and
			(decrease (angle ?a ?l3 ?x) (* #t (speed-d ?a)))
		)
	)

	(:process propagate_move_angle_increase
		:parameters (?a - arm ?l2 - link ?l3 - link ?x - axis)
		:precondition (and
			(increasing_angle-baxter ?a ?l2 ?x)
			(affects ?a ?l2 ?l3)
		)
		:effect (and
			(increase (angle ?a ?l3 ?x) (* #t (speed-i ?a)))
		)
	)

	;;;; I SEGUENTI EVENTI AZZERANO O METTONO A 360 -- A SECONDA DELLA DIREZIONE -- GLI ANGOLI

	(:event back-to-zero
		:parameters (?a - arm ?l3 - link ?x - axis)
		:precondition (and(> (angle ?a ?l3 ?x) 360))
		:effect (and(assign (angle ?a ?l3 ?x) 0))
	)

	(:event back-to-360
		:parameters (?a - arm ?l3 - link ?x - axis)
		:precondition (and(< (angle ?a ?l3 ?x) 0))
		:effect (and(assign (angle ?a ?l3 ?x) 360))
	)

)