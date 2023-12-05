(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 r11 r12 r13 r14 r15 r16 r17 r18 r19 r20 - road
		buf0 buf1 buf2 - buffer
	)
	(:init
	)
	(:goal
			(and
				(< (queue r4) 20.0)
			)
	)
)