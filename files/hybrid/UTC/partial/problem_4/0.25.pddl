(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init
		(= (tokenvalue r7s ter3) 10.0)
		(= (flow r8 r10 ter3) 2.0)
		(= (flow r3 r5 ter1) 2.0)
		(= (greentime ter1) 0.0)
		(= (flow r6 r9 ter2) 2.0)
		(active ter1 r2)
		(= (tokenvalue r2 ter1) 20.0)
		(= (tokenvalue r8 ter3) 20.0)
		(= (tokenvalue r3 ter1) 30.0)
		(= (tokenvalue r5 ter2) 10.0)
		(= (greentime ter3) 0.0)
		(= (max_queue r6) 1000.0)
		(= (maxgreentime ter3) 25.0)
		(= (flow r2 r5 ter1) 2.0)
		(availableflow r8 r10 ter3)
		(availableflow r7s r10 ter3)
		(= (max_queue r2) 1000.0)
		(= (token ter3) 10.0)
		(availableflow r5 r7s ter2)
	)
	(:goal
			(and
				(< (queue r1) 20.0)
				(< (queue r2) 20.0)
				(< (queue r3) 20.0)
				(< (queue r5) 20.0)
				(< (queue r7s) 20.0)
			)
	)
)