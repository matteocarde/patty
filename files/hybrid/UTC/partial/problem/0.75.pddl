(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init
		(= (greentime ter3) 0.0)
		(= (queue r7s) 20.0)
		(active ter3 r8)
		(availableflow r6 r9 ter2)
		(= (max_queue r7s) 50.0)
		(= (flow r7s r10 ter3) 2.0)
		(= (tokenvalue r6 ter2) 20.0)
		(= (maxtoken ter3) 20.0)
		(availableflow r1 r5 ter1)
		(= (flow r7n r9 ter2) 2.0)
		(= (flow r1 r5 ter1) 2.0)
		(= (flow r2 r5 ter1) 2.0)
		(active ter2 r6)
		(= (token ter3) 10.0)
		(= (queue r3) 50.0)
		(= (max_queue r10) 10000.0)
		(= (mingreentime ter3) 5.0)
		(= (queue r1) 60.0)
		(= (mingreentime ter2) 5.0)
		(= (tokenvalue r2 ter1) 20.0)
		(= (queue r9) 0.0)
		(= (max_queue r5) 70.0)
		(availableflow r6 r7s ter2)
		(availableflow r7n r9 ter2)
		(= (tokenvalue r1 ter1) 10.0)
		(= (max_queue r7n) 50.0)
		(= (maxgreentime ter2) 25.0)
		(availableflow r3 r5 ter1)
		(= (queue r6) 30.0)
		(active ter1 r1)
		(= (queue r4) 30.0)
		(= (tokenvalue r7n ter2) 30.0)
		(= (maxtoken ter1) 30.0)
		(= (token ter1) 10.0)
		(= (greentime ter2) 0.0)
		(= (tokenvalue r5 ter2) 10.0)
		(= (max_queue r6) 1000.0)
		(= (max_queue r3) 1000.0)
		(availableflow r8 r10 ter3)
		(= (maxtoken ter2) 30.0)
		(= (flow r5 r7s ter2) 2.0)
		(= (maxgreentime ter1) 25.0)
		(= (queue r5) 10.0)
		(= (queue r10) 0.0)
		(active ter1 r2)
		(= (tokenvalue r8 ter3) 20.0)
		(= (token ter2) 10.0)
		(= (tokenvalue r3 ter1) 30.0)
		(= (flow r8 r10 ter3) 2.0)
		(= (mingreentime ter1) 5.0)
		(availableflow r8 r7n ter3)
		(= (tokenvalue r7s ter3) 10.0)
		(= (flow r6 r9 ter2) 2.0)
		(= (maxgreentime ter3) 25.0)
		(= (max_queue r2) 1000.0)
		(availableflow r5 r9 ter2)
		(= (max_queue r1) 1000.0)
	)
	(:goal
			(and
				(< (queue r1) 20.0)
				(< (queue r2) 20.0)
				(< (queue r3) 20.0)
			)
	)
)