
        (define (problem prob18)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 r11 r12 r13 r14 r15 r16 r17 - robot
              l0 l1 l2 l3 l4 l5 l6 l7 l8 l9 l10 l11 l12 l13 l14 l15 l16 l17 - letter
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4) (= (i r5) 5) (= (i r6) 6) (= (i r7) 7) (= (i r8) 8) (= (i r9) 9) (= (i r10) 10) (= (i r11) 11) (= (i r12) 12) (= (i r13) 13) (= (i r14) 14) (= (i r15) 15) (= (i r16) 16) (= (i r17) 17)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80) (= (x r5) 100) (= (x r6) 120) (= (x r7) 140) (= (x r8) 160) (= (x r9) 180) (= (x r10) 200) (= (x r11) 220) (= (x r12) 240) (= (x r13) 260) (= (x r14) 280) (= (x r15) 300) (= (x r16) 320) (= (x r17) 340)
                
                (= (p r0 l0) 1) (= (p r0 l1) 1) (= (p r0 l2) 1) (= (p r0 l3) 1) (= (p r0 l4) 1) (= (p r0 l5) 1) (= (p r0 l6) 1) (= (p r0 l7) 1) (= (p r0 l8) 1) (= (p r0 l9) 1) (= (p r0 l10) 1) (= (p r0 l11) 1) (= (p r0 l12) 1) (= (p r0 l13) 1) (= (p r0 l14) 1) (= (p r0 l15) 1) (= (p r0 l16) 1) (= (p r0 l17) 1) (= (p r1 l0) 0) (= (p r1 l1) 0) (= (p r1 l2) 0) (= (p r1 l3) 0) (= (p r1 l4) 0) (= (p r1 l5) 0) (= (p r1 l6) 0) (= (p r1 l7) 0) (= (p r1 l8) 0) (= (p r1 l9) 0) (= (p r1 l10) 0) (= (p r1 l11) 0) (= (p r1 l12) 0) (= (p r1 l13) 0) (= (p r1 l14) 0) (= (p r1 l15) 0) (= (p r1 l16) 0) (= (p r1 l17) 0) (= (p r2 l0) 0) (= (p r2 l1) 0) (= (p r2 l2) 0) (= (p r2 l3) 0) (= (p r2 l4) 0) (= (p r2 l5) 0) (= (p r2 l6) 0) (= (p r2 l7) 0) (= (p r2 l8) 0) (= (p r2 l9) 0) (= (p r2 l10) 0) (= (p r2 l11) 0) (= (p r2 l12) 0) (= (p r2 l13) 0) (= (p r2 l14) 0) (= (p r2 l15) 0) (= (p r2 l16) 0) (= (p r2 l17) 0) (= (p r3 l0) 0) (= (p r3 l1) 0) (= (p r3 l2) 0) (= (p r3 l3) 0) (= (p r3 l4) 0) (= (p r3 l5) 0) (= (p r3 l6) 0) (= (p r3 l7) 0) (= (p r3 l8) 0) (= (p r3 l9) 0) (= (p r3 l10) 0) (= (p r3 l11) 0) (= (p r3 l12) 0) (= (p r3 l13) 0) (= (p r3 l14) 0) (= (p r3 l15) 0) (= (p r3 l16) 0) (= (p r3 l17) 0) (= (p r4 l0) 0) (= (p r4 l1) 0) (= (p r4 l2) 0) (= (p r4 l3) 0) (= (p r4 l4) 0) (= (p r4 l5) 0) (= (p r4 l6) 0) (= (p r4 l7) 0) (= (p r4 l8) 0) (= (p r4 l9) 0) (= (p r4 l10) 0) (= (p r4 l11) 0) (= (p r4 l12) 0) (= (p r4 l13) 0) (= (p r4 l14) 0) (= (p r4 l15) 0) (= (p r4 l16) 0) (= (p r4 l17) 0) (= (p r5 l0) 0) (= (p r5 l1) 0) (= (p r5 l2) 0) (= (p r5 l3) 0) (= (p r5 l4) 0) (= (p r5 l5) 0) (= (p r5 l6) 0) (= (p r5 l7) 0) (= (p r5 l8) 0) (= (p r5 l9) 0) (= (p r5 l10) 0) (= (p r5 l11) 0) (= (p r5 l12) 0) (= (p r5 l13) 0) (= (p r5 l14) 0) (= (p r5 l15) 0) (= (p r5 l16) 0) (= (p r5 l17) 0) (= (p r6 l0) 0) (= (p r6 l1) 0) (= (p r6 l2) 0) (= (p r6 l3) 0) (= (p r6 l4) 0) (= (p r6 l5) 0) (= (p r6 l6) 0) (= (p r6 l7) 0) (= (p r6 l8) 0) (= (p r6 l9) 0) (= (p r6 l10) 0) (= (p r6 l11) 0) (= (p r6 l12) 0) (= (p r6 l13) 0) (= (p r6 l14) 0) (= (p r6 l15) 0) (= (p r6 l16) 0) (= (p r6 l17) 0) (= (p r7 l0) 0) (= (p r7 l1) 0) (= (p r7 l2) 0) (= (p r7 l3) 0) (= (p r7 l4) 0) (= (p r7 l5) 0) (= (p r7 l6) 0) (= (p r7 l7) 0) (= (p r7 l8) 0) (= (p r7 l9) 0) (= (p r7 l10) 0) (= (p r7 l11) 0) (= (p r7 l12) 0) (= (p r7 l13) 0) (= (p r7 l14) 0) (= (p r7 l15) 0) (= (p r7 l16) 0) (= (p r7 l17) 0) (= (p r8 l0) 0) (= (p r8 l1) 0) (= (p r8 l2) 0) (= (p r8 l3) 0) (= (p r8 l4) 0) (= (p r8 l5) 0) (= (p r8 l6) 0) (= (p r8 l7) 0) (= (p r8 l8) 0) (= (p r8 l9) 0) (= (p r8 l10) 0) (= (p r8 l11) 0) (= (p r8 l12) 0) (= (p r8 l13) 0) (= (p r8 l14) 0) (= (p r8 l15) 0) (= (p r8 l16) 0) (= (p r8 l17) 0) (= (p r9 l0) 0) (= (p r9 l1) 0) (= (p r9 l2) 0) (= (p r9 l3) 0) (= (p r9 l4) 0) (= (p r9 l5) 0) (= (p r9 l6) 0) (= (p r9 l7) 0) (= (p r9 l8) 0) (= (p r9 l9) 0) (= (p r9 l10) 0) (= (p r9 l11) 0) (= (p r9 l12) 0) (= (p r9 l13) 0) (= (p r9 l14) 0) (= (p r9 l15) 0) (= (p r9 l16) 0) (= (p r9 l17) 0) (= (p r10 l0) 0) (= (p r10 l1) 0) (= (p r10 l2) 0) (= (p r10 l3) 0) (= (p r10 l4) 0) (= (p r10 l5) 0) (= (p r10 l6) 0) (= (p r10 l7) 0) (= (p r10 l8) 0) (= (p r10 l9) 0) (= (p r10 l10) 0) (= (p r10 l11) 0) (= (p r10 l12) 0) (= (p r10 l13) 0) (= (p r10 l14) 0) (= (p r10 l15) 0) (= (p r10 l16) 0) (= (p r10 l17) 0) (= (p r11 l0) 0) (= (p r11 l1) 0) (= (p r11 l2) 0) (= (p r11 l3) 0) (= (p r11 l4) 0) (= (p r11 l5) 0) (= (p r11 l6) 0) (= (p r11 l7) 0) (= (p r11 l8) 0) (= (p r11 l9) 0) (= (p r11 l10) 0) (= (p r11 l11) 0) (= (p r11 l12) 0) (= (p r11 l13) 0) (= (p r11 l14) 0) (= (p r11 l15) 0) (= (p r11 l16) 0) (= (p r11 l17) 0) (= (p r12 l0) 0) (= (p r12 l1) 0) (= (p r12 l2) 0) (= (p r12 l3) 0) (= (p r12 l4) 0) (= (p r12 l5) 0) (= (p r12 l6) 0) (= (p r12 l7) 0) (= (p r12 l8) 0) (= (p r12 l9) 0) (= (p r12 l10) 0) (= (p r12 l11) 0) (= (p r12 l12) 0) (= (p r12 l13) 0) (= (p r12 l14) 0) (= (p r12 l15) 0) (= (p r12 l16) 0) (= (p r12 l17) 0) (= (p r13 l0) 0) (= (p r13 l1) 0) (= (p r13 l2) 0) (= (p r13 l3) 0) (= (p r13 l4) 0) (= (p r13 l5) 0) (= (p r13 l6) 0) (= (p r13 l7) 0) (= (p r13 l8) 0) (= (p r13 l9) 0) (= (p r13 l10) 0) (= (p r13 l11) 0) (= (p r13 l12) 0) (= (p r13 l13) 0) (= (p r13 l14) 0) (= (p r13 l15) 0) (= (p r13 l16) 0) (= (p r13 l17) 0) (= (p r14 l0) 0) (= (p r14 l1) 0) (= (p r14 l2) 0) (= (p r14 l3) 0) (= (p r14 l4) 0) (= (p r14 l5) 0) (= (p r14 l6) 0) (= (p r14 l7) 0) (= (p r14 l8) 0) (= (p r14 l9) 0) (= (p r14 l10) 0) (= (p r14 l11) 0) (= (p r14 l12) 0) (= (p r14 l13) 0) (= (p r14 l14) 0) (= (p r14 l15) 0) (= (p r14 l16) 0) (= (p r14 l17) 0) (= (p r15 l0) 0) (= (p r15 l1) 0) (= (p r15 l2) 0) (= (p r15 l3) 0) (= (p r15 l4) 0) (= (p r15 l5) 0) (= (p r15 l6) 0) (= (p r15 l7) 0) (= (p r15 l8) 0) (= (p r15 l9) 0) (= (p r15 l10) 0) (= (p r15 l11) 0) (= (p r15 l12) 0) (= (p r15 l13) 0) (= (p r15 l14) 0) (= (p r15 l15) 0) (= (p r15 l16) 0) (= (p r15 l17) 0) (= (p r16 l0) 0) (= (p r16 l1) 0) (= (p r16 l2) 0) (= (p r16 l3) 0) (= (p r16 l4) 0) (= (p r16 l5) 0) (= (p r16 l6) 0) (= (p r16 l7) 0) (= (p r16 l8) 0) (= (p r16 l9) 0) (= (p r16 l10) 0) (= (p r16 l11) 0) (= (p r16 l12) 0) (= (p r16 l13) 0) (= (p r16 l14) 0) (= (p r16 l15) 0) (= (p r16 l16) 0) (= (p r16 l17) 0) (= (p r17 l0) 0) (= (p r17 l1) 0) (= (p r17 l2) 0) (= (p r17 l3) 0) (= (p r17 l4) 0) (= (p r17 l5) 0) (= (p r17 l6) 0) (= (p r17 l7) 0) (= (p r17 l8) 0) (= (p r17 l9) 0) (= (p r17 l10) 0) (= (p r17 l11) 0) (= (p r17 l12) 0) (= (p r17 l13) 0) (= (p r17 l14) 0) (= (p r17 l15) 0) (= (p r17 l16) 0) (= (p r17 l17) 0)
                (= (h r0) 5) (= (h r1) 0) (= (h r2) 0) (= (h r3) 0) (= (h r4) 0) (= (h r5) 0) (= (h r6) 0) (= (h r7) 0) (= (h r8) 0) (= (h r9) 0) (= (h r10) 0) (= (h r11) 0) (= (h r12) 0) (= (h r13) 0) (= (h r14) 0) (= (h r15) 0) (= (h r16) 0) (= (h r17) 0)
            )

            (:goal
                (and
                    (psd r0 l0) (psd r0 l1) (psd r0 l2) (psd r0 l3) (psd r0 l4) (psd r0 l5) (psd r0 l6) (psd r0 l7) (psd r0 l8) (psd r0 l9) (psd r0 l10) (psd r0 l11) (psd r0 l12) (psd r0 l13) (psd r0 l14) (psd r0 l15) (psd r0 l16) (psd r0 l17) (psd r1 l0) (psd r1 l1) (psd r1 l2) (psd r1 l3) (psd r1 l4) (psd r1 l5) (psd r1 l6) (psd r1 l7) (psd r1 l8) (psd r1 l9) (psd r1 l10) (psd r1 l11) (psd r1 l12) (psd r1 l13) (psd r1 l14) (psd r1 l15) (psd r1 l16) (psd r1 l17) (psd r2 l0) (psd r2 l1) (psd r2 l2) (psd r2 l3) (psd r2 l4) (psd r2 l5) (psd r2 l6) (psd r2 l7) (psd r2 l8) (psd r2 l9) (psd r2 l10) (psd r2 l11) (psd r2 l12) (psd r2 l13) (psd r2 l14) (psd r2 l15) (psd r2 l16) (psd r2 l17) (psd r3 l0) (psd r3 l1) (psd r3 l2) (psd r3 l3) (psd r3 l4) (psd r3 l5) (psd r3 l6) (psd r3 l7) (psd r3 l8) (psd r3 l9) (psd r3 l10) (psd r3 l11) (psd r3 l12) (psd r3 l13) (psd r3 l14) (psd r3 l15) (psd r3 l16) (psd r3 l17) (psd r4 l0) (psd r4 l1) (psd r4 l2) (psd r4 l3) (psd r4 l4) (psd r4 l5) (psd r4 l6) (psd r4 l7) (psd r4 l8) (psd r4 l9) (psd r4 l10) (psd r4 l11) (psd r4 l12) (psd r4 l13) (psd r4 l14) (psd r4 l15) (psd r4 l16) (psd r4 l17) (psd r5 l0) (psd r5 l1) (psd r5 l2) (psd r5 l3) (psd r5 l4) (psd r5 l5) (psd r5 l6) (psd r5 l7) (psd r5 l8) (psd r5 l9) (psd r5 l10) (psd r5 l11) (psd r5 l12) (psd r5 l13) (psd r5 l14) (psd r5 l15) (psd r5 l16) (psd r5 l17) (psd r6 l0) (psd r6 l1) (psd r6 l2) (psd r6 l3) (psd r6 l4) (psd r6 l5) (psd r6 l6) (psd r6 l7) (psd r6 l8) (psd r6 l9) (psd r6 l10) (psd r6 l11) (psd r6 l12) (psd r6 l13) (psd r6 l14) (psd r6 l15) (psd r6 l16) (psd r6 l17) (psd r7 l0) (psd r7 l1) (psd r7 l2) (psd r7 l3) (psd r7 l4) (psd r7 l5) (psd r7 l6) (psd r7 l7) (psd r7 l8) (psd r7 l9) (psd r7 l10) (psd r7 l11) (psd r7 l12) (psd r7 l13) (psd r7 l14) (psd r7 l15) (psd r7 l16) (psd r7 l17) (psd r8 l0) (psd r8 l1) (psd r8 l2) (psd r8 l3) (psd r8 l4) (psd r8 l5) (psd r8 l6) (psd r8 l7) (psd r8 l8) (psd r8 l9) (psd r8 l10) (psd r8 l11) (psd r8 l12) (psd r8 l13) (psd r8 l14) (psd r8 l15) (psd r8 l16) (psd r8 l17) (psd r9 l0) (psd r9 l1) (psd r9 l2) (psd r9 l3) (psd r9 l4) (psd r9 l5) (psd r9 l6) (psd r9 l7) (psd r9 l8) (psd r9 l9) (psd r9 l10) (psd r9 l11) (psd r9 l12) (psd r9 l13) (psd r9 l14) (psd r9 l15) (psd r9 l16) (psd r9 l17) (psd r10 l0) (psd r10 l1) (psd r10 l2) (psd r10 l3) (psd r10 l4) (psd r10 l5) (psd r10 l6) (psd r10 l7) (psd r10 l8) (psd r10 l9) (psd r10 l10) (psd r10 l11) (psd r10 l12) (psd r10 l13) (psd r10 l14) (psd r10 l15) (psd r10 l16) (psd r10 l17) (psd r11 l0) (psd r11 l1) (psd r11 l2) (psd r11 l3) (psd r11 l4) (psd r11 l5) (psd r11 l6) (psd r11 l7) (psd r11 l8) (psd r11 l9) (psd r11 l10) (psd r11 l11) (psd r11 l12) (psd r11 l13) (psd r11 l14) (psd r11 l15) (psd r11 l16) (psd r11 l17) (psd r12 l0) (psd r12 l1) (psd r12 l2) (psd r12 l3) (psd r12 l4) (psd r12 l5) (psd r12 l6) (psd r12 l7) (psd r12 l8) (psd r12 l9) (psd r12 l10) (psd r12 l11) (psd r12 l12) (psd r12 l13) (psd r12 l14) (psd r12 l15) (psd r12 l16) (psd r12 l17) (psd r13 l0) (psd r13 l1) (psd r13 l2) (psd r13 l3) (psd r13 l4) (psd r13 l5) (psd r13 l6) (psd r13 l7) (psd r13 l8) (psd r13 l9) (psd r13 l10) (psd r13 l11) (psd r13 l12) (psd r13 l13) (psd r13 l14) (psd r13 l15) (psd r13 l16) (psd r13 l17) (psd r14 l0) (psd r14 l1) (psd r14 l2) (psd r14 l3) (psd r14 l4) (psd r14 l5) (psd r14 l6) (psd r14 l7) (psd r14 l8) (psd r14 l9) (psd r14 l10) (psd r14 l11) (psd r14 l12) (psd r14 l13) (psd r14 l14) (psd r14 l15) (psd r14 l16) (psd r14 l17) (psd r15 l0) (psd r15 l1) (psd r15 l2) (psd r15 l3) (psd r15 l4) (psd r15 l5) (psd r15 l6) (psd r15 l7) (psd r15 l8) (psd r15 l9) (psd r15 l10) (psd r15 l11) (psd r15 l12) (psd r15 l13) (psd r15 l14) (psd r15 l15) (psd r15 l16) (psd r15 l17) (psd r16 l0) (psd r16 l1) (psd r16 l2) (psd r16 l3) (psd r16 l4) (psd r16 l5) (psd r16 l6) (psd r16 l7) (psd r16 l8) (psd r16 l9) (psd r16 l10) (psd r16 l11) (psd r16 l12) (psd r16 l13) (psd r16 l14) (psd r16 l15) (psd r16 l16) (psd r16 l17) (psd r17 l0) (psd r17 l1) (psd r17 l2) (psd r17 l3) (psd r17 l4) (psd r17 l5) (psd r17 l6) (psd r17 l7) (psd r17 l8) (psd r17 l9) (psd r17 l10) (psd r17 l11) (psd r17 l12) (psd r17 l13) (psd r17 l14) (psd r17 l15) (psd r17 l16) (psd r17 l17)
                    (= (h r0) 5)
                )
            )
        )