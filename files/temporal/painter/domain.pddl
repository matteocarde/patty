(define (domain new)
	(:requirements :fluents :equality :typing :durative-actions)

	(:types
		Item Treatment - object
	)

	(:predicates
		(busy)
		(not_busy)
		(treated ?i - Item ?t - Treatment)
		(not_treated ?i - Item ?t - Treatment)
		(started ?i - Item ?t - Treatment)
		(not_started ?i - Item ?t - Treatment)
		(ready ?i - Item ?t - Treatment)
		(consecutive ?t - Treatment ?next - Treatment)
		(clip_s_1 ?i - Item ?t - Treatment ?next - Treatment)
		(clip_c_1 ?i - Item ?t - Treatment ?next - Treatment)
		(clip_e_1 ?i - Item ?t - Treatment ?next - Treatment)
		(clip_s_2 ?i - Item ?t - Treatment ?next - Treatment)
		(clip_c_2 ?i - Item ?t - Treatment ?next - Treatment)
		(clip_e_2 ?i - Item ?t - Treatment ?next - Treatment)
	)

	(:functions
		(counter ?t - Treatment)
		(item_id ?i - Item)
	)

	(:durative-action make_treatment1
		:parameters (?i - Item ?t - Treatment ?next - Treatment)
		:duration (= ?duration 4)
		:condition (and
			(at start (and
					(= (counter ?t) (item_id ?i))
					(not_busy)
					(consecutive ?t ?next)
					(not_treated ?i ?t)
					(not_started ?i ?t)
					(ready ?i ?t)))
			(at end (clip_c_1 ?i ?t ?next))
		)
		:effect (and
			(at start (and
					(increase (counter ?t) 1)
					(busy)
					(not (not_busy))
					(not (not_started ?i ?t))
					(started ?i ?t)))
			(at end (and
					(clip_s_1 ?i ?t ?next)
					(treated ?i ?t)
					(not (not_treated ?i ?t))
					(not_busy)
					(not (busy))))
		)
	)

	(:durative-action zclip_1
		:parameters (?i - Item ?t - Treatment ?next - Treatment)
		:duration (= ?duration 0.002)
		:condition (and
			(at end (and
					(clip_s_1 ?i ?t ?next)
					(clip_e_1 ?i ?t ?next)))
			(over all (clip_c_1 ?i ?t ?next))
		)
		:effect (and
			(at start (clip_c_1 ?i ?t ?next))
			(at end (and
					(not (clip_s_1 ?i ?t ?next))
					(not (clip_c_1 ?i ?t ?next))
					(not (clip_e_1 ?i ?t ?next))))
		)
	)

	(:durative-action make_treatment2
		:parameters (?i - Item ?t - Treatment ?next - Treatment)
		:duration (= ?duration 6)
		:condition (and
			(at start (clip_c_1 ?i ?t ?next))
			(at end (clip_c_2 ?i ?t ?next))

		)
		:effect (and
			(at start (clip_e_1 ?i ?t ?next))
			(at end (and
					(clip_s_2 ?i ?t ?next)
					(ready ?i ?next)))
		)
	)

	(:durative-action zclip_2
		:parameters (?i - Item ?t - Treatment ?next - Treatment)
		:duration (= ?duration 0.002)
		:condition (and
			(at end (and (clip_s_2 ?i ?t ?next) (clip_e_2 ?i ?t ?next)))
			(over all (clip_c_2 ?i ?t ?next))
		)
		:effect (and
			(at start (clip_c_2 ?i ?t ?next))
			(at end (and
					(not (clip_s_2 ?i ?t ?next))
					(not (clip_c_2 ?i ?t ?next))
					(not (clip_e_2 ?i ?t ?next))))
		)
	)

	(:durative-action make_treatment3
		:parameters (?i - Item ?t - Treatment ?next - Treatment)
		:duration (= ?duration 5)
		:condition (and
			(at start (clip_c_2 ?i ?t ?next))
			(at end (started ?i ?next))
		)
		:effect (and
			(at start (clip_e_2 ?i ?t ?next))
		)
	)

)