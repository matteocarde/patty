
        (define (problem prob10)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 r3 r4 r5 r6 r7 r8 r9 - robot
              l0 l1 l2 l3 l4 l5 l6 l7 l8 l9 - letter
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4) (= (i r5) 5) (= (i r6) 6) (= (i r7) 7) (= (i r8) 8) (= (i r9) 9)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80) (= (x r5) 100) (= (x r6) 120) (= (x r7) 140) (= (x r8) 160) (= (x r9) 180)
                
                (= (p r0 l0) 1) (= (p r0 l1) 1) (= (p r0 l2) 1) (= (p r0 l3) 1) (= (p r0 l4) 1) (= (p r0 l5) 1) (= (p r0 l6) 1) (= (p r0 l7) 1) (= (p r0 l8) 1) (= (p r0 l9) 1) (= (p r1 l0) 0) (= (p r1 l1) 0) (= (p r1 l2) 0) (= (p r1 l3) 0) (= (p r1 l4) 0) (= (p r1 l5) 0) (= (p r1 l6) 0) (= (p r1 l7) 0) (= (p r1 l8) 0) (= (p r1 l9) 0) (= (p r2 l0) 0) (= (p r2 l1) 0) (= (p r2 l2) 0) (= (p r2 l3) 0) (= (p r2 l4) 0) (= (p r2 l5) 0) (= (p r2 l6) 0) (= (p r2 l7) 0) (= (p r2 l8) 0) (= (p r2 l9) 0) (= (p r3 l0) 0) (= (p r3 l1) 0) (= (p r3 l2) 0) (= (p r3 l3) 0) (= (p r3 l4) 0) (= (p r3 l5) 0) (= (p r3 l6) 0) (= (p r3 l7) 0) (= (p r3 l8) 0) (= (p r3 l9) 0) (= (p r4 l0) 0) (= (p r4 l1) 0) (= (p r4 l2) 0) (= (p r4 l3) 0) (= (p r4 l4) 0) (= (p r4 l5) 0) (= (p r4 l6) 0) (= (p r4 l7) 0) (= (p r4 l8) 0) (= (p r4 l9) 0) (= (p r5 l0) 0) (= (p r5 l1) 0) (= (p r5 l2) 0) (= (p r5 l3) 0) (= (p r5 l4) 0) (= (p r5 l5) 0) (= (p r5 l6) 0) (= (p r5 l7) 0) (= (p r5 l8) 0) (= (p r5 l9) 0) (= (p r6 l0) 0) (= (p r6 l1) 0) (= (p r6 l2) 0) (= (p r6 l3) 0) (= (p r6 l4) 0) (= (p r6 l5) 0) (= (p r6 l6) 0) (= (p r6 l7) 0) (= (p r6 l8) 0) (= (p r6 l9) 0) (= (p r7 l0) 0) (= (p r7 l1) 0) (= (p r7 l2) 0) (= (p r7 l3) 0) (= (p r7 l4) 0) (= (p r7 l5) 0) (= (p r7 l6) 0) (= (p r7 l7) 0) (= (p r7 l8) 0) (= (p r7 l9) 0) (= (p r8 l0) 0) (= (p r8 l1) 0) (= (p r8 l2) 0) (= (p r8 l3) 0) (= (p r8 l4) 0) (= (p r8 l5) 0) (= (p r8 l6) 0) (= (p r8 l7) 0) (= (p r8 l8) 0) (= (p r8 l9) 0) (= (p r9 l0) 0) (= (p r9 l1) 0) (= (p r9 l2) 0) (= (p r9 l3) 0) (= (p r9 l4) 0) (= (p r9 l5) 0) (= (p r9 l6) 0) (= (p r9 l7) 0) (= (p r9 l8) 0) (= (p r9 l9) 0)
                (= (h r0) 5) (= (h r1) 0) (= (h r2) 0) (= (h r3) 0) (= (h r4) 0) (= (h r5) 0) (= (h r6) 0) (= (h r7) 0) (= (h r8) 0) (= (h r9) 0)
            )

            (:goal
                (and
                    (psd r0 l0) (psd r0 l1) (psd r0 l2) (psd r0 l3) (psd r0 l4) (psd r0 l5) (psd r0 l6) (psd r0 l7) (psd r0 l8) (psd r0 l9) (psd r1 l0) (psd r1 l1) (psd r1 l2) (psd r1 l3) (psd r1 l4) (psd r1 l5) (psd r1 l6) (psd r1 l7) (psd r1 l8) (psd r1 l9) (psd r2 l0) (psd r2 l1) (psd r2 l2) (psd r2 l3) (psd r2 l4) (psd r2 l5) (psd r2 l6) (psd r2 l7) (psd r2 l8) (psd r2 l9) (psd r3 l0) (psd r3 l1) (psd r3 l2) (psd r3 l3) (psd r3 l4) (psd r3 l5) (psd r3 l6) (psd r3 l7) (psd r3 l8) (psd r3 l9) (psd r4 l0) (psd r4 l1) (psd r4 l2) (psd r4 l3) (psd r4 l4) (psd r4 l5) (psd r4 l6) (psd r4 l7) (psd r4 l8) (psd r4 l9) (psd r5 l0) (psd r5 l1) (psd r5 l2) (psd r5 l3) (psd r5 l4) (psd r5 l5) (psd r5 l6) (psd r5 l7) (psd r5 l8) (psd r5 l9) (psd r6 l0) (psd r6 l1) (psd r6 l2) (psd r6 l3) (psd r6 l4) (psd r6 l5) (psd r6 l6) (psd r6 l7) (psd r6 l8) (psd r6 l9) (psd r7 l0) (psd r7 l1) (psd r7 l2) (psd r7 l3) (psd r7 l4) (psd r7 l5) (psd r7 l6) (psd r7 l7) (psd r7 l8) (psd r7 l9) (psd r8 l0) (psd r8 l1) (psd r8 l2) (psd r8 l3) (psd r8 l4) (psd r8 l5) (psd r8 l6) (psd r8 l7) (psd r8 l8) (psd r8 l9) (psd r9 l0) (psd r9 l1) (psd r9 l2) (psd r9 l3) (psd r9 l4) (psd r9 l5) (psd r9 l6) (psd r9 l7) (psd r9 l8) (psd r9 l9)
                    (= (h r0) 5)
                )
            )
        )