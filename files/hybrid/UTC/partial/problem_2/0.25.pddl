(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init
		(= (flow r3 r5 ter1) 2.0)
		(active ter3 r8)
		(= (tokenvalue r1 ter1) 10.0)
		(= (flow r7n r9 ter2) 2.0)
		(= (queue r7n) 20.0)
		(= (max_queue r10) 10000.0)
		(active ter1 r1)
		(= (queue r5) 10.0)
		(active ter3 r7s)
		(availableflow r3 r5 ter1)
		(= (token ter2) 10.0)
		(= (queue r2) 20.0)
		(availableflow r7n r9 ter2)
		(availableflow r8 r7n ter3)
		(availableflow r5 r9 ter2)
		(availableflow r1 r5 ter1)
		(= (mingreentime ter1) 5.0)
		(= (flow r6 r7s ter2) 2.0)
		(= (maxtoken ter1) 30.0)
	)
	(:goal
			(and
				(< (queue r1) 10.0)
				(< (queue r2) 10.0)
				(< (queue r3) 10.0)
			)
	)
)