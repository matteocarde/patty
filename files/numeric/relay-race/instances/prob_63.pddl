
        (define (problem prob63)
            (:domain relay-race)
            (:objects
              r0 r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 r11 r12 r13 r14 r15 r16 r17 r18 r19 r20 r21 r22 r23 r24 r25 r26 r27 r28 r29 r30 r31 r32 r33 r34 r35 r36 r37 r38 r39 r40 r41 r42 r43 r44 r45 r46 r47 r48 r49 r50 r51 r52 r53 r54 r55 r56 r57 r58 r59 r60 r61 r62 - runner
              P0 P1 Q0 Q1 - baton
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4) (= (i r5) 5) (= (i r6) 6) (= (i r7) 7) (= (i r8) 8) (= (i r9) 9) (= (i r10) 10) (= (i r11) 11) (= (i r12) 12) (= (i r13) 13) (= (i r14) 14) (= (i r15) 15) (= (i r16) 16) (= (i r17) 17) (= (i r18) 18) (= (i r19) 19) (= (i r20) 20) (= (i r21) 21) (= (i r22) 22) (= (i r23) 23) (= (i r24) 24) (= (i r25) 25) (= (i r26) 26) (= (i r27) 27) (= (i r28) 28) (= (i r29) 29) (= (i r30) 30) (= (i r31) 31) (= (i r32) 32) (= (i r33) 33) (= (i r34) 34) (= (i r35) 35) (= (i r36) 36) (= (i r37) 37) (= (i r38) 38) (= (i r39) 39) (= (i r40) 40) (= (i r41) 41) (= (i r42) 42) (= (i r43) 43) (= (i r44) 44) (= (i r45) 45) (= (i r46) 46) (= (i r47) 47) (= (i r48) 48) (= (i r49) 49) (= (i r50) 50) (= (i r51) 51) (= (i r52) 52) (= (i r53) 53) (= (i r54) 54) (= (i r55) 55) (= (i r56) 56) (= (i r57) 57) (= (i r58) 58) (= (i r59) 59) (= (i r60) 60) (= (i r61) 61) (= (i r62) 62)
                (next r0 r1) (next r1 r2) (next r2 r3) (next r3 r4) (next r4 r5) (next r5 r6) (next r6 r7) (next r7 r8) (next r8 r9) (next r9 r10) (next r10 r11) (next r11 r12) (next r12 r13) (next r13 r14) (next r14 r15) (next r15 r16) (next r16 r17) (next r17 r18) (next r18 r19) (next r19 r20) (next r20 r21) (next r21 r22) (next r22 r23) (next r23 r24) (next r24 r25) (next r25 r26) (next r26 r27) (next r27 r28) (next r28 r29) (next r29 r30) (next r30 r31) (next r31 r32) (next r32 r33) (next r33 r34) (next r34 r35) (next r35 r36) (next r36 r37) (next r37 r38) (next r38 r39) (next r39 r40) (next r40 r41) (next r41 r42) (next r42 r43) (next r43 r44) (next r44 r45) (next r45 r46) (next r46 r47) (next r47 r48) (next r48 r49) (next r49 r50) (next r50 r51) (next r51 r52) (next r52 r53) (next r53 r54) (next r54 r55) (next r55 r56) (next r56 r57) (next r57 r58) (next r58 r59) (next r59 r60) (next r60 r61) (next r61 r62)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80) (= (x r5) 100) (= (x r6) 120) (= (x r7) 140) (= (x r8) 160) (= (x r9) 180) (= (x r10) 200) (= (x r11) 220) (= (x r12) 240) (= (x r13) 260) (= (x r14) 280) (= (x r15) 300) (= (x r16) 320) (= (x r17) 340) (= (x r18) 360) (= (x r19) 380) (= (x r20) 400) (= (x r21) 420) (= (x r22) 440) (= (x r23) 460) (= (x r24) 480) (= (x r25) 500) (= (x r26) 520) (= (x r27) 540) (= (x r28) 560) (= (x r29) 580) (= (x r30) 600) (= (x r31) 620) (= (x r32) 640) (= (x r33) 660) (= (x r34) 680) (= (x r35) 700) (= (x r36) 720) (= (x r37) 740) (= (x r38) 760) (= (x r39) 780) (= (x r40) 800) (= (x r41) 820) (= (x r42) 840) (= (x r43) 860) (= (x r44) 880) (= (x r45) 900) (= (x r46) 920) (= (x r47) 940) (= (x r48) 960) (= (x r49) 980) (= (x r50) 1000) (= (x r51) 1020) (= (x r52) 1040) (= (x r53) 1060) (= (x r54) 1080) (= (x r55) 1100) (= (x r56) 1120) (= (x r57) 1140) (= (x r58) 1160) (= (x r59) 1180) (= (x r60) 1200) (= (x r61) 1220) (= (x r62) 1240)
                
                (= (b r0 P0) 1) (= (b r0 P1) 1) (= (b r1 P0) 0) (= (b r1 P1) 0) (= (b r2 P0) 0) (= (b r2 P1) 0) (= (b r3 P0) 0) (= (b r3 P1) 0) (= (b r4 P0) 0) (= (b r4 P1) 0) (= (b r5 P0) 0) (= (b r5 P1) 0) (= (b r6 P0) 0) (= (b r6 P1) 0) (= (b r7 P0) 0) (= (b r7 P1) 0) (= (b r8 P0) 0) (= (b r8 P1) 0) (= (b r9 P0) 0) (= (b r9 P1) 0) (= (b r10 P0) 0) (= (b r10 P1) 0) (= (b r11 P0) 0) (= (b r11 P1) 0) (= (b r12 P0) 0) (= (b r12 P1) 0) (= (b r13 P0) 0) (= (b r13 P1) 0) (= (b r14 P0) 0) (= (b r14 P1) 0) (= (b r15 P0) 0) (= (b r15 P1) 0) (= (b r16 P0) 0) (= (b r16 P1) 0) (= (b r17 P0) 0) (= (b r17 P1) 0) (= (b r18 P0) 0) (= (b r18 P1) 0) (= (b r19 P0) 0) (= (b r19 P1) 0) (= (b r20 P0) 0) (= (b r20 P1) 0) (= (b r21 P0) 0) (= (b r21 P1) 0) (= (b r22 P0) 0) (= (b r22 P1) 0) (= (b r23 P0) 0) (= (b r23 P1) 0) (= (b r24 P0) 0) (= (b r24 P1) 0) (= (b r25 P0) 0) (= (b r25 P1) 0) (= (b r26 P0) 0) (= (b r26 P1) 0) (= (b r27 P0) 0) (= (b r27 P1) 0) (= (b r28 P0) 0) (= (b r28 P1) 0) (= (b r29 P0) 0) (= (b r29 P1) 0) (= (b r30 P0) 0) (= (b r30 P1) 0) (= (b r31 P0) 0) (= (b r31 P1) 0) (= (b r32 P0) 0) (= (b r32 P1) 0) (= (b r33 P0) 0) (= (b r33 P1) 0) (= (b r34 P0) 0) (= (b r34 P1) 0) (= (b r35 P0) 0) (= (b r35 P1) 0) (= (b r36 P0) 0) (= (b r36 P1) 0) (= (b r37 P0) 0) (= (b r37 P1) 0) (= (b r38 P0) 0) (= (b r38 P1) 0) (= (b r39 P0) 0) (= (b r39 P1) 0) (= (b r40 P0) 0) (= (b r40 P1) 0) (= (b r41 P0) 0) (= (b r41 P1) 0) (= (b r42 P0) 0) (= (b r42 P1) 0) (= (b r43 P0) 0) (= (b r43 P1) 0) (= (b r44 P0) 0) (= (b r44 P1) 0) (= (b r45 P0) 0) (= (b r45 P1) 0) (= (b r46 P0) 0) (= (b r46 P1) 0) (= (b r47 P0) 0) (= (b r47 P1) 0) (= (b r48 P0) 0) (= (b r48 P1) 0) (= (b r49 P0) 0) (= (b r49 P1) 0) (= (b r50 P0) 0) (= (b r50 P1) 0) (= (b r51 P0) 0) (= (b r51 P1) 0) (= (b r52 P0) 0) (= (b r52 P1) 0) (= (b r53 P0) 0) (= (b r53 P1) 0) (= (b r54 P0) 0) (= (b r54 P1) 0) (= (b r55 P0) 0) (= (b r55 P1) 0) (= (b r56 P0) 0) (= (b r56 P1) 0) (= (b r57 P0) 0) (= (b r57 P1) 0) (= (b r58 P0) 0) (= (b r58 P1) 0) (= (b r59 P0) 0) (= (b r59 P1) 0) (= (b r60 P0) 0) (= (b r60 P1) 0) (= (b r61 P0) 0) (= (b r61 P1) 0) (= (b r62 P0) 0) (= (b r62 P1) 0)
                (= (b r0 Q0) 1) (= (b r0 Q1) 1) (= (b r1 Q0) 0) (= (b r1 Q1) 0) (= (b r2 Q0) 0) (= (b r2 Q1) 0) (= (b r3 Q0) 0) (= (b r3 Q1) 0) (= (b r4 Q0) 0) (= (b r4 Q1) 0) (= (b r5 Q0) 0) (= (b r5 Q1) 0) (= (b r6 Q0) 0) (= (b r6 Q1) 0) (= (b r7 Q0) 0) (= (b r7 Q1) 0) (= (b r8 Q0) 0) (= (b r8 Q1) 0) (= (b r9 Q0) 0) (= (b r9 Q1) 0) (= (b r10 Q0) 0) (= (b r10 Q1) 0) (= (b r11 Q0) 0) (= (b r11 Q1) 0) (= (b r12 Q0) 0) (= (b r12 Q1) 0) (= (b r13 Q0) 0) (= (b r13 Q1) 0) (= (b r14 Q0) 0) (= (b r14 Q1) 0) (= (b r15 Q0) 0) (= (b r15 Q1) 0) (= (b r16 Q0) 0) (= (b r16 Q1) 0) (= (b r17 Q0) 0) (= (b r17 Q1) 0) (= (b r18 Q0) 0) (= (b r18 Q1) 0) (= (b r19 Q0) 0) (= (b r19 Q1) 0) (= (b r20 Q0) 0) (= (b r20 Q1) 0) (= (b r21 Q0) 0) (= (b r21 Q1) 0) (= (b r22 Q0) 0) (= (b r22 Q1) 0) (= (b r23 Q0) 0) (= (b r23 Q1) 0) (= (b r24 Q0) 0) (= (b r24 Q1) 0) (= (b r25 Q0) 0) (= (b r25 Q1) 0) (= (b r26 Q0) 0) (= (b r26 Q1) 0) (= (b r27 Q0) 0) (= (b r27 Q1) 0) (= (b r28 Q0) 0) (= (b r28 Q1) 0) (= (b r29 Q0) 0) (= (b r29 Q1) 0) (= (b r30 Q0) 0) (= (b r30 Q1) 0) (= (b r31 Q0) 0) (= (b r31 Q1) 0) (= (b r32 Q0) 0) (= (b r32 Q1) 0) (= (b r33 Q0) 0) (= (b r33 Q1) 0) (= (b r34 Q0) 0) (= (b r34 Q1) 0) (= (b r35 Q0) 0) (= (b r35 Q1) 0) (= (b r36 Q0) 0) (= (b r36 Q1) 0) (= (b r37 Q0) 0) (= (b r37 Q1) 0) (= (b r38 Q0) 0) (= (b r38 Q1) 0) (= (b r39 Q0) 0) (= (b r39 Q1) 0) (= (b r40 Q0) 0) (= (b r40 Q1) 0) (= (b r41 Q0) 0) (= (b r41 Q1) 0) (= (b r42 Q0) 0) (= (b r42 Q1) 0) (= (b r43 Q0) 0) (= (b r43 Q1) 0) (= (b r44 Q0) 0) (= (b r44 Q1) 0) (= (b r45 Q0) 0) (= (b r45 Q1) 0) (= (b r46 Q0) 0) (= (b r46 Q1) 0) (= (b r47 Q0) 0) (= (b r47 Q1) 0) (= (b r48 Q0) 0) (= (b r48 Q1) 0) (= (b r49 Q0) 0) (= (b r49 Q1) 0) (= (b r50 Q0) 0) (= (b r50 Q1) 0) (= (b r51 Q0) 0) (= (b r51 Q1) 0) (= (b r52 Q0) 0) (= (b r52 Q1) 0) (= (b r53 Q0) 0) (= (b r53 Q1) 0) (= (b r54 Q0) 0) (= (b r54 Q1) 0) (= (b r55 Q0) 0) (= (b r55 Q1) 0) (= (b r56 Q0) 0) (= (b r56 Q1) 0) (= (b r57 Q0) 0) (= (b r57 Q1) 0) (= (b r58 Q0) 0) (= (b r58 Q1) 0) (= (b r59 Q0) 0) (= (b r59 Q1) 0) (= (b r60 Q0) 0) (= (b r60 Q1) 0) (= (b r61 Q0) 0) (= (b r61 Q1) 0) (= (b r62 Q0) 0) (= (b r62 Q1) 0)
                (= (h r0) 4) (= (h r1) 0) (= (h r2) 0) (= (h r3) 0) (= (h r4) 0) (= (h r5) 0) (= (h r6) 0) (= (h r7) 0) (= (h r8) 0) (= (h r9) 0) (= (h r10) 0) (= (h r11) 0) (= (h r12) 0) (= (h r13) 0) (= (h r14) 0) (= (h r15) 0) (= (h r16) 0) (= (h r17) 0) (= (h r18) 0) (= (h r19) 0) (= (h r20) 0) (= (h r21) 0) (= (h r22) 0) (= (h r23) 0) (= (h r24) 0) (= (h r25) 0) (= (h r26) 0) (= (h r27) 0) (= (h r28) 0) (= (h r29) 0) (= (h r30) 0) (= (h r31) 0) (= (h r32) 0) (= (h r33) 0) (= (h r34) 0) (= (h r35) 0) (= (h r36) 0) (= (h r37) 0) (= (h r38) 0) (= (h r39) 0) (= (h r40) 0) (= (h r41) 0) (= (h r42) 0) (= (h r43) 0) (= (h r44) 0) (= (h r45) 0) (= (h r46) 0) (= (h r47) 0) (= (h r48) 0) (= (h r49) 0) (= (h r50) 0) (= (h r51) 0) (= (h r52) 0) (= (h r53) 0) (= (h r54) 0) (= (h r55) 0) (= (h r56) 0) (= (h r57) 0) (= (h r58) 0) (= (h r59) 0) (= (h r60) 0) (= (h r61) 0) (= (h r62) 0)
                
                (td r0 P0) (td r0 P1)
                (td r0 Q0) (td r0 Q1)
            )

            (:goal
                (and
                    (td r0 P0) (td r0 P1) (td r1 P0) (td r1 P1) (td r2 P0) (td r2 P1) (td r3 P0) (td r3 P1) (td r4 P0) (td r4 P1) (td r5 P0) (td r5 P1) (td r6 P0) (td r6 P1) (td r7 P0) (td r7 P1) (td r8 P0) (td r8 P1) (td r9 P0) (td r9 P1) (td r10 P0) (td r10 P1) (td r11 P0) (td r11 P1) (td r12 P0) (td r12 P1) (td r13 P0) (td r13 P1) (td r14 P0) (td r14 P1) (td r15 P0) (td r15 P1) (td r16 P0) (td r16 P1) (td r17 P0) (td r17 P1) (td r18 P0) (td r18 P1) (td r19 P0) (td r19 P1) (td r20 P0) (td r20 P1) (td r21 P0) (td r21 P1) (td r22 P0) (td r22 P1) (td r23 P0) (td r23 P1) (td r24 P0) (td r24 P1) (td r25 P0) (td r25 P1) (td r26 P0) (td r26 P1) (td r27 P0) (td r27 P1) (td r28 P0) (td r28 P1) (td r29 P0) (td r29 P1) (td r30 P0) (td r30 P1) (td r31 P0) (td r31 P1)
                    (not (td r32 P0)) (not (td r32 P1)) (not (td r33 P0)) (not (td r33 P1)) (not (td r34 P0)) (not (td r34 P1)) (not (td r35 P0)) (not (td r35 P1)) (not (td r36 P0)) (not (td r36 P1)) (not (td r37 P0)) (not (td r37 P1)) (not (td r38 P0)) (not (td r38 P1)) (not (td r39 P0)) (not (td r39 P1)) (not (td r40 P0)) (not (td r40 P1)) (not (td r41 P0)) (not (td r41 P1)) (not (td r42 P0)) (not (td r42 P1)) (not (td r43 P0)) (not (td r43 P1)) (not (td r44 P0)) (not (td r44 P1)) (not (td r45 P0)) (not (td r45 P1)) (not (td r46 P0)) (not (td r46 P1)) (not (td r47 P0)) (not (td r47 P1)) (not (td r48 P0)) (not (td r48 P1)) (not (td r49 P0)) (not (td r49 P1)) (not (td r50 P0)) (not (td r50 P1)) (not (td r51 P0)) (not (td r51 P1)) (not (td r52 P0)) (not (td r52 P1)) (not (td r53 P0)) (not (td r53 P1)) (not (td r54 P0)) (not (td r54 P1)) (not (td r55 P0)) (not (td r55 P1)) (not (td r56 P0)) (not (td r56 P1)) (not (td r57 P0)) (not (td r57 P1)) (not (td r58 P0)) (not (td r58 P1)) (not (td r59 P0)) (not (td r59 P1)) (not (td r60 P0)) (not (td r60 P1)) (not (td r61 P0)) (not (td r61 P1)) (not (td r62 P0)) (not (td r62 P1))
                    (td r0 Q0) (td r0 Q1) (td r1 Q0) (td r1 Q1) (td r2 Q0) (td r2 Q1) (td r3 Q0) (td r3 Q1) (td r4 Q0) (td r4 Q1) (td r5 Q0) (td r5 Q1) (td r6 Q0) (td r6 Q1) (td r7 Q0) (td r7 Q1) (td r8 Q0) (td r8 Q1) (td r9 Q0) (td r9 Q1) (td r10 Q0) (td r10 Q1) (td r11 Q0) (td r11 Q1) (td r12 Q0) (td r12 Q1) (td r13 Q0) (td r13 Q1) (td r14 Q0) (td r14 Q1) (td r15 Q0) (td r15 Q1) (td r16 Q0) (td r16 Q1) (td r17 Q0) (td r17 Q1) (td r18 Q0) (td r18 Q1) (td r19 Q0) (td r19 Q1) (td r20 Q0) (td r20 Q1) (td r21 Q0) (td r21 Q1) (td r22 Q0) (td r22 Q1) (td r23 Q0) (td r23 Q1) (td r24 Q0) (td r24 Q1) (td r25 Q0) (td r25 Q1) (td r26 Q0) (td r26 Q1) (td r27 Q0) (td r27 Q1) (td r28 Q0) (td r28 Q1) (td r29 Q0) (td r29 Q1) (td r30 Q0) (td r30 Q1) (td r31 Q0) (td r31 Q1) (td r32 Q0) (td r32 Q1) (td r33 Q0) (td r33 Q1) (td r34 Q0) (td r34 Q1) (td r35 Q0) (td r35 Q1) (td r36 Q0) (td r36 Q1) (td r37 Q0) (td r37 Q1) (td r38 Q0) (td r38 Q1) (td r39 Q0) (td r39 Q1) (td r40 Q0) (td r40 Q1) (td r41 Q0) (td r41 Q1) (td r42 Q0) (td r42 Q1) (td r43 Q0) (td r43 Q1) (td r44 Q0) (td r44 Q1) (td r45 Q0) (td r45 Q1) (td r46 Q0) (td r46 Q1) (td r47 Q0) (td r47 Q1) (td r48 Q0) (td r48 Q1) (td r49 Q0) (td r49 Q1) (td r50 Q0) (td r50 Q1) (td r51 Q0) (td r51 Q1) (td r52 Q0) (td r52 Q1) (td r53 Q0) (td r53 Q1) (td r54 Q0) (td r54 Q1) (td r55 Q0) (td r55 Q1) (td r56 Q0) (td r56 Q1) (td r57 Q0) (td r57 Q1) (td r58 Q0) (td r58 Q1) (td r59 Q0) (td r59 Q1) (td r60 Q0) (td r60 Q1) (td r61 Q0) (td r61 Q1) (td r62 Q0) (td r62 Q1)
                    (= (b r0 P0) 1) (= (b r0 P1) 1)
                    (= (b r62 Q0) 1) (= (b r62 Q1) 1)
                )
            )
        )