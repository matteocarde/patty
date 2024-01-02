(define (domain match_action_cost)
	(:requirements :fluents :equality :typing :durative-actions :negative-preconditions)

	(:types
		Match Fuse
	)

	(:predicates
		(handfree)
		(match_unused ?m - Match)
		(fuse_mended ?f - Fuse)
		(light)
	)

	(:functions
		(total-cost)
		(match_cost ?m - Match)
		(light_duration ?m - Match)
		(mend_duration ?f - Fuse)
	)

	(:durative-action light_match
		:parameters (?m - Match)
		:duration (= ?duration (light_duration ?m))
		:condition (and
			(at start (and
					(match_unused ?m)))
		)
		:effect (and
			(at start (and
					(not (match_unused ?m))
					(light)))
			(at end (and
					(not (light))
					(increase (total-cost) (match_cost ?m))))
		)
	)

	(:durative-action mend_fuse
		:parameters (?f - Fuse)
		:duration (= ?duration (mend_duration ?f))
		:condition (and
			(at start (and
					(handfree)
					(light)))
			(over all (light))
		)
		:effect (and
			(at start (and
					(not (handfree))))
			(at end (and
					(fuse_mended ?f)
					(handfree)
					(increase (total-cost) 1)))
		)
	)
)