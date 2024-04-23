
        (define (problem prob18)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 r11 r12 r13 r14 r15 r16 r17 - robot
              l0 l1 l2 - letter
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4) (= (i r5) 5) (= (i r6) 6) (= (i r7) 7) (= (i r8) 8) (= (i r9) 9) (= (i r10) 10) (= (i r11) 11) (= (i r12) 12) (= (i r13) 13) (= (i r14) 14) (= (i r15) 15) (= (i r16) 16) (= (i r17) 17)
                (next r0 r1) (next r1 r2) (next r2 r3) (next r3 r4) (next r4 r5) (next r5 r6) (next r6 r7) (next r7 r8) (next r8 r9) (next r9 r10) (next r10 r11) (next r11 r12) (next r12 r13) (next r13 r14) (next r14 r15) (next r15 r16) (next r16 r17)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80) (= (x r5) 100) (= (x r6) 120) (= (x r7) 140) (= (x r8) 160) (= (x r9) 180) (= (x r10) 200) (= (x r11) 220) (= (x r12) 240) (= (x r13) 260) (= (x r14) 280) (= (x r15) 300) (= (x r16) 320) (= (x r17) 340)
                
                (= (p r0 l0) 1) (= (p r0 l1) 1) (= (p r0 l2) 1) (= (p r1 l0) 0) (= (p r1 l1) 0) (= (p r1 l2) 0) (= (p r2 l0) 0) (= (p r2 l1) 0) (= (p r2 l2) 0) (= (p r3 l0) 0) (= (p r3 l1) 0) (= (p r3 l2) 0) (= (p r4 l0) 0) (= (p r4 l1) 0) (= (p r4 l2) 0) (= (p r5 l0) 0) (= (p r5 l1) 0) (= (p r5 l2) 0) (= (p r6 l0) 0) (= (p r6 l1) 0) (= (p r6 l2) 0) (= (p r7 l0) 0) (= (p r7 l1) 0) (= (p r7 l2) 0) (= (p r8 l0) 0) (= (p r8 l1) 0) (= (p r8 l2) 0) (= (p r9 l0) 0) (= (p r9 l1) 0) (= (p r9 l2) 0) (= (p r10 l0) 0) (= (p r10 l1) 0) (= (p r10 l2) 0) (= (p r11 l0) 0) (= (p r11 l1) 0) (= (p r11 l2) 0) (= (p r12 l0) 0) (= (p r12 l1) 0) (= (p r12 l2) 0) (= (p r13 l0) 0) (= (p r13 l1) 0) (= (p r13 l2) 0) (= (p r14 l0) 0) (= (p r14 l1) 0) (= (p r14 l2) 0) (= (p r15 l0) 0) (= (p r15 l1) 0) (= (p r15 l2) 0) (= (p r16 l0) 0) (= (p r16 l1) 0) (= (p r16 l2) 0) (= (p r17 l0) 0) (= (p r17 l1) 0) (= (p r17 l2) 0)
                (= (h r0) 3) (= (h r1) 0) (= (h r2) 0) (= (h r3) 0) (= (h r4) 0) (= (h r5) 0) (= (h r6) 0) (= (h r7) 0) (= (h r8) 0) (= (h r9) 0) (= (h r10) 0) (= (h r11) 0) (= (h r12) 0) (= (h r13) 0) (= (h r14) 0) (= (h r15) 0) (= (h r16) 0) (= (h r17) 0)
            )

            (:goal
                (and
                    (psd r0 l0) (psd r0 l1) (psd r0 l2) (psd r1 l0) (psd r1 l1) (psd r1 l2) (psd r2 l0) (psd r2 l1) (psd r2 l2) (psd r3 l0) (psd r3 l1) (psd r3 l2) (psd r4 l0) (psd r4 l1) (psd r4 l2) (psd r5 l0) (psd r5 l1) (psd r5 l2) (psd r6 l0) (psd r6 l1) (psd r6 l2) (psd r7 l0) (psd r7 l1) (psd r7 l2) (psd r8 l0) (psd r8 l1) (psd r8 l2) (psd r9 l0) (psd r9 l1) (psd r9 l2) (psd r10 l0) (psd r10 l1) (psd r10 l2) (psd r11 l0) (psd r11 l1) (psd r11 l2) (psd r12 l0) (psd r12 l1) (psd r12 l2) (psd r13 l0) (psd r13 l1) (psd r13 l2) (psd r14 l0) (psd r14 l1) (psd r14 l2) (psd r15 l0) (psd r15 l1) (psd r15 l2) (psd r16 l0) (psd r16 l1) (psd r16 l2) (psd r17 l0) (psd r17 l1) (psd r17 l2)
                    (= (h r0) 3)
                )
            )
        )