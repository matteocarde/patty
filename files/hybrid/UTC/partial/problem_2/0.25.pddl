(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init
		(= (flow r3 r5 ter1) 2.0)
		(= (tokenvalue r5 ter2) 10.0)
		(availableflow r6 r7s ter2)
		(= (queue r7s) 20.0)
		(active ter3 r7s)
		(= (token ter3) 10.0)
		(availableflow r2 r5 ter1)
		(= (max_queue r4) 80.0)
		(active ter1 r3)
		(availableflow r1 r5 ter1)
		(active ter2 r7n)
		(= (queue r3) 50.0)
		(= (flow r6 r9 ter2) 2.0)
		(= (saturated_queue r2) 10.0)
		(availableflow r6 r9 ter2)
		(availableflow r7s r10 ter3)
		(= (greentime ter2) 0.0)
		(= (flow r2 r5 ter1) 2.0)
		(= (queue r7n) 20.0)
	)
	(:goal
			(and
				(< (queue r1) 10.0)
				(< (queue r2) 10.0)
				(< (queue r3) 10.0)
			)
	)
)