(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init
		(= (flow r8 r10 ter3) 2.0)
		(= (queue r3) 50.0)
		(= (max_queue r3) 1000.0)
		(= (tokenvalue r2 ter1) 20.0)
		(= (max_queue r6) 1000.0)
		(bufferconnected buf0 r1)
		(= (mingreentime ter3) 5.0)
		(= (flow r8 r7n ter3) 2.0)
		(= (tokenvalue r8 ter3) 20.0)
		(= (flow r7s r10 ter3) 2.0)
		(= (token ter2) 10.0)
		(= (flow r6 r7s ter2) 2.0)
		(active ter1 r3)
		(= (flow r5 r9 ter2) 2.0)
		(active ter2 r5)
		(= (max_queue r4) 80.0)
		(= (queue r10) 0.0)
		(= (max_queue r7s) 50.0)
		(= (tokenvalue r7s ter3) 10.0)
	)
	(:goal
			(and
				(< (queue r1) 10.0)
				(< (queue r2) 10.0)
				(< (queue r3) 10.0)
			)
	)
)