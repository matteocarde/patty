
        (define (problem prob39)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 r11 r12 r13 r14 r15 r16 r17 r18 r20 r21 r22 r23 r24 r25 r26 r27 r28 r29 r30 r31 r32 r33 r34 r35 r36 r37 r38 - robot
              r19 - mailrobot
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4) (= (i r5) 5) (= (i r6) 6) (= (i r7) 7) (= (i r8) 8) (= (i r9) 9) (= (i r10) 10) (= (i r11) 11) (= (i r12) 12) (= (i r13) 13) (= (i r14) 14) (= (i r15) 15) (= (i r16) 16) (= (i r17) 17) (= (i r18) 18) (= (i r19) 19) (= (i r20) 20) (= (i r21) 21) (= (i r22) 22) (= (i r23) 23) (= (i r24) 24) (= (i r25) 25) (= (i r26) 26) (= (i r27) 27) (= (i r28) 28) (= (i r29) 29) (= (i r30) 30) (= (i r31) 31) (= (i r32) 32) (= (i r33) 33) (= (i r34) 34) (= (i r35) 35) (= (i r36) 36) (= (i r37) 37) (= (i r38) 38)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80) (= (x r5) 100) (= (x r6) 120) (= (x r7) 140) (= (x r8) 160) (= (x r9) 180) (= (x r10) 200) (= (x r11) 220) (= (x r12) 240) (= (x r13) 260) (= (x r14) 280) (= (x r15) 300) (= (x r16) 320) (= (x r17) 340) (= (x r18) 360) (= (x r19) 380) (= (x r20) 400) (= (x r21) 420) (= (x r22) 440) (= (x r23) 460) (= (x r24) 480) (= (x r25) 500) (= (x r26) 520) (= (x r27) 540) (= (x r28) 560) (= (x r29) 580) (= (x r30) 600) (= (x r31) 620) (= (x r32) 640) (= (x r33) 660) (= (x r34) 680) (= (x r35) 700) (= (x r36) 720) (= (x r37) 740) (= (x r38) 760)
                
                (= (p r0) 1) (= (p r1) 0) (= (p r2) 0) (= (p r3) 0) (= (p r4) 0) (= (p r5) 0) (= (p r6) 0) (= (p r7) 0) (= (p r8) 0) (= (p r9) 0) (= (p r10) 0) (= (p r11) 0) (= (p r12) 0) (= (p r13) 0) (= (p r14) 0) (= (p r15) 0) (= (p r16) 0) (= (p r17) 0) (= (p r18) 0) (= (p r19) 0) (= (p r20) 0) (= (p r21) 0) (= (p r22) 0) (= (p r23) 0) (= (p r24) 0) (= (p r25) 0) (= (p r26) 0) (= (p r27) 0) (= (p r28) 0) (= (p r29) 0) (= (p r30) 0) (= (p r31) 0) (= (p r32) 0) (= (p r33) 0) (= (p r34) 0) (= (p r35) 0) (= (p r36) 0) (= (p r37) 0) (= (p r38) 0)
                (= (q r0) 1) (= (q r1) 0) (= (q r2) 0) (= (q r3) 0) (= (q r4) 0) (= (q r5) 0) (= (q r6) 0) (= (q r7) 0) (= (q r8) 0) (= (q r9) 0) (= (q r10) 0) (= (q r11) 0) (= (q r12) 0) (= (q r13) 0) (= (q r14) 0) (= (q r15) 0) (= (q r16) 0) (= (q r17) 0) (= (q r18) 0) (= (q r19) 0) (= (q r20) 0) (= (q r21) 0) (= (q r22) 0) (= (q r23) 0) (= (q r24) 0) (= (q r25) 0) (= (q r26) 0) (= (q r27) 0) (= (q r28) 0) (= (q r29) 0) (= (q r30) 0) (= (q r31) 0) (= (q r32) 0) (= (q r33) 0) (= (q r34) 0) (= (q r35) 0) (= (q r36) 0) (= (q r37) 0) (= (q r38) 0)
            )

            (:goal
                (and
                    (psd)
                    (qsd)
                    (= (p r0) 1)
                    (= (q r38) 1)
                )
            )
        )