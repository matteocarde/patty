(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init
		(availableflow r8 r10 ter3)
		(bufferconnected buf0 r1)
		(= (queue r6) 30.0)
		(= (queue r3) 50.0)
		(= (max_queue r6) 1000.0)
		(= (max_queue r9) 10000.0)
		(= (max_queue r10) 10000.0)
		(= (queue r7n) 20.0)
		(= (flow r6 r7s ter2) 2.0)
		(= (max_queue r2) 1000.0)
		(= (tokenvalue r7s ter3) 10.0)
		(availableflow r2 r5 ter1)
		(= (maxtoken ter3) 20.0)
		(active ter3 r7s)
		(active ter2 r5)
		(= (queue r10) 0.0)
		(= (max_queue r3) 1000.0)
		(= (tokenvalue r6 ter2) 20.0)
		(= (flow r1 r5 ter1) 2.0)
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