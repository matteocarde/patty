(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init
		(= (queue r8) 25.0)
		(= (tokenvalue r7n ter2) 30.0)
		(availableflow r1 r5 ter1)
		(= (max_queue r5) 70.0)
		(= (token ter1) 10.0)
		(= (tokenvalue r8 ter3) 20.0)
		(= (queue r2) 20.0)
		(= (flow r2 r5 ter1) 2.0)
		(= (token ter2) 10.0)
		(active ter2 r7n)
		(= (max_queue r10) 10000.0)
		(availableflow r5 r9 ter2)
		(= (maxtoken ter2) 30.0)
		(bufferconnected buf0 r1)
		(active ter2 r6)
		(active ter3 r8)
		(= (maxtoken ter1) 30.0)
		(= (max_queue r9) 10000.0)
		(= (flow r6 r9 ter2) 2.0)
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