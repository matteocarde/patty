(define (problem trafficlights)
    (:domain urbantraffic)
    (:objects int1 int2 int3 int4 int5 int6 int7 int8 int9 - intersection r1 r2 r3 r4 r5 r6w r6e r7w r7e r8 r9 r10 r11w r11e r12 r13 r14 r15w r15e r16w r16e r17 - road buf0 - buffer)
(:init

(= (queue r1) 4000)
(= (queue r2) 4000)
(= (queue r3) 4000)
(= (queue r4) 4000)
(= (queue r5) 200)
(= (queue r6w) 200)
(= (queue r6e) 200)
(= (queue r7w) 200)
(= (queue r7e) 200)
(= (queue r8) 200)
(= (queue r9) 300)
(= (queue r10) 300)
(= (queue r11w) 50)
(= (queue r11e) 50)
(= (queue r12) 300)
(= (queue r13) 100)
(= (queue r14) 0)
(= (queue r15w) 50)
(= (queue r15e) 50)
(= (queue r16w) 50)
(= (queue r16e) 50)
(= (queue r17) 0)
	
(bufferconnected buf0 r1)

(= (max_queue r1) 5000)
(= (max_queue r2) 5000)
(= (max_queue r3) 5000)
(= (max_queue r4) 5000)
(= (max_queue r5) 500)
(= (max_queue r6w) 500)
(= (max_queue r7w) 500)
(= (max_queue r6e) 500)
(= (max_queue r7e) 500)
(= (max_queue r8) 300)
(= (max_queue r9) 500)
(= (max_queue r10) 500)
(= (max_queue r11w) 150)
(= (max_queue r11e) 150)
(= (max_queue r12) 700)
(= (max_queue r13) 500)
(= (max_queue r14) 10000)
(= (max_queue r15w) 200)
(= (max_queue r15e) 200)
(= (max_queue r16w) 200)
(= (max_queue r16e) 200)
(= (max_queue r17) 10000)

(= (saturated_queue r1) 500)
(= (saturated_queue r2) 500)
(= (saturated_queue r3) 500)
(= (saturated_queue r4) 500)
(= (saturated_queue r5) 300)
(= (saturated_queue r6w) 300)
(= (saturated_queue r7w) 300)
(= (saturated_queue r6e) 300)
(= (saturated_queue r7e) 300)
(= (saturated_queue r8) 200)
(= (saturated_queue r9) 300)
(= (saturated_queue r10) 400)
(= (saturated_queue r11w) 100)
(= (saturated_queue r11e) 100)
(= (saturated_queue r12) 500)
(= (saturated_queue r13) 300)
(= (saturated_queue r14) 10000)
(= (saturated_queue r15w) 100)
(= (saturated_queue r15e) 100)
(= (saturated_queue r16w) 100)
(= (saturated_queue r16e) 100)
(= (saturated_queue r17) 10000)

;; intersection 1
	(= (greentime int1) 0)
 	(= (token int1)  10)
 	(= (maxtoken int1)  20)
 	(= (tokenvalue r4 int1)  10)
 	(= (tokenvalue r6w int1)  20) 
	(= (maxgreentime int1) 40)
	(= (mingreentime int1) 5)
	(= (flow r4 r6e int1) 3)
	(= (flow r4 r5 int1) 5)
	(= (flow r6w r5 int1) 2)
	(availableflow r4 r6e int1)
	(availableflow r4 r5 int1)
	(availableflow r6w r5 int1)
	(active int1 r4)
	(active int1 r6w)

;; intersection 2
	(= (greentime int2) 0)
 	(= (token int2)  10)
 	(= (maxtoken int2)  20)
 	(= (tokenvalue r7w int2)  10)
 	(= (tokenvalue r6e int2)  20) 
	(= (maxgreentime int2) 40)
	(= (mingreentime int2) 5)
	(= (flow r7w r6w int2) 2)
	(= (flow r6e r7e int2) 2)
	(= (flow r6e r8 int2) 1)
	(= (flow r7w r8 int2) 1)
	(availableflow r7w r6w int2)
	(availableflow r6e r7e int2)
	(availableflow r6e r8 int2)
	(availableflow r7w r8 int2)
	(active int2 r6e)
	(active int2 r7w)

;; intersection 3
	(= (greentime int3) 0)
 	(= (token int3)  10)
 	(= (maxtoken int3)  20)
 	(= (tokenvalue r10 int3)  10)
 	(= (tokenvalue r7e int3)  20) 
	(= (maxgreentime int3) 40)
	(= (mingreentime int3) 5)
	(= (flow r10 r7w int3) 1)
	(= (flow r10 r9 int3) 2)
	(= (flow r7e r9 int3) 1)
	(availableflow r10 r7w int3)
	(availableflow r10 r9 int3)
	(availableflow r7e r9 int3)
	(active int3 r10)
	(active int3 r7e)


;; intersection 4
	(= (greentime int4) 0)
 	(= (token int4)  10)
 	(= (maxtoken int4)  20)
 	(= (tokenvalue r3 int4)  10)
 	(= (tokenvalue r11w int4)  20) 
	(= (maxgreentime int4) 40)
	(= (mingreentime int4) 5)
	(= (flow r3 r11e int4) 3)
	(= (flow r3 r10 int4) 5)
	(= (flow r11w r10 int4) 1)
	(availableflow r3 r11e int4)
	(availableflow r3 r10 int4)
	(availableflow r11w r10 int4)
	(active int4 r3)
	(active int4 r11w)

;; intersection 5
	(= (greentime int5) 0)
 	(= (token int5)  10)
 	(= (maxtoken int5)  20)
 	(= (tokenvalue r2 int5)  10)
 	(= (tokenvalue r11e int5)  20) 
	(= (maxgreentime int5) 40)
	(= (mingreentime int5) 5)
	(= (flow r2 r11w int5) 3)
	(= (flow r2 r12 int5) 5)
	(= (flow r11e r12 int5) 1)
	(availableflow r2 r11w int5)
	(availableflow r2 r12 int5)
	(availableflow r11e r12 int5)
	(active int5 r2)
	(active int5 r11e)

;; intersection 6
	(= (greentime int6) 0)
 	(= (token int6)  10)
 	(= (maxtoken int6)  20)
 	(= (tokenvalue r1 int6)  10)
 	(= (tokenvalue r12 int6)  20) 
	(= (maxgreentime int6) 40)
	(= (mingreentime int6) 5)
	(= (flow r12 r13 int6) 2)
	(= (flow r1 r13 int6) 5)
	(availableflow r12 r13 int6)
	(availableflow r1 r13 int6)
	(active int6 r1)
	(active int6 r12)

;; intersection 7
	(= (greentime int7) 0)
 	(= (token int7)  10)
 	(= (maxtoken int7)  20)
 	(= (tokenvalue r15e int7)  10)
 	(= (tokenvalue r13 int7)  10)
 	(= (tokenvalue r9 int7)  20)
	(= (maxgreentime int7) 40)
	(= (mingreentime int7) 5)
	(= (flow r15e r14 int7) 1)
	(= (flow r13 r14 int7) 1)
	(= (flow r9 r14 int7) 2)
	(availableflow r15e r14  int7)
	(availableflow r13 r14 int7)
	(availableflow r9 r14 int7)
	(active int7 r15e)
	(active int7 r13)	
	(active int7 r9)


;; intersection 8
	(= (greentime int8) 0)
 	(= (token int8)  10)
 	(= (maxtoken int8)  20)
 	(= (tokenvalue r15w int8)  10)
 	(= (tokenvalue r16e int8)  10)
 	(= (tokenvalue r8 int8)  20)
	(= (maxgreentime int8) 20)
	(= (mingreentime int8) 4)
	(= (flow r15w r16w int8) 2)
	(= (flow r16e r15e int8) 2)
	(= (flow r8 r16e int8) 1)
	(= (flow r8 r15e int8) 1)
	(availableflow r15w r16w  int8)
	(availableflow r16e r15e int8)
	(availableflow r8 r16w int8)
	(availableflow r8 r15e int8)
	(active int8 r16e)
	(active int8 r15w)	
	(active int8 r8)

;; intersection 9
	(= (greentime int9) 0)
 	(= (token int9)  10)
 	(= (maxtoken int9)  20)
 	(= (tokenvalue r5 int9)  10)
 	(= (tokenvalue r16w int9)  20) 
	(= (maxgreentime int9) 20)
	(= (mingreentime int9) 4)
	(= (flow r5 r16e int9) 3)
	(= (flow r5 r17 int9) 2)
	(= (flow r16w r17 int9) 2)
	(availableflow r5 r16e int9)
	(availableflow r5 r17 int9)
	(availableflow r16w r17 int9)
	(active int9 r5)
	(active int9 r16w)


)  
(:goal
(and
 (< (queue r4) (saturated_queue r4))
 (< (queue r3) (saturated_queue r3))
 (< (queue r2) (saturated_queue r2))
 (< (queue r1) (saturated_queue r1))
)
)
)

