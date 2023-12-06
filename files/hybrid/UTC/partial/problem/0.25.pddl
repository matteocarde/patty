(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init
		(= (token ter3) 10.0)
		(= (flow r1 r5 ter1) 2.0)
		(= (tokenvalue r6 ter2) 20.0)
		(availableflow r7s r10 ter3)
		(availableflow r6 r9 ter2)
		(= (queue r4) 30.0)
		(= (token ter1) 10.0)
		(= (tokenvalue r8 ter3) 20.0)
		(= (queue r3) 50.0)
		(availableflow r6 r7s ter2)
		(= (max_queue r3) 1000.0)
		(active ter2 r6)
		(active ter2 r7n)
		(active ter2 r5)
		(availableflow r7n r9 ter2)
		(active ter3 r7s)
		(= (flow r5 r9 ter2) 2.0)
		(= (flow r3 r5 ter1) 2.0)
		(availableflow r8 r7n ter3)
	)
	(:goal
			(and
				(< (queue r1) 20.0)
				(< (queue r2) 20.0)
				(< (queue r3) 20.0)
			)
	)
)