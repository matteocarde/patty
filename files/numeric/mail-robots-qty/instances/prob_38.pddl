
        (define (problem prob38)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 r11 r12 r13 r14 r15 r16 r17 r18 r19 r20 r21 r22 r23 r24 r25 r26 r27 r28 r29 r30 r31 r32 r33 r34 r35 r36 r37 - robot
              l0 l1 l2 l3 - letter
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4) (= (i r5) 5) (= (i r6) 6) (= (i r7) 7) (= (i r8) 8) (= (i r9) 9) (= (i r10) 10) (= (i r11) 11) (= (i r12) 12) (= (i r13) 13) (= (i r14) 14) (= (i r15) 15) (= (i r16) 16) (= (i r17) 17) (= (i r18) 18) (= (i r19) 19) (= (i r20) 20) (= (i r21) 21) (= (i r22) 22) (= (i r23) 23) (= (i r24) 24) (= (i r25) 25) (= (i r26) 26) (= (i r27) 27) (= (i r28) 28) (= (i r29) 29) (= (i r30) 30) (= (i r31) 31) (= (i r32) 32) (= (i r33) 33) (= (i r34) 34) (= (i r35) 35) (= (i r36) 36) (= (i r37) 37)
                (next r0 r1) (next r1 r2) (next r2 r3) (next r3 r4) (next r4 r5) (next r5 r6) (next r6 r7) (next r7 r8) (next r8 r9) (next r9 r10) (next r10 r11) (next r11 r12) (next r12 r13) (next r13 r14) (next r14 r15) (next r15 r16) (next r16 r17) (next r17 r18) (next r18 r19) (next r19 r20) (next r20 r21) (next r21 r22) (next r22 r23) (next r23 r24) (next r24 r25) (next r25 r26) (next r26 r27) (next r27 r28) (next r28 r29) (next r29 r30) (next r30 r31) (next r31 r32) (next r32 r33) (next r33 r34) (next r34 r35) (next r35 r36) (next r36 r37)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80) (= (x r5) 100) (= (x r6) 120) (= (x r7) 140) (= (x r8) 160) (= (x r9) 180) (= (x r10) 200) (= (x r11) 220) (= (x r12) 240) (= (x r13) 260) (= (x r14) 280) (= (x r15) 300) (= (x r16) 320) (= (x r17) 340) (= (x r18) 360) (= (x r19) 380) (= (x r20) 400) (= (x r21) 420) (= (x r22) 440) (= (x r23) 460) (= (x r24) 480) (= (x r25) 500) (= (x r26) 520) (= (x r27) 540) (= (x r28) 560) (= (x r29) 580) (= (x r30) 600) (= (x r31) 620) (= (x r32) 640) (= (x r33) 660) (= (x r34) 680) (= (x r35) 700) (= (x r36) 720) (= (x r37) 740)
                
                (= (p r0 l0) 1) (= (p r0 l1) 1) (= (p r0 l2) 1) (= (p r0 l3) 1) (= (p r1 l0) 0) (= (p r1 l1) 0) (= (p r1 l2) 0) (= (p r1 l3) 0) (= (p r2 l0) 0) (= (p r2 l1) 0) (= (p r2 l2) 0) (= (p r2 l3) 0) (= (p r3 l0) 0) (= (p r3 l1) 0) (= (p r3 l2) 0) (= (p r3 l3) 0) (= (p r4 l0) 0) (= (p r4 l1) 0) (= (p r4 l2) 0) (= (p r4 l3) 0) (= (p r5 l0) 0) (= (p r5 l1) 0) (= (p r5 l2) 0) (= (p r5 l3) 0) (= (p r6 l0) 0) (= (p r6 l1) 0) (= (p r6 l2) 0) (= (p r6 l3) 0) (= (p r7 l0) 0) (= (p r7 l1) 0) (= (p r7 l2) 0) (= (p r7 l3) 0) (= (p r8 l0) 0) (= (p r8 l1) 0) (= (p r8 l2) 0) (= (p r8 l3) 0) (= (p r9 l0) 0) (= (p r9 l1) 0) (= (p r9 l2) 0) (= (p r9 l3) 0) (= (p r10 l0) 0) (= (p r10 l1) 0) (= (p r10 l2) 0) (= (p r10 l3) 0) (= (p r11 l0) 0) (= (p r11 l1) 0) (= (p r11 l2) 0) (= (p r11 l3) 0) (= (p r12 l0) 0) (= (p r12 l1) 0) (= (p r12 l2) 0) (= (p r12 l3) 0) (= (p r13 l0) 0) (= (p r13 l1) 0) (= (p r13 l2) 0) (= (p r13 l3) 0) (= (p r14 l0) 0) (= (p r14 l1) 0) (= (p r14 l2) 0) (= (p r14 l3) 0) (= (p r15 l0) 0) (= (p r15 l1) 0) (= (p r15 l2) 0) (= (p r15 l3) 0) (= (p r16 l0) 0) (= (p r16 l1) 0) (= (p r16 l2) 0) (= (p r16 l3) 0) (= (p r17 l0) 0) (= (p r17 l1) 0) (= (p r17 l2) 0) (= (p r17 l3) 0) (= (p r18 l0) 0) (= (p r18 l1) 0) (= (p r18 l2) 0) (= (p r18 l3) 0) (= (p r19 l0) 0) (= (p r19 l1) 0) (= (p r19 l2) 0) (= (p r19 l3) 0) (= (p r20 l0) 0) (= (p r20 l1) 0) (= (p r20 l2) 0) (= (p r20 l3) 0) (= (p r21 l0) 0) (= (p r21 l1) 0) (= (p r21 l2) 0) (= (p r21 l3) 0) (= (p r22 l0) 0) (= (p r22 l1) 0) (= (p r22 l2) 0) (= (p r22 l3) 0) (= (p r23 l0) 0) (= (p r23 l1) 0) (= (p r23 l2) 0) (= (p r23 l3) 0) (= (p r24 l0) 0) (= (p r24 l1) 0) (= (p r24 l2) 0) (= (p r24 l3) 0) (= (p r25 l0) 0) (= (p r25 l1) 0) (= (p r25 l2) 0) (= (p r25 l3) 0) (= (p r26 l0) 0) (= (p r26 l1) 0) (= (p r26 l2) 0) (= (p r26 l3) 0) (= (p r27 l0) 0) (= (p r27 l1) 0) (= (p r27 l2) 0) (= (p r27 l3) 0) (= (p r28 l0) 0) (= (p r28 l1) 0) (= (p r28 l2) 0) (= (p r28 l3) 0) (= (p r29 l0) 0) (= (p r29 l1) 0) (= (p r29 l2) 0) (= (p r29 l3) 0) (= (p r30 l0) 0) (= (p r30 l1) 0) (= (p r30 l2) 0) (= (p r30 l3) 0) (= (p r31 l0) 0) (= (p r31 l1) 0) (= (p r31 l2) 0) (= (p r31 l3) 0) (= (p r32 l0) 0) (= (p r32 l1) 0) (= (p r32 l2) 0) (= (p r32 l3) 0) (= (p r33 l0) 0) (= (p r33 l1) 0) (= (p r33 l2) 0) (= (p r33 l3) 0) (= (p r34 l0) 0) (= (p r34 l1) 0) (= (p r34 l2) 0) (= (p r34 l3) 0) (= (p r35 l0) 0) (= (p r35 l1) 0) (= (p r35 l2) 0) (= (p r35 l3) 0) (= (p r36 l0) 0) (= (p r36 l1) 0) (= (p r36 l2) 0) (= (p r36 l3) 0) (= (p r37 l0) 0) (= (p r37 l1) 0) (= (p r37 l2) 0) (= (p r37 l3) 0)
                (= (h r0) 4) (= (h r1) 0) (= (h r2) 0) (= (h r3) 0) (= (h r4) 0) (= (h r5) 0) (= (h r6) 0) (= (h r7) 0) (= (h r8) 0) (= (h r9) 0) (= (h r10) 0) (= (h r11) 0) (= (h r12) 0) (= (h r13) 0) (= (h r14) 0) (= (h r15) 0) (= (h r16) 0) (= (h r17) 0) (= (h r18) 0) (= (h r19) 0) (= (h r20) 0) (= (h r21) 0) (= (h r22) 0) (= (h r23) 0) (= (h r24) 0) (= (h r25) 0) (= (h r26) 0) (= (h r27) 0) (= (h r28) 0) (= (h r29) 0) (= (h r30) 0) (= (h r31) 0) (= (h r32) 0) (= (h r33) 0) (= (h r34) 0) (= (h r35) 0) (= (h r36) 0) (= (h r37) 0)
            )

            (:goal
                (and
                    (psd r0 l0) (psd r0 l1) (psd r0 l2) (psd r0 l3) (psd r1 l0) (psd r1 l1) (psd r1 l2) (psd r1 l3) (psd r2 l0) (psd r2 l1) (psd r2 l2) (psd r2 l3) (psd r3 l0) (psd r3 l1) (psd r3 l2) (psd r3 l3) (psd r4 l0) (psd r4 l1) (psd r4 l2) (psd r4 l3) (psd r5 l0) (psd r5 l1) (psd r5 l2) (psd r5 l3) (psd r6 l0) (psd r6 l1) (psd r6 l2) (psd r6 l3) (psd r7 l0) (psd r7 l1) (psd r7 l2) (psd r7 l3) (psd r8 l0) (psd r8 l1) (psd r8 l2) (psd r8 l3) (psd r9 l0) (psd r9 l1) (psd r9 l2) (psd r9 l3) (psd r10 l0) (psd r10 l1) (psd r10 l2) (psd r10 l3) (psd r11 l0) (psd r11 l1) (psd r11 l2) (psd r11 l3) (psd r12 l0) (psd r12 l1) (psd r12 l2) (psd r12 l3) (psd r13 l0) (psd r13 l1) (psd r13 l2) (psd r13 l3) (psd r14 l0) (psd r14 l1) (psd r14 l2) (psd r14 l3) (psd r15 l0) (psd r15 l1) (psd r15 l2) (psd r15 l3) (psd r16 l0) (psd r16 l1) (psd r16 l2) (psd r16 l3) (psd r17 l0) (psd r17 l1) (psd r17 l2) (psd r17 l3) (psd r18 l0) (psd r18 l1) (psd r18 l2) (psd r18 l3) (psd r19 l0) (psd r19 l1) (psd r19 l2) (psd r19 l3) (psd r20 l0) (psd r20 l1) (psd r20 l2) (psd r20 l3) (psd r21 l0) (psd r21 l1) (psd r21 l2) (psd r21 l3) (psd r22 l0) (psd r22 l1) (psd r22 l2) (psd r22 l3) (psd r23 l0) (psd r23 l1) (psd r23 l2) (psd r23 l3) (psd r24 l0) (psd r24 l1) (psd r24 l2) (psd r24 l3) (psd r25 l0) (psd r25 l1) (psd r25 l2) (psd r25 l3) (psd r26 l0) (psd r26 l1) (psd r26 l2) (psd r26 l3) (psd r27 l0) (psd r27 l1) (psd r27 l2) (psd r27 l3) (psd r28 l0) (psd r28 l1) (psd r28 l2) (psd r28 l3) (psd r29 l0) (psd r29 l1) (psd r29 l2) (psd r29 l3) (psd r30 l0) (psd r30 l1) (psd r30 l2) (psd r30 l3) (psd r31 l0) (psd r31 l1) (psd r31 l2) (psd r31 l3) (psd r32 l0) (psd r32 l1) (psd r32 l2) (psd r32 l3) (psd r33 l0) (psd r33 l1) (psd r33 l2) (psd r33 l3) (psd r34 l0) (psd r34 l1) (psd r34 l2) (psd r34 l3) (psd r35 l0) (psd r35 l1) (psd r35 l2) (psd r35 l3) (psd r36 l0) (psd r36 l1) (psd r36 l2) (psd r36 l3) (psd r37 l0) (psd r37 l1) (psd r37 l2) (psd r37 l3)
                    (= (h r0) 4)
                )
            )
        )