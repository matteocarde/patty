
        (define (problem prob45)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 r11 r12 r13 r14 r15 r16 r17 r18 r19 r20 r21 r22 r23 r24 r25 r26 r27 r28 r29 r30 r31 r32 r33 r34 r35 r36 r37 r38 r39 r40 r41 r42 r43 r44 - robot
              g0 g1 - green
              y0 y1 - yellow
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4) (= (i r5) 5) (= (i r6) 6) (= (i r7) 7) (= (i r8) 8) (= (i r9) 9) (= (i r10) 10) (= (i r11) 11) (= (i r12) 12) (= (i r13) 13) (= (i r14) 14) (= (i r15) 15) (= (i r16) 16) (= (i r17) 17) (= (i r18) 18) (= (i r19) 19) (= (i r20) 20) (= (i r21) 21) (= (i r22) 22) (= (i r23) 23) (= (i r24) 24) (= (i r25) 25) (= (i r26) 26) (= (i r27) 27) (= (i r28) 28) (= (i r29) 29) (= (i r30) 30) (= (i r31) 31) (= (i r32) 32) (= (i r33) 33) (= (i r34) 34) (= (i r35) 35) (= (i r36) 36) (= (i r37) 37) (= (i r38) 38) (= (i r39) 39) (= (i r40) 40) (= (i r41) 41) (= (i r42) 42) (= (i r43) 43) (= (i r44) 44)
                (next r0 r1) (next r1 r2) (next r2 r3) (next r3 r4) (next r4 r5) (next r5 r6) (next r6 r7) (next r7 r8) (next r8 r9) (next r9 r10) (next r10 r11) (next r11 r12) (next r12 r13) (next r13 r14) (next r14 r15) (next r15 r16) (next r16 r17) (next r17 r18) (next r18 r19) (next r19 r20) (next r20 r21) (next r21 r22) (next r22 r23) (next r23 r24) (next r24 r25) (next r25 r26) (next r26 r27) (next r27 r28) (next r28 r29) (next r29 r30) (next r30 r31) (next r31 r32) (next r32 r33) (next r33 r34) (next r34 r35) (next r35 r36) (next r36 r37) (next r37 r38) (next r38 r39) (next r39 r40) (next r40 r41) (next r41 r42) (next r42 r43) (next r43 r44)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80) (= (x r5) 100) (= (x r6) 120) (= (x r7) 140) (= (x r8) 160) (= (x r9) 180) (= (x r10) 200) (= (x r11) 220) (= (x r12) 240) (= (x r13) 260) (= (x r14) 280) (= (x r15) 300) (= (x r16) 320) (= (x r17) 340) (= (x r18) 360) (= (x r19) 380) (= (x r20) 400) (= (x r21) 420) (= (x r22) 440) (= (x r23) 460) (= (x r24) 480) (= (x r25) 500) (= (x r26) 520) (= (x r27) 540) (= (x r28) 560) (= (x r29) 580) (= (x r30) 600) (= (x r31) 620) (= (x r32) 640) (= (x r33) 660) (= (x r34) 680) (= (x r35) 700) (= (x r36) 720) (= (x r37) 740) (= (x r38) 760) (= (x r39) 780) (= (x r40) 800) (= (x r41) 820) (= (x r42) 840) (= (x r43) 860) (= (x r44) 880)
                
                (= (g r0 g0) 1) (= (g r0 g1) 1) (= (g r1 g0) 0) (= (g r1 g1) 0) (= (g r2 g0) 0) (= (g r2 g1) 0) (= (g r3 g0) 0) (= (g r3 g1) 0) (= (g r4 g0) 0) (= (g r4 g1) 0) (= (g r5 g0) 0) (= (g r5 g1) 0) (= (g r6 g0) 0) (= (g r6 g1) 0) (= (g r7 g0) 0) (= (g r7 g1) 0) (= (g r8 g0) 0) (= (g r8 g1) 0) (= (g r9 g0) 0) (= (g r9 g1) 0) (= (g r10 g0) 0) (= (g r10 g1) 0) (= (g r11 g0) 0) (= (g r11 g1) 0) (= (g r12 g0) 0) (= (g r12 g1) 0) (= (g r13 g0) 0) (= (g r13 g1) 0) (= (g r14 g0) 0) (= (g r14 g1) 0) (= (g r15 g0) 0) (= (g r15 g1) 0) (= (g r16 g0) 0) (= (g r16 g1) 0) (= (g r17 g0) 0) (= (g r17 g1) 0) (= (g r18 g0) 0) (= (g r18 g1) 0) (= (g r19 g0) 0) (= (g r19 g1) 0) (= (g r20 g0) 0) (= (g r20 g1) 0) (= (g r21 g0) 0) (= (g r21 g1) 0) (= (g r22 g0) 0) (= (g r22 g1) 0) (= (g r23 g0) 0) (= (g r23 g1) 0) (= (g r24 g0) 0) (= (g r24 g1) 0) (= (g r25 g0) 0) (= (g r25 g1) 0) (= (g r26 g0) 0) (= (g r26 g1) 0) (= (g r27 g0) 0) (= (g r27 g1) 0) (= (g r28 g0) 0) (= (g r28 g1) 0) (= (g r29 g0) 0) (= (g r29 g1) 0) (= (g r30 g0) 0) (= (g r30 g1) 0) (= (g r31 g0) 0) (= (g r31 g1) 0) (= (g r32 g0) 0) (= (g r32 g1) 0) (= (g r33 g0) 0) (= (g r33 g1) 0) (= (g r34 g0) 0) (= (g r34 g1) 0) (= (g r35 g0) 0) (= (g r35 g1) 0) (= (g r36 g0) 0) (= (g r36 g1) 0) (= (g r37 g0) 0) (= (g r37 g1) 0) (= (g r38 g0) 0) (= (g r38 g1) 0) (= (g r39 g0) 0) (= (g r39 g1) 0) (= (g r40 g0) 0) (= (g r40 g1) 0) (= (g r41 g0) 0) (= (g r41 g1) 0) (= (g r42 g0) 0) (= (g r42 g1) 0) (= (g r43 g0) 0) (= (g r43 g1) 0) (= (g r44 g0) 0) (= (g r44 g1) 0)
                (= (y r0 y0) 1) (= (y r0 y1) 1) (= (y r1 y0) 0) (= (y r1 y1) 0) (= (y r2 y0) 0) (= (y r2 y1) 0) (= (y r3 y0) 0) (= (y r3 y1) 0) (= (y r4 y0) 0) (= (y r4 y1) 0) (= (y r5 y0) 0) (= (y r5 y1) 0) (= (y r6 y0) 0) (= (y r6 y1) 0) (= (y r7 y0) 0) (= (y r7 y1) 0) (= (y r8 y0) 0) (= (y r8 y1) 0) (= (y r9 y0) 0) (= (y r9 y1) 0) (= (y r10 y0) 0) (= (y r10 y1) 0) (= (y r11 y0) 0) (= (y r11 y1) 0) (= (y r12 y0) 0) (= (y r12 y1) 0) (= (y r13 y0) 0) (= (y r13 y1) 0) (= (y r14 y0) 0) (= (y r14 y1) 0) (= (y r15 y0) 0) (= (y r15 y1) 0) (= (y r16 y0) 0) (= (y r16 y1) 0) (= (y r17 y0) 0) (= (y r17 y1) 0) (= (y r18 y0) 0) (= (y r18 y1) 0) (= (y r19 y0) 0) (= (y r19 y1) 0) (= (y r20 y0) 0) (= (y r20 y1) 0) (= (y r21 y0) 0) (= (y r21 y1) 0) (= (y r22 y0) 0) (= (y r22 y1) 0) (= (y r23 y0) 0) (= (y r23 y1) 0) (= (y r24 y0) 0) (= (y r24 y1) 0) (= (y r25 y0) 0) (= (y r25 y1) 0) (= (y r26 y0) 0) (= (y r26 y1) 0) (= (y r27 y0) 0) (= (y r27 y1) 0) (= (y r28 y0) 0) (= (y r28 y1) 0) (= (y r29 y0) 0) (= (y r29 y1) 0) (= (y r30 y0) 0) (= (y r30 y1) 0) (= (y r31 y0) 0) (= (y r31 y1) 0) (= (y r32 y0) 0) (= (y r32 y1) 0) (= (y r33 y0) 0) (= (y r33 y1) 0) (= (y r34 y0) 0) (= (y r34 y1) 0) (= (y r35 y0) 0) (= (y r35 y1) 0) (= (y r36 y0) 0) (= (y r36 y1) 0) (= (y r37 y0) 0) (= (y r37 y1) 0) (= (y r38 y0) 0) (= (y r38 y1) 0) (= (y r39 y0) 0) (= (y r39 y1) 0) (= (y r40 y0) 0) (= (y r40 y1) 0) (= (y r41 y0) 0) (= (y r41 y1) 0) (= (y r42 y0) 0) (= (y r42 y1) 0) (= (y r43 y0) 0) (= (y r43 y1) 0) (= (y r44 y0) 0) (= (y r44 y1) 0)
                (= (hg r0) 2) (= (hg r1) 0) (= (hg r2) 0) (= (hg r3) 0) (= (hg r4) 0) (= (hg r5) 0) (= (hg r6) 0) (= (hg r7) 0) (= (hg r8) 0) (= (hg r9) 0) (= (hg r10) 0) (= (hg r11) 0) (= (hg r12) 0) (= (hg r13) 0) (= (hg r14) 0) (= (hg r15) 0) (= (hg r16) 0) (= (hg r17) 0) (= (hg r18) 0) (= (hg r19) 0) (= (hg r20) 0) (= (hg r21) 0) (= (hg r22) 0) (= (hg r23) 0) (= (hg r24) 0) (= (hg r25) 0) (= (hg r26) 0) (= (hg r27) 0) (= (hg r28) 0) (= (hg r29) 0) (= (hg r30) 0) (= (hg r31) 0) (= (hg r32) 0) (= (hg r33) 0) (= (hg r34) 0) (= (hg r35) 0) (= (hg r36) 0) (= (hg r37) 0) (= (hg r38) 0) (= (hg r39) 0) (= (hg r40) 0) (= (hg r41) 0) (= (hg r42) 0) (= (hg r43) 0) (= (hg r44) 0)
                (= (hy r0) 2) (= (hy r1) 0) (= (hy r2) 0) (= (hy r3) 0) (= (hy r4) 0) (= (hy r5) 0) (= (hy r6) 0) (= (hy r7) 0) (= (hy r8) 0) (= (hy r9) 0) (= (hy r10) 0) (= (hy r11) 0) (= (hy r12) 0) (= (hy r13) 0) (= (hy r14) 0) (= (hy r15) 0) (= (hy r16) 0) (= (hy r17) 0) (= (hy r18) 0) (= (hy r19) 0) (= (hy r20) 0) (= (hy r21) 0) (= (hy r22) 0) (= (hy r23) 0) (= (hy r24) 0) (= (hy r25) 0) (= (hy r26) 0) (= (hy r27) 0) (= (hy r28) 0) (= (hy r29) 0) (= (hy r30) 0) (= (hy r31) 0) (= (hy r32) 0) (= (hy r33) 0) (= (hy r34) 0) (= (hy r35) 0) (= (hy r36) 0) (= (hy r37) 0) (= (hy r38) 0) (= (hy r39) 0) (= (hy r40) 0) (= (hy r41) 0) (= (hy r42) 0) (= (hy r43) 0) (= (hy r44) 0)
            )

            (:goal
                (and
                    (gsd r0 g0) (gsd r0 g1) (gsd r1 g0) (gsd r1 g1) (gsd r2 g0) (gsd r2 g1) (gsd r3 g0) (gsd r3 g1) (gsd r4 g0) (gsd r4 g1) (gsd r5 g0) (gsd r5 g1) (gsd r6 g0) (gsd r6 g1) (gsd r7 g0) (gsd r7 g1) (gsd r8 g0) (gsd r8 g1) (gsd r9 g0) (gsd r9 g1) (gsd r10 g0) (gsd r10 g1) (gsd r11 g0) (gsd r11 g1) (gsd r12 g0) (gsd r12 g1) (gsd r13 g0) (gsd r13 g1) (gsd r14 g0) (gsd r14 g1) (gsd r15 g0) (gsd r15 g1) (gsd r16 g0) (gsd r16 g1) (gsd r17 g0) (gsd r17 g1) (gsd r18 g0) (gsd r18 g1) (gsd r19 g0) (gsd r19 g1) (gsd r20 g0) (gsd r20 g1) (gsd r21 g0) (gsd r21 g1) (gsd r22 g0) (gsd r22 g1)
                    (ysd r0 y0) (ysd r0 y1) (ysd r1 y0) (ysd r1 y1) (ysd r2 y0) (ysd r2 y1) (ysd r3 y0) (ysd r3 y1) (ysd r4 y0) (ysd r4 y1) (ysd r5 y0) (ysd r5 y1) (ysd r6 y0) (ysd r6 y1) (ysd r7 y0) (ysd r7 y1) (ysd r8 y0) (ysd r8 y1) (ysd r9 y0) (ysd r9 y1) (ysd r10 y0) (ysd r10 y1) (ysd r11 y0) (ysd r11 y1) (ysd r12 y0) (ysd r12 y1) (ysd r13 y0) (ysd r13 y1) (ysd r14 y0) (ysd r14 y1) (ysd r15 y0) (ysd r15 y1) (ysd r16 y0) (ysd r16 y1) (ysd r17 y0) (ysd r17 y1) (ysd r18 y0) (ysd r18 y1) (ysd r19 y0) (ysd r19 y1) (ysd r20 y0) (ysd r20 y1) (ysd r21 y0) (ysd r21 y1) (ysd r22 y0) (ysd r22 y1) (ysd r23 y0) (ysd r23 y1) (ysd r24 y0) (ysd r24 y1) (ysd r25 y0) (ysd r25 y1) (ysd r26 y0) (ysd r26 y1) (ysd r27 y0) (ysd r27 y1) (ysd r28 y0) (ysd r28 y1) (ysd r29 y0) (ysd r29 y1) (ysd r30 y0) (ysd r30 y1) (ysd r31 y0) (ysd r31 y1) (ysd r32 y0) (ysd r32 y1) (ysd r33 y0) (ysd r33 y1) (ysd r34 y0) (ysd r34 y1) (ysd r35 y0) (ysd r35 y1) (ysd r36 y0) (ysd r36 y1) (ysd r37 y0) (ysd r37 y1) (ysd r38 y0) (ysd r38 y1) (ysd r39 y0) (ysd r39 y1) (ysd r40 y0) (ysd r40 y1) (ysd r41 y0) (ysd r41 y1) (ysd r42 y0) (ysd r42 y1) (ysd r43 y0) (ysd r43 y1) (ysd r44 y0) (ysd r44 y1)
                    (= (hg r0) 2)
                    (= (hy r44) 2)
                )
            )
        )