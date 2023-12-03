(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7n r7s r8 r9 r10 - road
		buf0 - buffer
	)
	(:init

		(= (queue r1) 60)
		(= (queue r2) 20)
		(= (queue r3) 50)
		(= (queue r4) 30)
		(= (queue r5) 10)
		(= (queue r6) 30)
		(= (queue r7s) 20)
		(= (queue r7n) 20)
		(= (queue r8) 25)

		(= (queue r9) 0)
		(= (queue r10) 0)

		(bufferconnected buf0 r1)
		(= (max_queue r1) 1000)
		(= (max_queue r2) 1000)
		(= (max_queue r3) 1000)
		(= (max_queue r4) 80)
		(= (max_queue r5) 70)
		(= (max_queue r6) 1000)
		(= (max_queue r7n) 50)
		(= (max_queue r7s) 50)
		(= (max_queue r8) 1000)
		(= (max_queue r9) 10000)
		(= (max_queue r10) 10000)

		; (= 20 20)
		; (= (saturated_queue r2) 20)
		; (= (saturated_queue r3) 20)

		;; intersection 1
		(= (greentime ter1) 0)
		(= (token ter1) 10)
		(= (maxtoken ter1) 30)
		(= (tokenvalue r1 ter1) 10)
		(= (tokenvalue r2 ter1) 20)
		(= (tokenvalue r3 ter1) 30)
		(= (maxgreentime ter1) 25)
		(= (mingreentime ter1) 5)
		(= (flow r2 r5 ter1) 2)
		;;	(= (flow r2 r4 ter1) 2)
		(= (flow r1 r5 ter1) 2)
		;;	(= (flow r1 r4 ter1) 2)
		(= (flow r3 r5 ter1) 2)
		;;	(= (flow r3 r4 ter1) 2)
		(availableflow r2 r5 ter1)
		;;	(availableflow r2 r4 ter1)
		(availableflow r3 r5 ter1)
		;;	(availableflow r3 r4 ter1)
		(availableflow r1 r5 ter1)
		;;	(availableflow r1 r4 ter1)
		(active ter1 r1)
		(active ter1 r2)
		(active ter1 r3)

		;; intersection 3
		(= (maxgreentime ter3) 25)
		(= (mingreentime ter3) 5)
		(= (greentime ter3) 0)
		(= (token ter3) 10)
		(= (maxtoken ter3) 20)
		;; 	(= (tokenvalue r4 ter3)  10)
		(= (tokenvalue r7s ter3) 10)
		(= (tokenvalue r8 ter3) 20)

		;;	(= (flow r4 r10 ter3) 2)
		;;	(= (flow r4 r7n ter3) 2)
		(= (flow r8 r10 ter3) 2)
		(= (flow r8 r7n ter3) 2)
		(= (flow r7s r10 ter3) 2)

		;;	(availableflow r4 r10 ter3)
		;;	(availableflow r4 r7n ter3)
		(availableflow r8 r10 ter3)
		(availableflow r8 r7n ter3)
		(availableflow r7s r10 ter3)

		;;	(active ter3 r4)
		(active ter3 r8)
		(active ter3 r7s)

		(= (greentime ter2) 0)
		(= (token ter2) 10)
		(= (maxtoken ter2) 30)
		(= (tokenvalue r5 ter2) 10)
		(= (tokenvalue r6 ter2) 20)
		(= (tokenvalue r7n ter2) 30)
		(= (maxgreentime ter2) 25)
		(= (mingreentime ter2) 5)
		(= (flow r5 r9 ter2) 2)
		(= (flow r5 r7s ter2) 2)
		(= (flow r7n r9 ter2) 2)
		(= (flow r6 r9 ter2) 2)
		(= (flow r6 r7s ter2) 2)
		(availableflow r5 r9 ter2)
		(availableflow r5 r7s ter2)
		(availableflow r6 r9 ter2)
		(availableflow r6 r7s ter2)
		(availableflow r7n r9 ter2)
		(active ter2 r5)
		(active ter2 r6)
		(active ter2 r7n)

	)
	(:goal
		(and
			(< (queue r1) 20)
			(< (queue r2) 20)
			(< (queue r3) 20)
		)
	)
)