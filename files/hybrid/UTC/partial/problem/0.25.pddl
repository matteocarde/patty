(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init
		(= (maxtoken ter2) 30.0)
		(= (flow r2 r5 ter1) 2.0)
		(= (tokenvalue r2 ter1) 20.0)
		(= (token ter1) 10.0)
		(availableflow r3 r5 ter1)
		(= (token ter2) 10.0)
		(= (tokenvalue r3 ter1) 30.0)
		(= (flow r3 r5 ter1) 2.0)
		(= (flow r7s r10 ter3) 2.0)
		(active ter1 r2)
		(= (greentime ter2) 0.0)
		(availableflow r8 r7n ter3)
		(availableflow r1 r5 ter1)
		(= (max_queue r7s) 50.0)
		(= (flow r1 r5 ter1) 2.0)
		(= (max_queue r9) 10000.0)
		(= (queue r7s) 20.0)
		(availableflow r7n r9 ter2)
		(= (queue r1) 60.0)
	)
	(:goal
			(and
				(< (queue r1) 20.0)
				(< (queue r2) 20.0)
				(< (queue r3) 20.0)
			)
	)
)