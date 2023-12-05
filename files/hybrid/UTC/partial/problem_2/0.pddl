(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init
	)
	(:goal
			(and
				(< (queue r1) 10.0)
				(< (queue r2) 10.0)
				(< (queue r3) 10.0)
			)
	)
)