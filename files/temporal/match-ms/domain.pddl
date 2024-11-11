(define (domain match_makespan)
	(:requirements :fluents :equality :typing :durative-actions :negative-preconditions)

	(:types
		Match Fuse
	)

	(:predicates
		(handfree)
		(match_unused ?m - Match)
		(fuse_mended ?f - Fuse)
		(dark)
		(light)
	)

	(:functions
		(light_duration ?m - Match)
		(mend_duration ?f - Fuse)
	)

	(:durative-action zlight_match
		:parameters (?m - Match)
		:duration (= ?duration (light_duration ?m))
		:condition (and
			(at start (and
					(match_unused ?m)
					(dark)))
		)
		:effect (and
			(at start (and
					(not (match_unused ?m))
					(not (dark))
					(light)))
			(at end (and
					(dark)
					(not (light))))
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
					(handfree)))
		)
	)
)