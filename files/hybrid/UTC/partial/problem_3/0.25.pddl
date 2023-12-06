(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init
		(= (greentime ter1) 0.0)
		(= (flow r7n r9 ter2) 2.0)
		(= (maxgreentime ter2) 25.0)
		(= (maxgreentime ter3) 25.0)
		(= (maxtoken ter3) 20.0)
		(= (maxgreentime ter1) 25.0)
		(= (queue r6) 30.0)
		(= (mingreentime ter2) 5.0)
		(= (flow r6 r9 ter2) 2.0)
		(= (max_queue r8) 1000.0)
		(= (max_queue r7s) 50.0)
		(= (mingreentime ter3) 5.0)
		(availableflow r8 r10 ter3)
		(active ter1 r3)
		(= (max_queue r3) 1000.0)
		(= (queue r10) 0.0)
		(active ter1 r2)
		(= (queue r8) 25.0)
		(= (token ter2) 10.0)
	)
	(:goal
			(and
				(< (queue r1) 20.0)
				(< (queue r2) 20.0)
				(< (queue r3) 20.0)
			)
	)
)