(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init
		(= (flow r7s r10 ter3) 2.0)
		(= (token ter2) 10.0)
		(active ter1 r3)
		(availableflow r7n r9 ter2)
		(availableflow r7s r10 ter3)
		(= (flow r6 r7s ter2) 2.0)
		(active ter2 r5)
		(availableflow r5 r9 ter2)
		(= (maxgreentime ter2) 25.0)
		(= (mingreentime ter2) 5.0)
		(= (maxtoken ter1) 30.0)
		(= (tokenvalue r6 ter2) 20.0)
		(= (flow r5 r9 ter2) 2.0)
		(active ter3 r8)
		(active ter3 r7s)
		(availableflow r5 r7s ter2)
		(= (queue r2) 40.0)
		(= (flow r7n r9 ter2) 2.0)
		(= (max_queue r4) 80.0)
	)
	(:goal
			(and
				(< (queue r1) 20.0)
				(< (queue r2) 20.0)
				(< (queue r3) 20.0)
			)
	)
)