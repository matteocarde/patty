(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init
		(availableflow r5 r7s ter2)
		(active ter1 r1)
		(= (queue r3) 50.0)
		(= (flow r7s r10 ter3) 2.0)
		(= (max_queue r1) 1000.0)
		(= (tokenvalue r8 ter3) 20.0)
		(availableflow r8 r7n ter3)
		(= (queue r10) 0.0)
		(availableflow r5 r9 ter2)
		(= (flow r3 r5 ter1) 2.0)
		(= (flow r5 r7s ter2) 2.0)
		(= (tokenvalue r7n ter2) 30.0)
		(availableflow r3 r5 ter1)
		(availableflow r6 r9 ter2)
		(= (maxgreentime ter2) 25.0)
		(= (token ter2) 10.0)
		(= (greentime ter1) 0.0)
		(= (flow r5 r9 ter2) 2.0)
		(= (tokenvalue r2 ter1) 20.0)
	)
	(:goal
			(and
				(< (queue r1) 20.0)
				(< (queue r2) 20.0)
				(< (queue r3) 20.0)
			)
	)
)