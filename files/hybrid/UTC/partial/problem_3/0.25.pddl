(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init
		(= (queue r7s) 20.0)
		(active ter2 r5)
		(active ter2 r7n)
		(= (token ter1) 10.0)
		(availableflow r7n r9 ter2)
		(availableflow r3 r5 ter1)
		(= (flow r5 r9 ter2) 2.0)
		(= (mingreentime ter1) 5.0)
		(= (max_queue r5) 70.0)
		(= (max_queue r8) 1000.0)
		(= (max_queue r7n) 50.0)
		(bufferconnected buf0 r1)
		(= (max_queue r3) 1000.0)
		(= (queue r7n) 20.0)
		(active ter1 r2)
		(= (queue r3) 100.0)
		(availableflow r6 r9 ter2)
		(= (greentime ter3) 0.0)
		(= (maxgreentime ter1) 25.0)
	)
	(:goal
			(and
				(< (queue r1) 20.0)
				(< (queue r2) 20.0)
				(< (queue r3) 20.0)
			)
	)
)