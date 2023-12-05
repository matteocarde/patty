(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 r11 r12 r13 r14 r15 r16 r17 r18 r19 r20 - road
		buf0 buf1 buf2 - buffer
	)
	(:init
		(= (queue r1) -23.0)
		(= (queue r2) 17.0)
		(= (queue r3) 22.0)
		(= (queue r4) 40.0)
		(= (queue r5) 9.0)
		(= (queue r6) 44.0)
		(= (queue r7) -8.0)
		(= (queue r8) 1.0)
		(= (queue r9) 16.0)
		(= (queue r10) 18.0)
		(= (queue r11) 102.0)
		(= (queue r12) -12.0)
		(= (queue r13) 77.0)
		(= (queue r14) -1.0)
		(= (queue r15) 56.0)
		(= (queue r16) -21.0)
		(= (queue r17) 24.0)
		(= (queue r18) 16.0)
		(= (queue r19) 61.0)
		(= (queue r20) 7.0)
		(= (carsinbuffer buf0) 43.0)
		(gotcars buf0)
		(bufferconnected buf0 r17)
		(= (carsinbuffer buf1) 16.0)
		(gotcars buf1)
		(bufferconnected buf1 r15)
		(= (carsinbuffer buf2) 39.0)
		(gotcars buf2)
		(bufferconnected buf2 r9)
		(= (max_queue r1) 110.0)
		(= (max_queue r2) 123.0)
		(= (max_queue r3) 116.0)
		(= (max_queue r4) 56.0)
		(= (max_queue r5) 100.0)
		(= (max_queue r6) 116.0)
		(= (max_queue r7) 87.0)
		(= (max_queue r8) 99.0)
		(= (max_queue r9) 78.0)
		(= (max_queue r10) 78.0)
		(= (max_queue r11) 104.0)
		(= (max_queue r12) 98.0)
		(= (max_queue r13) 107.0)
		(= (max_queue r14) 104.0)
		(= (max_queue r15) 98.0)
		(= (max_queue r16) 99.0)
		(= (max_queue r17) 114.0)
		(= (max_queue r18) 94.0)
		(= (max_queue r19) 115.0)
		(= (max_queue r20) 107.0)
		(= (saturated_queue r1) 80.0)
		(= (saturated_queue r2) 97.0)
		(= (saturated_queue r3) 120.0)
		(= (saturated_queue r4) 18.0)
		(= (saturated_queue r5) 118.0)
		(= (saturated_queue r6) 121.0)
		(= (saturated_queue r7) 101.0)
		(= (saturated_queue r8) 124.0)
		(= (saturated_queue r9) 88.0)
		(= (saturated_queue r10) 79.0)
		(= (saturated_queue r11) 81.0)
		(= (saturated_queue r12) 123.0)
		(= (saturated_queue r13) 94.0)
		(= (saturated_queue r14) 79.0)
		(= (saturated_queue r15) 117.0)
		(= (saturated_queue r16) 77.0)
		(= (saturated_queue r17) 103.0)
		(= (saturated_queue r18) 117.0)
		(= (saturated_queue r19) 96.0)
		(= (saturated_queue r20) 101.0)
		(= (greentime ter1) -1.0)
		(= (token ter1) 36.0)
		(= (maxtoken ter1) -3.0)
		(= (tokenvalue r8 ter1) 25.0)
		(= (tokenvalue r4 ter1) -12.0)
		(= (tokenvalue r2 ter1) 5.0)
		(= (tokenvalue r6 ter1) 29.0)
		(= (maxgreentime ter1) 29.0)
		(= (mingreentime ter1) 0.0)
		(= (flow r8 r3 ter1) 5.0)
		(= (flow r8 r5 ter1) 2.0)
		(= (flow r8 r7 ter1) -17.0)
		(= (flow r2 r1 ter1) 3.0)
		(= (flow r2 r5 ter1) 16.0)
		(= (flow r2 r7 ter1) 0.0)
		(= (flow r4 r1 ter1) -17.0)
		(= (flow r4 r3 ter1) 11.0)
		(= (flow r4 r7 ter1) 14.0)
		(= (flow r6 r1 ter1) -3.0)
		(= (flow r6 r3 ter1) 12.0)
		(= (flow r6 r5 ter1) 18.0)
		(availableflow r8 r3 ter1)
		(availableflow r8 r5 ter1)
		(availableflow r8 r7 ter1)
		(availableflow r2 r1 ter1)
		(availableflow r2 r5 ter1)
		(availableflow r2 r7 ter1)
		(availableflow r4 r1 ter1)
		(availableflow r4 r3 ter1)
		(availableflow r4 r7 ter1)
		(availableflow r6 r1 ter1)
		(availableflow r6 r3 ter1)
		(availableflow r6 r5 ter1)
		(active ter1 r8)
		(active ter1 r2)
		(active ter1 r4)
		(active ter1 r6)
		(= (greentime ter2) 5.0)
		(= (token ter2) 41.0)
		(= (maxtoken ter2) 16.0)
		(= (tokenvalue r5 ter2) -10.0)
		(= (tokenvalue r11 ter2) -9.0)
		(= (tokenvalue r9 ter2) 25.0)
		(= (tokenvalue r13 ter2) -1.0)
		(= (maxgreentime ter2) 10.0)
		(= (mingreentime ter2) -2.0)
		(= (flow r5 r10 ter2) -2.0)
		(= (flow r5 r14 ter2) -14.0)
		(= (flow r5 r12 ter2) 16.0)
		(= (flow r9 r4 ter2) -10.0)
		(= (flow r9 r14 ter2) 15.0)
		(= (flow r9 r12 ter2) 11.0)
		(= (flow r11 r10 ter2) -21.0)
		(= (flow r11 r4 ter2) -6.0)
		(= (flow r11 r14 ter2) 1.0)
		(= (flow r13 r10 ter2) -14.0)
		(= (flow r13 r4 ter2) -11.0)
		(= (flow r13 r12 ter2) -19.0)
		(availableflow r5 r10 ter2)
		(availableflow r5 r14 ter2)
		(availableflow r5 r12 ter2)
		(availableflow r9 r4 ter2)
		(availableflow r9 r14 ter2)
		(availableflow r9 r12 ter2)
		(availableflow r11 r10 ter2)
		(availableflow r11 r4 ter2)
		(availableflow r11 r14 ter2)
		(availableflow r13 r10 ter2)
		(availableflow r13 r4 ter2)
		(availableflow r13 r12 ter2)
		(active ter2 r5)
		(active ter2 r9)
		(active ter2 r11)
		(active ter2 r13)
		(= (maxgreentime ter3) 1.0)
		(= (mingreentime ter3) 16.0)
		(= (greentime ter3) 5.0)
		(= (token ter3) 5.0)
		(= (maxtoken ter3) 1.0)
		(= (tokenvalue r12 ter3) -1.0)
		(= (tokenvalue r17 ter3) 15.0)
		(= (tokenvalue r15 ter3) 18.0)
		(= (tokenvalue r19 ter3) 4.0)
		(= (flow r12 r16 ter3) -19.0)
		(= (flow r12 r18 ter3) 15.0)
		(= (flow r12 r20 ter3) 14.0)
		(= (flow r15 r11 ter3) 9.0)
		(= (flow r15 r20 ter3) 13.0)
		(= (flow r15 r18 ter3) -4.0)
		(= (flow r17 r11 ter3) 18.0)
		(= (flow r17 r16 ter3) -18.0)
		(= (flow r17 r20 ter3) -22.0)
		(= (flow r19 r16 ter3) 6.0)
		(= (flow r19 r11 ter3) -8.0)
		(= (flow r19 r18 ter3) -8.0)
		(availableflow r12 r16 ter3)
		(availableflow r12 r18 ter3)
		(availableflow r12 r20 ter3)
		(availableflow r15 r11 ter3)
		(availableflow r15 r20 ter3)
		(availableflow r15 r18 ter3)
		(availableflow r17 r11 ter3)
		(availableflow r17 r16 ter3)
		(availableflow r17 r20 ter3)
		(availableflow r19 r16 ter3)
		(availableflow r19 r11 ter3)
		(availableflow r19 r18 ter3)
		(active ter3 r12)
		(active ter3 r19)
		(active ter3 r17)
		(active ter3 r15)
	)
	(:goal
			(and
				(< (queue r4) 20.0)
			)
	)
)