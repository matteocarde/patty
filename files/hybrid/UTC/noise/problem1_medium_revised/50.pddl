(define (problem trafficlights)
	(:domain urbantraffic)
	(:objects
		ter1 ter2 ter3 - intersection
		r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 r11 r12 r13 r14 r15 r16 r17 r18 r19 r20 - road
		buf0 buf1 buf2 - buffer
	)
	(:init
		(= (queue r1) -13.0)
		(= (queue r2) 19.0)
		(= (queue r3) -21.0)
		(= (queue r4) 37.0)
		(= (queue r5) 6.0)
		(= (queue r6) 77.0)
		(= (queue r7) 21.0)
		(= (queue r8) -20.0)
		(= (queue r9) 6.0)
		(= (queue r10) 39.0)
		(= (queue r11) 83.0)
		(= (queue r12) -37.0)
		(= (queue r13) 48.0)
		(= (queue r14) 37.0)
		(= (queue r15) 95.0)
		(= (queue r16) -31.0)
		(= (queue r17) 18.0)
		(= (queue r18) -43.0)
		(= (queue r19) 85.0)
		(= (queue r20) 25.0)
		(= (carsinbuffer buf0) -4.0)
		(gotcars buf0)
		(bufferconnected buf0 r17)
		(= (carsinbuffer buf1) -31.0)
		(gotcars buf1)
		(bufferconnected buf1 r15)
		(= (carsinbuffer buf2) 15.0)
		(gotcars buf2)
		(bufferconnected buf2 r9)
		(= (max_queue r1) 81.0)
		(= (max_queue r2) 100.0)
		(= (max_queue r3) 54.0)
		(= (max_queue r4) 5.0)
		(= (max_queue r5) 57.0)
		(= (max_queue r6) 108.0)
		(= (max_queue r7) 52.0)
		(= (max_queue r8) 122.0)
		(= (max_queue r9) 80.0)
		(= (max_queue r10) 139.0)
		(= (max_queue r11) 61.0)
		(= (max_queue r12) 105.0)
		(= (max_queue r13) 90.0)
		(= (max_queue r14) 91.0)
		(= (max_queue r15) 79.0)
		(= (max_queue r16) 103.0)
		(= (max_queue r17) 66.0)
		(= (max_queue r18) 51.0)
		(= (max_queue r19) 114.0)
		(= (max_queue r20) 146.0)
		(= (saturated_queue r1) 87.0)
		(= (saturated_queue r2) 134.0)
		(= (saturated_queue r3) 120.0)
		(= (saturated_queue r4) 68.0)
		(= (saturated_queue r5) 146.0)
		(= (saturated_queue r6) 66.0)
		(= (saturated_queue r7) 130.0)
		(= (saturated_queue r8) 105.0)
		(= (saturated_queue r9) 57.0)
		(= (saturated_queue r10) 125.0)
		(= (saturated_queue r11) 144.0)
		(= (saturated_queue r12) 111.0)
		(= (saturated_queue r13) 146.0)
		(= (saturated_queue r14) 94.0)
		(= (saturated_queue r15) 66.0)
		(= (saturated_queue r16) 56.0)
		(= (saturated_queue r17) 140.0)
		(= (saturated_queue r18) 65.0)
		(= (saturated_queue r19) 94.0)
		(= (saturated_queue r20) 142.0)
		(= (greentime ter1) 16.0)
		(= (token ter1) 69.0)
		(= (maxtoken ter1) -24.0)
		(= (tokenvalue r8 ter1) 6.0)
		(= (tokenvalue r4 ter1) -20.0)
		(= (tokenvalue r2 ter1) -30.0)
		(= (tokenvalue r6 ter1) 17.0)
		(= (maxgreentime ter1) 28.0)
		(= (mingreentime ter1) -40.0)
		(= (flow r8 r3 ter1) 18.0)
		(= (flow r8 r5 ter1) 19.0)
		(= (flow r8 r7 ter1) 13.0)
		(= (flow r2 r1 ter1) 50.0)
		(= (flow r2 r5 ter1) -37.0)
		(= (flow r2 r7 ter1) 48.0)
		(= (flow r4 r1 ter1) -10.0)
		(= (flow r4 r3 ter1) -27.0)
		(= (flow r4 r7 ter1) 31.0)
		(= (flow r6 r1 ter1) -10.0)
		(= (flow r6 r3 ter1) 1.0)
		(= (flow r6 r5 ter1) -6.0)
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
		(= (greentime ter2) 23.0)
		(= (token ter2) -26.0)
		(= (maxtoken ter2) 13.0)
		(= (tokenvalue r5 ter2) 44.0)
		(= (tokenvalue r11 ter2) 13.0)
		(= (tokenvalue r9 ter2) 28.0)
		(= (tokenvalue r13 ter2) 12.0)
		(= (maxgreentime ter2) 36.0)
		(= (mingreentime ter2) 39.0)
		(= (flow r5 r10 ter2) 3.0)
		(= (flow r5 r14 ter2) 45.0)
		(= (flow r5 r12 ter2) 3.0)
		(= (flow r9 r4 ter2) 5.0)
		(= (flow r9 r14 ter2) -2.0)
		(= (flow r9 r12 ter2) -22.0)
		(= (flow r11 r10 ter2) 45.0)
		(= (flow r11 r4 ter2) -41.0)
		(= (flow r11 r14 ter2) -48.0)
		(= (flow r13 r10 ter2) -11.0)
		(= (flow r13 r4 ter2) 49.0)
		(= (flow r13 r12 ter2) 34.0)
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
		(= (maxgreentime ter3) 13.0)
		(= (mingreentime ter3) 42.0)
		(= (greentime ter3) -35.0)
		(= (token ter3) 34.0)
		(= (maxtoken ter3) 33.0)
		(= (tokenvalue r12 ter3) -4.0)
		(= (tokenvalue r17 ter3) 29.0)
		(= (tokenvalue r15 ter3) 60.0)
		(= (tokenvalue r19 ter3) 4.0)
		(= (flow r12 r16 ter3) 29.0)
		(= (flow r12 r18 ter3) 46.0)
		(= (flow r12 r20 ter3) 12.0)
		(= (flow r15 r11 ter3) 35.0)
		(= (flow r15 r20 ter3) 21.0)
		(= (flow r15 r18 ter3) 8.0)
		(= (flow r17 r11 ter3) 0.0)
		(= (flow r17 r16 ter3) 35.0)
		(= (flow r17 r20 ter3) 15.0)
		(= (flow r19 r16 ter3) 26.0)
		(= (flow r19 r11 ter3) 8.0)
		(= (flow r19 r18 ter3) -27.0)
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