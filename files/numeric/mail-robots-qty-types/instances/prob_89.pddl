
        (define (problem prob89)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 r11 r12 r13 r14 r15 r16 r17 r18 r19 r20 r21 r22 r23 r24 r25 r26 r27 r28 r29 r30 r31 r32 r33 r34 r35 r36 r37 r38 r39 r40 r41 r42 r43 r44 r45 r46 r47 r48 r49 r50 r51 r52 r53 r54 r55 r56 r57 r58 r59 r60 r61 r62 r63 r64 r65 r66 r67 r68 r69 r70 r71 r72 r73 r74 r75 r76 r77 r78 r79 r80 r81 r82 r83 r84 r85 r86 r87 r88 - robot
              g0 g1 - green
              y0 y1 - yellow
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4) (= (i r5) 5) (= (i r6) 6) (= (i r7) 7) (= (i r8) 8) (= (i r9) 9) (= (i r10) 10) (= (i r11) 11) (= (i r12) 12) (= (i r13) 13) (= (i r14) 14) (= (i r15) 15) (= (i r16) 16) (= (i r17) 17) (= (i r18) 18) (= (i r19) 19) (= (i r20) 20) (= (i r21) 21) (= (i r22) 22) (= (i r23) 23) (= (i r24) 24) (= (i r25) 25) (= (i r26) 26) (= (i r27) 27) (= (i r28) 28) (= (i r29) 29) (= (i r30) 30) (= (i r31) 31) (= (i r32) 32) (= (i r33) 33) (= (i r34) 34) (= (i r35) 35) (= (i r36) 36) (= (i r37) 37) (= (i r38) 38) (= (i r39) 39) (= (i r40) 40) (= (i r41) 41) (= (i r42) 42) (= (i r43) 43) (= (i r44) 44) (= (i r45) 45) (= (i r46) 46) (= (i r47) 47) (= (i r48) 48) (= (i r49) 49) (= (i r50) 50) (= (i r51) 51) (= (i r52) 52) (= (i r53) 53) (= (i r54) 54) (= (i r55) 55) (= (i r56) 56) (= (i r57) 57) (= (i r58) 58) (= (i r59) 59) (= (i r60) 60) (= (i r61) 61) (= (i r62) 62) (= (i r63) 63) (= (i r64) 64) (= (i r65) 65) (= (i r66) 66) (= (i r67) 67) (= (i r68) 68) (= (i r69) 69) (= (i r70) 70) (= (i r71) 71) (= (i r72) 72) (= (i r73) 73) (= (i r74) 74) (= (i r75) 75) (= (i r76) 76) (= (i r77) 77) (= (i r78) 78) (= (i r79) 79) (= (i r80) 80) (= (i r81) 81) (= (i r82) 82) (= (i r83) 83) (= (i r84) 84) (= (i r85) 85) (= (i r86) 86) (= (i r87) 87) (= (i r88) 88)
                (next r0 r1) (next r1 r2) (next r2 r3) (next r3 r4) (next r4 r5) (next r5 r6) (next r6 r7) (next r7 r8) (next r8 r9) (next r9 r10) (next r10 r11) (next r11 r12) (next r12 r13) (next r13 r14) (next r14 r15) (next r15 r16) (next r16 r17) (next r17 r18) (next r18 r19) (next r19 r20) (next r20 r21) (next r21 r22) (next r22 r23) (next r23 r24) (next r24 r25) (next r25 r26) (next r26 r27) (next r27 r28) (next r28 r29) (next r29 r30) (next r30 r31) (next r31 r32) (next r32 r33) (next r33 r34) (next r34 r35) (next r35 r36) (next r36 r37) (next r37 r38) (next r38 r39) (next r39 r40) (next r40 r41) (next r41 r42) (next r42 r43) (next r43 r44) (next r44 r45) (next r45 r46) (next r46 r47) (next r47 r48) (next r48 r49) (next r49 r50) (next r50 r51) (next r51 r52) (next r52 r53) (next r53 r54) (next r54 r55) (next r55 r56) (next r56 r57) (next r57 r58) (next r58 r59) (next r59 r60) (next r60 r61) (next r61 r62) (next r62 r63) (next r63 r64) (next r64 r65) (next r65 r66) (next r66 r67) (next r67 r68) (next r68 r69) (next r69 r70) (next r70 r71) (next r71 r72) (next r72 r73) (next r73 r74) (next r74 r75) (next r75 r76) (next r76 r77) (next r77 r78) (next r78 r79) (next r79 r80) (next r80 r81) (next r81 r82) (next r82 r83) (next r83 r84) (next r84 r85) (next r85 r86) (next r86 r87) (next r87 r88)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80) (= (x r5) 100) (= (x r6) 120) (= (x r7) 140) (= (x r8) 160) (= (x r9) 180) (= (x r10) 200) (= (x r11) 220) (= (x r12) 240) (= (x r13) 260) (= (x r14) 280) (= (x r15) 300) (= (x r16) 320) (= (x r17) 340) (= (x r18) 360) (= (x r19) 380) (= (x r20) 400) (= (x r21) 420) (= (x r22) 440) (= (x r23) 460) (= (x r24) 480) (= (x r25) 500) (= (x r26) 520) (= (x r27) 540) (= (x r28) 560) (= (x r29) 580) (= (x r30) 600) (= (x r31) 620) (= (x r32) 640) (= (x r33) 660) (= (x r34) 680) (= (x r35) 700) (= (x r36) 720) (= (x r37) 740) (= (x r38) 760) (= (x r39) 780) (= (x r40) 800) (= (x r41) 820) (= (x r42) 840) (= (x r43) 860) (= (x r44) 880) (= (x r45) 900) (= (x r46) 920) (= (x r47) 940) (= (x r48) 960) (= (x r49) 980) (= (x r50) 1000) (= (x r51) 1020) (= (x r52) 1040) (= (x r53) 1060) (= (x r54) 1080) (= (x r55) 1100) (= (x r56) 1120) (= (x r57) 1140) (= (x r58) 1160) (= (x r59) 1180) (= (x r60) 1200) (= (x r61) 1220) (= (x r62) 1240) (= (x r63) 1260) (= (x r64) 1280) (= (x r65) 1300) (= (x r66) 1320) (= (x r67) 1340) (= (x r68) 1360) (= (x r69) 1380) (= (x r70) 1400) (= (x r71) 1420) (= (x r72) 1440) (= (x r73) 1460) (= (x r74) 1480) (= (x r75) 1500) (= (x r76) 1520) (= (x r77) 1540) (= (x r78) 1560) (= (x r79) 1580) (= (x r80) 1600) (= (x r81) 1620) (= (x r82) 1640) (= (x r83) 1660) (= (x r84) 1680) (= (x r85) 1700) (= (x r86) 1720) (= (x r87) 1740) (= (x r88) 1760)
                
                (= (g r0 g0) 1) (= (g r0 g1) 1) (= (g r1 g0) 0) (= (g r1 g1) 0) (= (g r2 g0) 0) (= (g r2 g1) 0) (= (g r3 g0) 0) (= (g r3 g1) 0) (= (g r4 g0) 0) (= (g r4 g1) 0) (= (g r5 g0) 0) (= (g r5 g1) 0) (= (g r6 g0) 0) (= (g r6 g1) 0) (= (g r7 g0) 0) (= (g r7 g1) 0) (= (g r8 g0) 0) (= (g r8 g1) 0) (= (g r9 g0) 0) (= (g r9 g1) 0) (= (g r10 g0) 0) (= (g r10 g1) 0) (= (g r11 g0) 0) (= (g r11 g1) 0) (= (g r12 g0) 0) (= (g r12 g1) 0) (= (g r13 g0) 0) (= (g r13 g1) 0) (= (g r14 g0) 0) (= (g r14 g1) 0) (= (g r15 g0) 0) (= (g r15 g1) 0) (= (g r16 g0) 0) (= (g r16 g1) 0) (= (g r17 g0) 0) (= (g r17 g1) 0) (= (g r18 g0) 0) (= (g r18 g1) 0) (= (g r19 g0) 0) (= (g r19 g1) 0) (= (g r20 g0) 0) (= (g r20 g1) 0) (= (g r21 g0) 0) (= (g r21 g1) 0) (= (g r22 g0) 0) (= (g r22 g1) 0) (= (g r23 g0) 0) (= (g r23 g1) 0) (= (g r24 g0) 0) (= (g r24 g1) 0) (= (g r25 g0) 0) (= (g r25 g1) 0) (= (g r26 g0) 0) (= (g r26 g1) 0) (= (g r27 g0) 0) (= (g r27 g1) 0) (= (g r28 g0) 0) (= (g r28 g1) 0) (= (g r29 g0) 0) (= (g r29 g1) 0) (= (g r30 g0) 0) (= (g r30 g1) 0) (= (g r31 g0) 0) (= (g r31 g1) 0) (= (g r32 g0) 0) (= (g r32 g1) 0) (= (g r33 g0) 0) (= (g r33 g1) 0) (= (g r34 g0) 0) (= (g r34 g1) 0) (= (g r35 g0) 0) (= (g r35 g1) 0) (= (g r36 g0) 0) (= (g r36 g1) 0) (= (g r37 g0) 0) (= (g r37 g1) 0) (= (g r38 g0) 0) (= (g r38 g1) 0) (= (g r39 g0) 0) (= (g r39 g1) 0) (= (g r40 g0) 0) (= (g r40 g1) 0) (= (g r41 g0) 0) (= (g r41 g1) 0) (= (g r42 g0) 0) (= (g r42 g1) 0) (= (g r43 g0) 0) (= (g r43 g1) 0) (= (g r44 g0) 0) (= (g r44 g1) 0) (= (g r45 g0) 0) (= (g r45 g1) 0) (= (g r46 g0) 0) (= (g r46 g1) 0) (= (g r47 g0) 0) (= (g r47 g1) 0) (= (g r48 g0) 0) (= (g r48 g1) 0) (= (g r49 g0) 0) (= (g r49 g1) 0) (= (g r50 g0) 0) (= (g r50 g1) 0) (= (g r51 g0) 0) (= (g r51 g1) 0) (= (g r52 g0) 0) (= (g r52 g1) 0) (= (g r53 g0) 0) (= (g r53 g1) 0) (= (g r54 g0) 0) (= (g r54 g1) 0) (= (g r55 g0) 0) (= (g r55 g1) 0) (= (g r56 g0) 0) (= (g r56 g1) 0) (= (g r57 g0) 0) (= (g r57 g1) 0) (= (g r58 g0) 0) (= (g r58 g1) 0) (= (g r59 g0) 0) (= (g r59 g1) 0) (= (g r60 g0) 0) (= (g r60 g1) 0) (= (g r61 g0) 0) (= (g r61 g1) 0) (= (g r62 g0) 0) (= (g r62 g1) 0) (= (g r63 g0) 0) (= (g r63 g1) 0) (= (g r64 g0) 0) (= (g r64 g1) 0) (= (g r65 g0) 0) (= (g r65 g1) 0) (= (g r66 g0) 0) (= (g r66 g1) 0) (= (g r67 g0) 0) (= (g r67 g1) 0) (= (g r68 g0) 0) (= (g r68 g1) 0) (= (g r69 g0) 0) (= (g r69 g1) 0) (= (g r70 g0) 0) (= (g r70 g1) 0) (= (g r71 g0) 0) (= (g r71 g1) 0) (= (g r72 g0) 0) (= (g r72 g1) 0) (= (g r73 g0) 0) (= (g r73 g1) 0) (= (g r74 g0) 0) (= (g r74 g1) 0) (= (g r75 g0) 0) (= (g r75 g1) 0) (= (g r76 g0) 0) (= (g r76 g1) 0) (= (g r77 g0) 0) (= (g r77 g1) 0) (= (g r78 g0) 0) (= (g r78 g1) 0) (= (g r79 g0) 0) (= (g r79 g1) 0) (= (g r80 g0) 0) (= (g r80 g1) 0) (= (g r81 g0) 0) (= (g r81 g1) 0) (= (g r82 g0) 0) (= (g r82 g1) 0) (= (g r83 g0) 0) (= (g r83 g1) 0) (= (g r84 g0) 0) (= (g r84 g1) 0) (= (g r85 g0) 0) (= (g r85 g1) 0) (= (g r86 g0) 0) (= (g r86 g1) 0) (= (g r87 g0) 0) (= (g r87 g1) 0) (= (g r88 g0) 0) (= (g r88 g1) 0)
                (= (y r0 y0) 1) (= (y r0 y1) 1) (= (y r1 y0) 0) (= (y r1 y1) 0) (= (y r2 y0) 0) (= (y r2 y1) 0) (= (y r3 y0) 0) (= (y r3 y1) 0) (= (y r4 y0) 0) (= (y r4 y1) 0) (= (y r5 y0) 0) (= (y r5 y1) 0) (= (y r6 y0) 0) (= (y r6 y1) 0) (= (y r7 y0) 0) (= (y r7 y1) 0) (= (y r8 y0) 0) (= (y r8 y1) 0) (= (y r9 y0) 0) (= (y r9 y1) 0) (= (y r10 y0) 0) (= (y r10 y1) 0) (= (y r11 y0) 0) (= (y r11 y1) 0) (= (y r12 y0) 0) (= (y r12 y1) 0) (= (y r13 y0) 0) (= (y r13 y1) 0) (= (y r14 y0) 0) (= (y r14 y1) 0) (= (y r15 y0) 0) (= (y r15 y1) 0) (= (y r16 y0) 0) (= (y r16 y1) 0) (= (y r17 y0) 0) (= (y r17 y1) 0) (= (y r18 y0) 0) (= (y r18 y1) 0) (= (y r19 y0) 0) (= (y r19 y1) 0) (= (y r20 y0) 0) (= (y r20 y1) 0) (= (y r21 y0) 0) (= (y r21 y1) 0) (= (y r22 y0) 0) (= (y r22 y1) 0) (= (y r23 y0) 0) (= (y r23 y1) 0) (= (y r24 y0) 0) (= (y r24 y1) 0) (= (y r25 y0) 0) (= (y r25 y1) 0) (= (y r26 y0) 0) (= (y r26 y1) 0) (= (y r27 y0) 0) (= (y r27 y1) 0) (= (y r28 y0) 0) (= (y r28 y1) 0) (= (y r29 y0) 0) (= (y r29 y1) 0) (= (y r30 y0) 0) (= (y r30 y1) 0) (= (y r31 y0) 0) (= (y r31 y1) 0) (= (y r32 y0) 0) (= (y r32 y1) 0) (= (y r33 y0) 0) (= (y r33 y1) 0) (= (y r34 y0) 0) (= (y r34 y1) 0) (= (y r35 y0) 0) (= (y r35 y1) 0) (= (y r36 y0) 0) (= (y r36 y1) 0) (= (y r37 y0) 0) (= (y r37 y1) 0) (= (y r38 y0) 0) (= (y r38 y1) 0) (= (y r39 y0) 0) (= (y r39 y1) 0) (= (y r40 y0) 0) (= (y r40 y1) 0) (= (y r41 y0) 0) (= (y r41 y1) 0) (= (y r42 y0) 0) (= (y r42 y1) 0) (= (y r43 y0) 0) (= (y r43 y1) 0) (= (y r44 y0) 0) (= (y r44 y1) 0) (= (y r45 y0) 0) (= (y r45 y1) 0) (= (y r46 y0) 0) (= (y r46 y1) 0) (= (y r47 y0) 0) (= (y r47 y1) 0) (= (y r48 y0) 0) (= (y r48 y1) 0) (= (y r49 y0) 0) (= (y r49 y1) 0) (= (y r50 y0) 0) (= (y r50 y1) 0) (= (y r51 y0) 0) (= (y r51 y1) 0) (= (y r52 y0) 0) (= (y r52 y1) 0) (= (y r53 y0) 0) (= (y r53 y1) 0) (= (y r54 y0) 0) (= (y r54 y1) 0) (= (y r55 y0) 0) (= (y r55 y1) 0) (= (y r56 y0) 0) (= (y r56 y1) 0) (= (y r57 y0) 0) (= (y r57 y1) 0) (= (y r58 y0) 0) (= (y r58 y1) 0) (= (y r59 y0) 0) (= (y r59 y1) 0) (= (y r60 y0) 0) (= (y r60 y1) 0) (= (y r61 y0) 0) (= (y r61 y1) 0) (= (y r62 y0) 0) (= (y r62 y1) 0) (= (y r63 y0) 0) (= (y r63 y1) 0) (= (y r64 y0) 0) (= (y r64 y1) 0) (= (y r65 y0) 0) (= (y r65 y1) 0) (= (y r66 y0) 0) (= (y r66 y1) 0) (= (y r67 y0) 0) (= (y r67 y1) 0) (= (y r68 y0) 0) (= (y r68 y1) 0) (= (y r69 y0) 0) (= (y r69 y1) 0) (= (y r70 y0) 0) (= (y r70 y1) 0) (= (y r71 y0) 0) (= (y r71 y1) 0) (= (y r72 y0) 0) (= (y r72 y1) 0) (= (y r73 y0) 0) (= (y r73 y1) 0) (= (y r74 y0) 0) (= (y r74 y1) 0) (= (y r75 y0) 0) (= (y r75 y1) 0) (= (y r76 y0) 0) (= (y r76 y1) 0) (= (y r77 y0) 0) (= (y r77 y1) 0) (= (y r78 y0) 0) (= (y r78 y1) 0) (= (y r79 y0) 0) (= (y r79 y1) 0) (= (y r80 y0) 0) (= (y r80 y1) 0) (= (y r81 y0) 0) (= (y r81 y1) 0) (= (y r82 y0) 0) (= (y r82 y1) 0) (= (y r83 y0) 0) (= (y r83 y1) 0) (= (y r84 y0) 0) (= (y r84 y1) 0) (= (y r85 y0) 0) (= (y r85 y1) 0) (= (y r86 y0) 0) (= (y r86 y1) 0) (= (y r87 y0) 0) (= (y r87 y1) 0) (= (y r88 y0) 0) (= (y r88 y1) 0)
                (= (hg r0) 2) (= (hg r1) 0) (= (hg r2) 0) (= (hg r3) 0) (= (hg r4) 0) (= (hg r5) 0) (= (hg r6) 0) (= (hg r7) 0) (= (hg r8) 0) (= (hg r9) 0) (= (hg r10) 0) (= (hg r11) 0) (= (hg r12) 0) (= (hg r13) 0) (= (hg r14) 0) (= (hg r15) 0) (= (hg r16) 0) (= (hg r17) 0) (= (hg r18) 0) (= (hg r19) 0) (= (hg r20) 0) (= (hg r21) 0) (= (hg r22) 0) (= (hg r23) 0) (= (hg r24) 0) (= (hg r25) 0) (= (hg r26) 0) (= (hg r27) 0) (= (hg r28) 0) (= (hg r29) 0) (= (hg r30) 0) (= (hg r31) 0) (= (hg r32) 0) (= (hg r33) 0) (= (hg r34) 0) (= (hg r35) 0) (= (hg r36) 0) (= (hg r37) 0) (= (hg r38) 0) (= (hg r39) 0) (= (hg r40) 0) (= (hg r41) 0) (= (hg r42) 0) (= (hg r43) 0) (= (hg r44) 0) (= (hg r45) 0) (= (hg r46) 0) (= (hg r47) 0) (= (hg r48) 0) (= (hg r49) 0) (= (hg r50) 0) (= (hg r51) 0) (= (hg r52) 0) (= (hg r53) 0) (= (hg r54) 0) (= (hg r55) 0) (= (hg r56) 0) (= (hg r57) 0) (= (hg r58) 0) (= (hg r59) 0) (= (hg r60) 0) (= (hg r61) 0) (= (hg r62) 0) (= (hg r63) 0) (= (hg r64) 0) (= (hg r65) 0) (= (hg r66) 0) (= (hg r67) 0) (= (hg r68) 0) (= (hg r69) 0) (= (hg r70) 0) (= (hg r71) 0) (= (hg r72) 0) (= (hg r73) 0) (= (hg r74) 0) (= (hg r75) 0) (= (hg r76) 0) (= (hg r77) 0) (= (hg r78) 0) (= (hg r79) 0) (= (hg r80) 0) (= (hg r81) 0) (= (hg r82) 0) (= (hg r83) 0) (= (hg r84) 0) (= (hg r85) 0) (= (hg r86) 0) (= (hg r87) 0) (= (hg r88) 0)
                (= (hy r0) 2) (= (hy r1) 0) (= (hy r2) 0) (= (hy r3) 0) (= (hy r4) 0) (= (hy r5) 0) (= (hy r6) 0) (= (hy r7) 0) (= (hy r8) 0) (= (hy r9) 0) (= (hy r10) 0) (= (hy r11) 0) (= (hy r12) 0) (= (hy r13) 0) (= (hy r14) 0) (= (hy r15) 0) (= (hy r16) 0) (= (hy r17) 0) (= (hy r18) 0) (= (hy r19) 0) (= (hy r20) 0) (= (hy r21) 0) (= (hy r22) 0) (= (hy r23) 0) (= (hy r24) 0) (= (hy r25) 0) (= (hy r26) 0) (= (hy r27) 0) (= (hy r28) 0) (= (hy r29) 0) (= (hy r30) 0) (= (hy r31) 0) (= (hy r32) 0) (= (hy r33) 0) (= (hy r34) 0) (= (hy r35) 0) (= (hy r36) 0) (= (hy r37) 0) (= (hy r38) 0) (= (hy r39) 0) (= (hy r40) 0) (= (hy r41) 0) (= (hy r42) 0) (= (hy r43) 0) (= (hy r44) 0) (= (hy r45) 0) (= (hy r46) 0) (= (hy r47) 0) (= (hy r48) 0) (= (hy r49) 0) (= (hy r50) 0) (= (hy r51) 0) (= (hy r52) 0) (= (hy r53) 0) (= (hy r54) 0) (= (hy r55) 0) (= (hy r56) 0) (= (hy r57) 0) (= (hy r58) 0) (= (hy r59) 0) (= (hy r60) 0) (= (hy r61) 0) (= (hy r62) 0) (= (hy r63) 0) (= (hy r64) 0) (= (hy r65) 0) (= (hy r66) 0) (= (hy r67) 0) (= (hy r68) 0) (= (hy r69) 0) (= (hy r70) 0) (= (hy r71) 0) (= (hy r72) 0) (= (hy r73) 0) (= (hy r74) 0) (= (hy r75) 0) (= (hy r76) 0) (= (hy r77) 0) (= (hy r78) 0) (= (hy r79) 0) (= (hy r80) 0) (= (hy r81) 0) (= (hy r82) 0) (= (hy r83) 0) (= (hy r84) 0) (= (hy r85) 0) (= (hy r86) 0) (= (hy r87) 0) (= (hy r88) 0)
            )

            (:goal
                (and
                    (gsd r0 g0) (gsd r0 g1) (gsd r1 g0) (gsd r1 g1) (gsd r2 g0) (gsd r2 g1) (gsd r3 g0) (gsd r3 g1) (gsd r4 g0) (gsd r4 g1) (gsd r5 g0) (gsd r5 g1) (gsd r6 g0) (gsd r6 g1) (gsd r7 g0) (gsd r7 g1) (gsd r8 g0) (gsd r8 g1) (gsd r9 g0) (gsd r9 g1) (gsd r10 g0) (gsd r10 g1) (gsd r11 g0) (gsd r11 g1) (gsd r12 g0) (gsd r12 g1) (gsd r13 g0) (gsd r13 g1) (gsd r14 g0) (gsd r14 g1) (gsd r15 g0) (gsd r15 g1) (gsd r16 g0) (gsd r16 g1) (gsd r17 g0) (gsd r17 g1) (gsd r18 g0) (gsd r18 g1) (gsd r19 g0) (gsd r19 g1) (gsd r20 g0) (gsd r20 g1) (gsd r21 g0) (gsd r21 g1) (gsd r22 g0) (gsd r22 g1) (gsd r23 g0) (gsd r23 g1) (gsd r24 g0) (gsd r24 g1) (gsd r25 g0) (gsd r25 g1) (gsd r26 g0) (gsd r26 g1) (gsd r27 g0) (gsd r27 g1) (gsd r28 g0) (gsd r28 g1) (gsd r29 g0) (gsd r29 g1) (gsd r30 g0) (gsd r30 g1) (gsd r31 g0) (gsd r31 g1) (gsd r32 g0) (gsd r32 g1) (gsd r33 g0) (gsd r33 g1) (gsd r34 g0) (gsd r34 g1) (gsd r35 g0) (gsd r35 g1) (gsd r36 g0) (gsd r36 g1) (gsd r37 g0) (gsd r37 g1) (gsd r38 g0) (gsd r38 g1) (gsd r39 g0) (gsd r39 g1) (gsd r40 g0) (gsd r40 g1) (gsd r41 g0) (gsd r41 g1) (gsd r42 g0) (gsd r42 g1) (gsd r43 g0) (gsd r43 g1) (gsd r44 g0) (gsd r44 g1)
                    (ysd r0 y0) (ysd r0 y1) (ysd r1 y0) (ysd r1 y1) (ysd r2 y0) (ysd r2 y1) (ysd r3 y0) (ysd r3 y1) (ysd r4 y0) (ysd r4 y1) (ysd r5 y0) (ysd r5 y1) (ysd r6 y0) (ysd r6 y1) (ysd r7 y0) (ysd r7 y1) (ysd r8 y0) (ysd r8 y1) (ysd r9 y0) (ysd r9 y1) (ysd r10 y0) (ysd r10 y1) (ysd r11 y0) (ysd r11 y1) (ysd r12 y0) (ysd r12 y1) (ysd r13 y0) (ysd r13 y1) (ysd r14 y0) (ysd r14 y1) (ysd r15 y0) (ysd r15 y1) (ysd r16 y0) (ysd r16 y1) (ysd r17 y0) (ysd r17 y1) (ysd r18 y0) (ysd r18 y1) (ysd r19 y0) (ysd r19 y1) (ysd r20 y0) (ysd r20 y1) (ysd r21 y0) (ysd r21 y1) (ysd r22 y0) (ysd r22 y1) (ysd r23 y0) (ysd r23 y1) (ysd r24 y0) (ysd r24 y1) (ysd r25 y0) (ysd r25 y1) (ysd r26 y0) (ysd r26 y1) (ysd r27 y0) (ysd r27 y1) (ysd r28 y0) (ysd r28 y1) (ysd r29 y0) (ysd r29 y1) (ysd r30 y0) (ysd r30 y1) (ysd r31 y0) (ysd r31 y1) (ysd r32 y0) (ysd r32 y1) (ysd r33 y0) (ysd r33 y1) (ysd r34 y0) (ysd r34 y1) (ysd r35 y0) (ysd r35 y1) (ysd r36 y0) (ysd r36 y1) (ysd r37 y0) (ysd r37 y1) (ysd r38 y0) (ysd r38 y1) (ysd r39 y0) (ysd r39 y1) (ysd r40 y0) (ysd r40 y1) (ysd r41 y0) (ysd r41 y1) (ysd r42 y0) (ysd r42 y1) (ysd r43 y0) (ysd r43 y1) (ysd r44 y0) (ysd r44 y1) (ysd r45 y0) (ysd r45 y1) (ysd r46 y0) (ysd r46 y1) (ysd r47 y0) (ysd r47 y1) (ysd r48 y0) (ysd r48 y1) (ysd r49 y0) (ysd r49 y1) (ysd r50 y0) (ysd r50 y1) (ysd r51 y0) (ysd r51 y1) (ysd r52 y0) (ysd r52 y1) (ysd r53 y0) (ysd r53 y1) (ysd r54 y0) (ysd r54 y1) (ysd r55 y0) (ysd r55 y1) (ysd r56 y0) (ysd r56 y1) (ysd r57 y0) (ysd r57 y1) (ysd r58 y0) (ysd r58 y1) (ysd r59 y0) (ysd r59 y1) (ysd r60 y0) (ysd r60 y1) (ysd r61 y0) (ysd r61 y1) (ysd r62 y0) (ysd r62 y1) (ysd r63 y0) (ysd r63 y1) (ysd r64 y0) (ysd r64 y1) (ysd r65 y0) (ysd r65 y1) (ysd r66 y0) (ysd r66 y1) (ysd r67 y0) (ysd r67 y1) (ysd r68 y0) (ysd r68 y1) (ysd r69 y0) (ysd r69 y1) (ysd r70 y0) (ysd r70 y1) (ysd r71 y0) (ysd r71 y1) (ysd r72 y0) (ysd r72 y1) (ysd r73 y0) (ysd r73 y1) (ysd r74 y0) (ysd r74 y1) (ysd r75 y0) (ysd r75 y1) (ysd r76 y0) (ysd r76 y1) (ysd r77 y0) (ysd r77 y1) (ysd r78 y0) (ysd r78 y1) (ysd r79 y0) (ysd r79 y1) (ysd r80 y0) (ysd r80 y1) (ysd r81 y0) (ysd r81 y1) (ysd r82 y0) (ysd r82 y1) (ysd r83 y0) (ysd r83 y1) (ysd r84 y0) (ysd r84 y1) (ysd r85 y0) (ysd r85 y1) (ysd r86 y0) (ysd r86 y1) (ysd r87 y0) (ysd r87 y1) (ysd r88 y0) (ysd r88 y1)
                    (= (hg r0) 2)
                    (= (hy r88) 2)
                )
            )
        )