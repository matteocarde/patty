(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init
		(active ter1 r2)
		(active ter2 r6)
		(= (mingreentime ter2) 5.0)
		(availableflow r8 r7n ter3)
		(= (flow r8 r10 ter3) 2.0)
		(availableflow r2 r5 ter1)
		(= (mingreentime ter3) 5.0)
		(= (max_queue r1) 1000.0)
		(= (mingreentime ter1) 5.0)
		(= (tokenvalue r3 ter1) 30.0)
		(active ter2 r5)
		(= (maxtoken ter3) 20.0)
		(availableflow r6 r9 ter2)
		(= (max_queue r7s) 50.0)
		(active ter3 r8)
		(= (max_queue r4) 80.0)
		(= (flow r3 r5 ter1) 2.0)
		(= (flow r1 r5 ter1) 2.0)
		(= (greentime ter2) 0.0)
		(= (maxgreentime ter3) 25.0)
		(availableflow r6 r7s ter2)
		(= (queue r8) 25.0)
		(= (flow r8 r7n ter3) 2.0)
		(active ter1 r3)
		(= (greentime ter3) 0.0)
		(active ter2 r7n)
		(availableflow r5 r7s ter2)
		(availableflow r1 r5 ter1)
		(= (tokenvalue r2 ter1) 20.0)
		(= (queue r7n) 20.0)
		(availableflow r7s r10 ter3)
		(= (queue r3) 50.0)
		(availableflow r5 r9 ter2)
		(= (queue r2) 20.0)
		(= (max_queue r10) 10000.0)
		(= (tokenvalue r8 ter3) 20.0)
		(= (max_queue r7n) 50.0)
		(= (tokenvalue r6 ter2) 20.0)
		(availableflow r8 r10 ter3)
	)
	(:goal
			(and
				(< (queue r1) 10.0)
				(< (queue r2) 10.0)
				(< (queue r3) 10.0)
			)
	)
)