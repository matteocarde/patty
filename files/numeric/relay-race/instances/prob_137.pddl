
        (define (problem prob137)
            (:domain relay-race)
            (:objects
              r0 r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 r11 r12 r13 r14 r15 r16 r17 r18 r19 r20 r21 r22 r23 r24 r25 r26 r27 r28 r29 r30 r31 r32 r33 r34 r35 r36 r37 r38 r39 r40 r41 r42 r43 r44 r45 r46 r47 r48 r49 r50 r51 r52 r53 r54 r55 r56 r57 r58 r59 r60 r61 r62 r63 r64 r65 r66 r67 r68 r69 r70 r71 r72 r73 r74 r75 r76 r77 r78 r79 r80 r81 r82 r83 r84 r85 r86 r87 r88 r89 r90 r91 r92 r93 r94 r95 r96 r97 r98 r99 r100 r101 r102 r103 r104 r105 r106 r107 r108 r109 r110 r111 r112 r113 r114 r115 r116 r117 r118 r119 r120 r121 r122 r123 r124 r125 r126 r127 r128 r129 r130 r131 r132 r133 r134 r135 r136 - runner
              P0 P1 P2 Q0 Q1 Q2 - baton
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4) (= (i r5) 5) (= (i r6) 6) (= (i r7) 7) (= (i r8) 8) (= (i r9) 9) (= (i r10) 10) (= (i r11) 11) (= (i r12) 12) (= (i r13) 13) (= (i r14) 14) (= (i r15) 15) (= (i r16) 16) (= (i r17) 17) (= (i r18) 18) (= (i r19) 19) (= (i r20) 20) (= (i r21) 21) (= (i r22) 22) (= (i r23) 23) (= (i r24) 24) (= (i r25) 25) (= (i r26) 26) (= (i r27) 27) (= (i r28) 28) (= (i r29) 29) (= (i r30) 30) (= (i r31) 31) (= (i r32) 32) (= (i r33) 33) (= (i r34) 34) (= (i r35) 35) (= (i r36) 36) (= (i r37) 37) (= (i r38) 38) (= (i r39) 39) (= (i r40) 40) (= (i r41) 41) (= (i r42) 42) (= (i r43) 43) (= (i r44) 44) (= (i r45) 45) (= (i r46) 46) (= (i r47) 47) (= (i r48) 48) (= (i r49) 49) (= (i r50) 50) (= (i r51) 51) (= (i r52) 52) (= (i r53) 53) (= (i r54) 54) (= (i r55) 55) (= (i r56) 56) (= (i r57) 57) (= (i r58) 58) (= (i r59) 59) (= (i r60) 60) (= (i r61) 61) (= (i r62) 62) (= (i r63) 63) (= (i r64) 64) (= (i r65) 65) (= (i r66) 66) (= (i r67) 67) (= (i r68) 68) (= (i r69) 69) (= (i r70) 70) (= (i r71) 71) (= (i r72) 72) (= (i r73) 73) (= (i r74) 74) (= (i r75) 75) (= (i r76) 76) (= (i r77) 77) (= (i r78) 78) (= (i r79) 79) (= (i r80) 80) (= (i r81) 81) (= (i r82) 82) (= (i r83) 83) (= (i r84) 84) (= (i r85) 85) (= (i r86) 86) (= (i r87) 87) (= (i r88) 88) (= (i r89) 89) (= (i r90) 90) (= (i r91) 91) (= (i r92) 92) (= (i r93) 93) (= (i r94) 94) (= (i r95) 95) (= (i r96) 96) (= (i r97) 97) (= (i r98) 98) (= (i r99) 99) (= (i r100) 100) (= (i r101) 101) (= (i r102) 102) (= (i r103) 103) (= (i r104) 104) (= (i r105) 105) (= (i r106) 106) (= (i r107) 107) (= (i r108) 108) (= (i r109) 109) (= (i r110) 110) (= (i r111) 111) (= (i r112) 112) (= (i r113) 113) (= (i r114) 114) (= (i r115) 115) (= (i r116) 116) (= (i r117) 117) (= (i r118) 118) (= (i r119) 119) (= (i r120) 120) (= (i r121) 121) (= (i r122) 122) (= (i r123) 123) (= (i r124) 124) (= (i r125) 125) (= (i r126) 126) (= (i r127) 127) (= (i r128) 128) (= (i r129) 129) (= (i r130) 130) (= (i r131) 131) (= (i r132) 132) (= (i r133) 133) (= (i r134) 134) (= (i r135) 135) (= (i r136) 136)
                (next r0 r1) (next r1 r2) (next r2 r3) (next r3 r4) (next r4 r5) (next r5 r6) (next r6 r7) (next r7 r8) (next r8 r9) (next r9 r10) (next r10 r11) (next r11 r12) (next r12 r13) (next r13 r14) (next r14 r15) (next r15 r16) (next r16 r17) (next r17 r18) (next r18 r19) (next r19 r20) (next r20 r21) (next r21 r22) (next r22 r23) (next r23 r24) (next r24 r25) (next r25 r26) (next r26 r27) (next r27 r28) (next r28 r29) (next r29 r30) (next r30 r31) (next r31 r32) (next r32 r33) (next r33 r34) (next r34 r35) (next r35 r36) (next r36 r37) (next r37 r38) (next r38 r39) (next r39 r40) (next r40 r41) (next r41 r42) (next r42 r43) (next r43 r44) (next r44 r45) (next r45 r46) (next r46 r47) (next r47 r48) (next r48 r49) (next r49 r50) (next r50 r51) (next r51 r52) (next r52 r53) (next r53 r54) (next r54 r55) (next r55 r56) (next r56 r57) (next r57 r58) (next r58 r59) (next r59 r60) (next r60 r61) (next r61 r62) (next r62 r63) (next r63 r64) (next r64 r65) (next r65 r66) (next r66 r67) (next r67 r68) (next r68 r69) (next r69 r70) (next r70 r71) (next r71 r72) (next r72 r73) (next r73 r74) (next r74 r75) (next r75 r76) (next r76 r77) (next r77 r78) (next r78 r79) (next r79 r80) (next r80 r81) (next r81 r82) (next r82 r83) (next r83 r84) (next r84 r85) (next r85 r86) (next r86 r87) (next r87 r88) (next r88 r89) (next r89 r90) (next r90 r91) (next r91 r92) (next r92 r93) (next r93 r94) (next r94 r95) (next r95 r96) (next r96 r97) (next r97 r98) (next r98 r99) (next r99 r100) (next r100 r101) (next r101 r102) (next r102 r103) (next r103 r104) (next r104 r105) (next r105 r106) (next r106 r107) (next r107 r108) (next r108 r109) (next r109 r110) (next r110 r111) (next r111 r112) (next r112 r113) (next r113 r114) (next r114 r115) (next r115 r116) (next r116 r117) (next r117 r118) (next r118 r119) (next r119 r120) (next r120 r121) (next r121 r122) (next r122 r123) (next r123 r124) (next r124 r125) (next r125 r126) (next r126 r127) (next r127 r128) (next r128 r129) (next r129 r130) (next r130 r131) (next r131 r132) (next r132 r133) (next r133 r134) (next r134 r135) (next r135 r136)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80) (= (x r5) 100) (= (x r6) 120) (= (x r7) 140) (= (x r8) 160) (= (x r9) 180) (= (x r10) 200) (= (x r11) 220) (= (x r12) 240) (= (x r13) 260) (= (x r14) 280) (= (x r15) 300) (= (x r16) 320) (= (x r17) 340) (= (x r18) 360) (= (x r19) 380) (= (x r20) 400) (= (x r21) 420) (= (x r22) 440) (= (x r23) 460) (= (x r24) 480) (= (x r25) 500) (= (x r26) 520) (= (x r27) 540) (= (x r28) 560) (= (x r29) 580) (= (x r30) 600) (= (x r31) 620) (= (x r32) 640) (= (x r33) 660) (= (x r34) 680) (= (x r35) 700) (= (x r36) 720) (= (x r37) 740) (= (x r38) 760) (= (x r39) 780) (= (x r40) 800) (= (x r41) 820) (= (x r42) 840) (= (x r43) 860) (= (x r44) 880) (= (x r45) 900) (= (x r46) 920) (= (x r47) 940) (= (x r48) 960) (= (x r49) 980) (= (x r50) 1000) (= (x r51) 1020) (= (x r52) 1040) (= (x r53) 1060) (= (x r54) 1080) (= (x r55) 1100) (= (x r56) 1120) (= (x r57) 1140) (= (x r58) 1160) (= (x r59) 1180) (= (x r60) 1200) (= (x r61) 1220) (= (x r62) 1240) (= (x r63) 1260) (= (x r64) 1280) (= (x r65) 1300) (= (x r66) 1320) (= (x r67) 1340) (= (x r68) 1360) (= (x r69) 1380) (= (x r70) 1400) (= (x r71) 1420) (= (x r72) 1440) (= (x r73) 1460) (= (x r74) 1480) (= (x r75) 1500) (= (x r76) 1520) (= (x r77) 1540) (= (x r78) 1560) (= (x r79) 1580) (= (x r80) 1600) (= (x r81) 1620) (= (x r82) 1640) (= (x r83) 1660) (= (x r84) 1680) (= (x r85) 1700) (= (x r86) 1720) (= (x r87) 1740) (= (x r88) 1760) (= (x r89) 1780) (= (x r90) 1800) (= (x r91) 1820) (= (x r92) 1840) (= (x r93) 1860) (= (x r94) 1880) (= (x r95) 1900) (= (x r96) 1920) (= (x r97) 1940) (= (x r98) 1960) (= (x r99) 1980) (= (x r100) 2000) (= (x r101) 2020) (= (x r102) 2040) (= (x r103) 2060) (= (x r104) 2080) (= (x r105) 2100) (= (x r106) 2120) (= (x r107) 2140) (= (x r108) 2160) (= (x r109) 2180) (= (x r110) 2200) (= (x r111) 2220) (= (x r112) 2240) (= (x r113) 2260) (= (x r114) 2280) (= (x r115) 2300) (= (x r116) 2320) (= (x r117) 2340) (= (x r118) 2360) (= (x r119) 2380) (= (x r120) 2400) (= (x r121) 2420) (= (x r122) 2440) (= (x r123) 2460) (= (x r124) 2480) (= (x r125) 2500) (= (x r126) 2520) (= (x r127) 2540) (= (x r128) 2560) (= (x r129) 2580) (= (x r130) 2600) (= (x r131) 2620) (= (x r132) 2640) (= (x r133) 2660) (= (x r134) 2680) (= (x r135) 2700) (= (x r136) 2720)
                
                (= (b r0 P0) 1) (= (b r0 P1) 1) (= (b r0 P2) 1) (= (b r1 P0) 0) (= (b r1 P1) 0) (= (b r1 P2) 0) (= (b r2 P0) 0) (= (b r2 P1) 0) (= (b r2 P2) 0) (= (b r3 P0) 0) (= (b r3 P1) 0) (= (b r3 P2) 0) (= (b r4 P0) 0) (= (b r4 P1) 0) (= (b r4 P2) 0) (= (b r5 P0) 0) (= (b r5 P1) 0) (= (b r5 P2) 0) (= (b r6 P0) 0) (= (b r6 P1) 0) (= (b r6 P2) 0) (= (b r7 P0) 0) (= (b r7 P1) 0) (= (b r7 P2) 0) (= (b r8 P0) 0) (= (b r8 P1) 0) (= (b r8 P2) 0) (= (b r9 P0) 0) (= (b r9 P1) 0) (= (b r9 P2) 0) (= (b r10 P0) 0) (= (b r10 P1) 0) (= (b r10 P2) 0) (= (b r11 P0) 0) (= (b r11 P1) 0) (= (b r11 P2) 0) (= (b r12 P0) 0) (= (b r12 P1) 0) (= (b r12 P2) 0) (= (b r13 P0) 0) (= (b r13 P1) 0) (= (b r13 P2) 0) (= (b r14 P0) 0) (= (b r14 P1) 0) (= (b r14 P2) 0) (= (b r15 P0) 0) (= (b r15 P1) 0) (= (b r15 P2) 0) (= (b r16 P0) 0) (= (b r16 P1) 0) (= (b r16 P2) 0) (= (b r17 P0) 0) (= (b r17 P1) 0) (= (b r17 P2) 0) (= (b r18 P0) 0) (= (b r18 P1) 0) (= (b r18 P2) 0) (= (b r19 P0) 0) (= (b r19 P1) 0) (= (b r19 P2) 0) (= (b r20 P0) 0) (= (b r20 P1) 0) (= (b r20 P2) 0) (= (b r21 P0) 0) (= (b r21 P1) 0) (= (b r21 P2) 0) (= (b r22 P0) 0) (= (b r22 P1) 0) (= (b r22 P2) 0) (= (b r23 P0) 0) (= (b r23 P1) 0) (= (b r23 P2) 0) (= (b r24 P0) 0) (= (b r24 P1) 0) (= (b r24 P2) 0) (= (b r25 P0) 0) (= (b r25 P1) 0) (= (b r25 P2) 0) (= (b r26 P0) 0) (= (b r26 P1) 0) (= (b r26 P2) 0) (= (b r27 P0) 0) (= (b r27 P1) 0) (= (b r27 P2) 0) (= (b r28 P0) 0) (= (b r28 P1) 0) (= (b r28 P2) 0) (= (b r29 P0) 0) (= (b r29 P1) 0) (= (b r29 P2) 0) (= (b r30 P0) 0) (= (b r30 P1) 0) (= (b r30 P2) 0) (= (b r31 P0) 0) (= (b r31 P1) 0) (= (b r31 P2) 0) (= (b r32 P0) 0) (= (b r32 P1) 0) (= (b r32 P2) 0) (= (b r33 P0) 0) (= (b r33 P1) 0) (= (b r33 P2) 0) (= (b r34 P0) 0) (= (b r34 P1) 0) (= (b r34 P2) 0) (= (b r35 P0) 0) (= (b r35 P1) 0) (= (b r35 P2) 0) (= (b r36 P0) 0) (= (b r36 P1) 0) (= (b r36 P2) 0) (= (b r37 P0) 0) (= (b r37 P1) 0) (= (b r37 P2) 0) (= (b r38 P0) 0) (= (b r38 P1) 0) (= (b r38 P2) 0) (= (b r39 P0) 0) (= (b r39 P1) 0) (= (b r39 P2) 0) (= (b r40 P0) 0) (= (b r40 P1) 0) (= (b r40 P2) 0) (= (b r41 P0) 0) (= (b r41 P1) 0) (= (b r41 P2) 0) (= (b r42 P0) 0) (= (b r42 P1) 0) (= (b r42 P2) 0) (= (b r43 P0) 0) (= (b r43 P1) 0) (= (b r43 P2) 0) (= (b r44 P0) 0) (= (b r44 P1) 0) (= (b r44 P2) 0) (= (b r45 P0) 0) (= (b r45 P1) 0) (= (b r45 P2) 0) (= (b r46 P0) 0) (= (b r46 P1) 0) (= (b r46 P2) 0) (= (b r47 P0) 0) (= (b r47 P1) 0) (= (b r47 P2) 0) (= (b r48 P0) 0) (= (b r48 P1) 0) (= (b r48 P2) 0) (= (b r49 P0) 0) (= (b r49 P1) 0) (= (b r49 P2) 0) (= (b r50 P0) 0) (= (b r50 P1) 0) (= (b r50 P2) 0) (= (b r51 P0) 0) (= (b r51 P1) 0) (= (b r51 P2) 0) (= (b r52 P0) 0) (= (b r52 P1) 0) (= (b r52 P2) 0) (= (b r53 P0) 0) (= (b r53 P1) 0) (= (b r53 P2) 0) (= (b r54 P0) 0) (= (b r54 P1) 0) (= (b r54 P2) 0) (= (b r55 P0) 0) (= (b r55 P1) 0) (= (b r55 P2) 0) (= (b r56 P0) 0) (= (b r56 P1) 0) (= (b r56 P2) 0) (= (b r57 P0) 0) (= (b r57 P1) 0) (= (b r57 P2) 0) (= (b r58 P0) 0) (= (b r58 P1) 0) (= (b r58 P2) 0) (= (b r59 P0) 0) (= (b r59 P1) 0) (= (b r59 P2) 0) (= (b r60 P0) 0) (= (b r60 P1) 0) (= (b r60 P2) 0) (= (b r61 P0) 0) (= (b r61 P1) 0) (= (b r61 P2) 0) (= (b r62 P0) 0) (= (b r62 P1) 0) (= (b r62 P2) 0) (= (b r63 P0) 0) (= (b r63 P1) 0) (= (b r63 P2) 0) (= (b r64 P0) 0) (= (b r64 P1) 0) (= (b r64 P2) 0) (= (b r65 P0) 0) (= (b r65 P1) 0) (= (b r65 P2) 0) (= (b r66 P0) 0) (= (b r66 P1) 0) (= (b r66 P2) 0) (= (b r67 P0) 0) (= (b r67 P1) 0) (= (b r67 P2) 0) (= (b r68 P0) 0) (= (b r68 P1) 0) (= (b r68 P2) 0) (= (b r69 P0) 0) (= (b r69 P1) 0) (= (b r69 P2) 0) (= (b r70 P0) 0) (= (b r70 P1) 0) (= (b r70 P2) 0) (= (b r71 P0) 0) (= (b r71 P1) 0) (= (b r71 P2) 0) (= (b r72 P0) 0) (= (b r72 P1) 0) (= (b r72 P2) 0) (= (b r73 P0) 0) (= (b r73 P1) 0) (= (b r73 P2) 0) (= (b r74 P0) 0) (= (b r74 P1) 0) (= (b r74 P2) 0) (= (b r75 P0) 0) (= (b r75 P1) 0) (= (b r75 P2) 0) (= (b r76 P0) 0) (= (b r76 P1) 0) (= (b r76 P2) 0) (= (b r77 P0) 0) (= (b r77 P1) 0) (= (b r77 P2) 0) (= (b r78 P0) 0) (= (b r78 P1) 0) (= (b r78 P2) 0) (= (b r79 P0) 0) (= (b r79 P1) 0) (= (b r79 P2) 0) (= (b r80 P0) 0) (= (b r80 P1) 0) (= (b r80 P2) 0) (= (b r81 P0) 0) (= (b r81 P1) 0) (= (b r81 P2) 0) (= (b r82 P0) 0) (= (b r82 P1) 0) (= (b r82 P2) 0) (= (b r83 P0) 0) (= (b r83 P1) 0) (= (b r83 P2) 0) (= (b r84 P0) 0) (= (b r84 P1) 0) (= (b r84 P2) 0) (= (b r85 P0) 0) (= (b r85 P1) 0) (= (b r85 P2) 0) (= (b r86 P0) 0) (= (b r86 P1) 0) (= (b r86 P2) 0) (= (b r87 P0) 0) (= (b r87 P1) 0) (= (b r87 P2) 0) (= (b r88 P0) 0) (= (b r88 P1) 0) (= (b r88 P2) 0) (= (b r89 P0) 0) (= (b r89 P1) 0) (= (b r89 P2) 0) (= (b r90 P0) 0) (= (b r90 P1) 0) (= (b r90 P2) 0) (= (b r91 P0) 0) (= (b r91 P1) 0) (= (b r91 P2) 0) (= (b r92 P0) 0) (= (b r92 P1) 0) (= (b r92 P2) 0) (= (b r93 P0) 0) (= (b r93 P1) 0) (= (b r93 P2) 0) (= (b r94 P0) 0) (= (b r94 P1) 0) (= (b r94 P2) 0) (= (b r95 P0) 0) (= (b r95 P1) 0) (= (b r95 P2) 0) (= (b r96 P0) 0) (= (b r96 P1) 0) (= (b r96 P2) 0) (= (b r97 P0) 0) (= (b r97 P1) 0) (= (b r97 P2) 0) (= (b r98 P0) 0) (= (b r98 P1) 0) (= (b r98 P2) 0) (= (b r99 P0) 0) (= (b r99 P1) 0) (= (b r99 P2) 0) (= (b r100 P0) 0) (= (b r100 P1) 0) (= (b r100 P2) 0) (= (b r101 P0) 0) (= (b r101 P1) 0) (= (b r101 P2) 0) (= (b r102 P0) 0) (= (b r102 P1) 0) (= (b r102 P2) 0) (= (b r103 P0) 0) (= (b r103 P1) 0) (= (b r103 P2) 0) (= (b r104 P0) 0) (= (b r104 P1) 0) (= (b r104 P2) 0) (= (b r105 P0) 0) (= (b r105 P1) 0) (= (b r105 P2) 0) (= (b r106 P0) 0) (= (b r106 P1) 0) (= (b r106 P2) 0) (= (b r107 P0) 0) (= (b r107 P1) 0) (= (b r107 P2) 0) (= (b r108 P0) 0) (= (b r108 P1) 0) (= (b r108 P2) 0) (= (b r109 P0) 0) (= (b r109 P1) 0) (= (b r109 P2) 0) (= (b r110 P0) 0) (= (b r110 P1) 0) (= (b r110 P2) 0) (= (b r111 P0) 0) (= (b r111 P1) 0) (= (b r111 P2) 0) (= (b r112 P0) 0) (= (b r112 P1) 0) (= (b r112 P2) 0) (= (b r113 P0) 0) (= (b r113 P1) 0) (= (b r113 P2) 0) (= (b r114 P0) 0) (= (b r114 P1) 0) (= (b r114 P2) 0) (= (b r115 P0) 0) (= (b r115 P1) 0) (= (b r115 P2) 0) (= (b r116 P0) 0) (= (b r116 P1) 0) (= (b r116 P2) 0) (= (b r117 P0) 0) (= (b r117 P1) 0) (= (b r117 P2) 0) (= (b r118 P0) 0) (= (b r118 P1) 0) (= (b r118 P2) 0) (= (b r119 P0) 0) (= (b r119 P1) 0) (= (b r119 P2) 0) (= (b r120 P0) 0) (= (b r120 P1) 0) (= (b r120 P2) 0) (= (b r121 P0) 0) (= (b r121 P1) 0) (= (b r121 P2) 0) (= (b r122 P0) 0) (= (b r122 P1) 0) (= (b r122 P2) 0) (= (b r123 P0) 0) (= (b r123 P1) 0) (= (b r123 P2) 0) (= (b r124 P0) 0) (= (b r124 P1) 0) (= (b r124 P2) 0) (= (b r125 P0) 0) (= (b r125 P1) 0) (= (b r125 P2) 0) (= (b r126 P0) 0) (= (b r126 P1) 0) (= (b r126 P2) 0) (= (b r127 P0) 0) (= (b r127 P1) 0) (= (b r127 P2) 0) (= (b r128 P0) 0) (= (b r128 P1) 0) (= (b r128 P2) 0) (= (b r129 P0) 0) (= (b r129 P1) 0) (= (b r129 P2) 0) (= (b r130 P0) 0) (= (b r130 P1) 0) (= (b r130 P2) 0) (= (b r131 P0) 0) (= (b r131 P1) 0) (= (b r131 P2) 0) (= (b r132 P0) 0) (= (b r132 P1) 0) (= (b r132 P2) 0) (= (b r133 P0) 0) (= (b r133 P1) 0) (= (b r133 P2) 0) (= (b r134 P0) 0) (= (b r134 P1) 0) (= (b r134 P2) 0) (= (b r135 P0) 0) (= (b r135 P1) 0) (= (b r135 P2) 0) (= (b r136 P0) 0) (= (b r136 P1) 0) (= (b r136 P2) 0)
                (= (b r0 Q0) 1) (= (b r0 Q1) 1) (= (b r0 Q2) 1) (= (b r1 Q0) 0) (= (b r1 Q1) 0) (= (b r1 Q2) 0) (= (b r2 Q0) 0) (= (b r2 Q1) 0) (= (b r2 Q2) 0) (= (b r3 Q0) 0) (= (b r3 Q1) 0) (= (b r3 Q2) 0) (= (b r4 Q0) 0) (= (b r4 Q1) 0) (= (b r4 Q2) 0) (= (b r5 Q0) 0) (= (b r5 Q1) 0) (= (b r5 Q2) 0) (= (b r6 Q0) 0) (= (b r6 Q1) 0) (= (b r6 Q2) 0) (= (b r7 Q0) 0) (= (b r7 Q1) 0) (= (b r7 Q2) 0) (= (b r8 Q0) 0) (= (b r8 Q1) 0) (= (b r8 Q2) 0) (= (b r9 Q0) 0) (= (b r9 Q1) 0) (= (b r9 Q2) 0) (= (b r10 Q0) 0) (= (b r10 Q1) 0) (= (b r10 Q2) 0) (= (b r11 Q0) 0) (= (b r11 Q1) 0) (= (b r11 Q2) 0) (= (b r12 Q0) 0) (= (b r12 Q1) 0) (= (b r12 Q2) 0) (= (b r13 Q0) 0) (= (b r13 Q1) 0) (= (b r13 Q2) 0) (= (b r14 Q0) 0) (= (b r14 Q1) 0) (= (b r14 Q2) 0) (= (b r15 Q0) 0) (= (b r15 Q1) 0) (= (b r15 Q2) 0) (= (b r16 Q0) 0) (= (b r16 Q1) 0) (= (b r16 Q2) 0) (= (b r17 Q0) 0) (= (b r17 Q1) 0) (= (b r17 Q2) 0) (= (b r18 Q0) 0) (= (b r18 Q1) 0) (= (b r18 Q2) 0) (= (b r19 Q0) 0) (= (b r19 Q1) 0) (= (b r19 Q2) 0) (= (b r20 Q0) 0) (= (b r20 Q1) 0) (= (b r20 Q2) 0) (= (b r21 Q0) 0) (= (b r21 Q1) 0) (= (b r21 Q2) 0) (= (b r22 Q0) 0) (= (b r22 Q1) 0) (= (b r22 Q2) 0) (= (b r23 Q0) 0) (= (b r23 Q1) 0) (= (b r23 Q2) 0) (= (b r24 Q0) 0) (= (b r24 Q1) 0) (= (b r24 Q2) 0) (= (b r25 Q0) 0) (= (b r25 Q1) 0) (= (b r25 Q2) 0) (= (b r26 Q0) 0) (= (b r26 Q1) 0) (= (b r26 Q2) 0) (= (b r27 Q0) 0) (= (b r27 Q1) 0) (= (b r27 Q2) 0) (= (b r28 Q0) 0) (= (b r28 Q1) 0) (= (b r28 Q2) 0) (= (b r29 Q0) 0) (= (b r29 Q1) 0) (= (b r29 Q2) 0) (= (b r30 Q0) 0) (= (b r30 Q1) 0) (= (b r30 Q2) 0) (= (b r31 Q0) 0) (= (b r31 Q1) 0) (= (b r31 Q2) 0) (= (b r32 Q0) 0) (= (b r32 Q1) 0) (= (b r32 Q2) 0) (= (b r33 Q0) 0) (= (b r33 Q1) 0) (= (b r33 Q2) 0) (= (b r34 Q0) 0) (= (b r34 Q1) 0) (= (b r34 Q2) 0) (= (b r35 Q0) 0) (= (b r35 Q1) 0) (= (b r35 Q2) 0) (= (b r36 Q0) 0) (= (b r36 Q1) 0) (= (b r36 Q2) 0) (= (b r37 Q0) 0) (= (b r37 Q1) 0) (= (b r37 Q2) 0) (= (b r38 Q0) 0) (= (b r38 Q1) 0) (= (b r38 Q2) 0) (= (b r39 Q0) 0) (= (b r39 Q1) 0) (= (b r39 Q2) 0) (= (b r40 Q0) 0) (= (b r40 Q1) 0) (= (b r40 Q2) 0) (= (b r41 Q0) 0) (= (b r41 Q1) 0) (= (b r41 Q2) 0) (= (b r42 Q0) 0) (= (b r42 Q1) 0) (= (b r42 Q2) 0) (= (b r43 Q0) 0) (= (b r43 Q1) 0) (= (b r43 Q2) 0) (= (b r44 Q0) 0) (= (b r44 Q1) 0) (= (b r44 Q2) 0) (= (b r45 Q0) 0) (= (b r45 Q1) 0) (= (b r45 Q2) 0) (= (b r46 Q0) 0) (= (b r46 Q1) 0) (= (b r46 Q2) 0) (= (b r47 Q0) 0) (= (b r47 Q1) 0) (= (b r47 Q2) 0) (= (b r48 Q0) 0) (= (b r48 Q1) 0) (= (b r48 Q2) 0) (= (b r49 Q0) 0) (= (b r49 Q1) 0) (= (b r49 Q2) 0) (= (b r50 Q0) 0) (= (b r50 Q1) 0) (= (b r50 Q2) 0) (= (b r51 Q0) 0) (= (b r51 Q1) 0) (= (b r51 Q2) 0) (= (b r52 Q0) 0) (= (b r52 Q1) 0) (= (b r52 Q2) 0) (= (b r53 Q0) 0) (= (b r53 Q1) 0) (= (b r53 Q2) 0) (= (b r54 Q0) 0) (= (b r54 Q1) 0) (= (b r54 Q2) 0) (= (b r55 Q0) 0) (= (b r55 Q1) 0) (= (b r55 Q2) 0) (= (b r56 Q0) 0) (= (b r56 Q1) 0) (= (b r56 Q2) 0) (= (b r57 Q0) 0) (= (b r57 Q1) 0) (= (b r57 Q2) 0) (= (b r58 Q0) 0) (= (b r58 Q1) 0) (= (b r58 Q2) 0) (= (b r59 Q0) 0) (= (b r59 Q1) 0) (= (b r59 Q2) 0) (= (b r60 Q0) 0) (= (b r60 Q1) 0) (= (b r60 Q2) 0) (= (b r61 Q0) 0) (= (b r61 Q1) 0) (= (b r61 Q2) 0) (= (b r62 Q0) 0) (= (b r62 Q1) 0) (= (b r62 Q2) 0) (= (b r63 Q0) 0) (= (b r63 Q1) 0) (= (b r63 Q2) 0) (= (b r64 Q0) 0) (= (b r64 Q1) 0) (= (b r64 Q2) 0) (= (b r65 Q0) 0) (= (b r65 Q1) 0) (= (b r65 Q2) 0) (= (b r66 Q0) 0) (= (b r66 Q1) 0) (= (b r66 Q2) 0) (= (b r67 Q0) 0) (= (b r67 Q1) 0) (= (b r67 Q2) 0) (= (b r68 Q0) 0) (= (b r68 Q1) 0) (= (b r68 Q2) 0) (= (b r69 Q0) 0) (= (b r69 Q1) 0) (= (b r69 Q2) 0) (= (b r70 Q0) 0) (= (b r70 Q1) 0) (= (b r70 Q2) 0) (= (b r71 Q0) 0) (= (b r71 Q1) 0) (= (b r71 Q2) 0) (= (b r72 Q0) 0) (= (b r72 Q1) 0) (= (b r72 Q2) 0) (= (b r73 Q0) 0) (= (b r73 Q1) 0) (= (b r73 Q2) 0) (= (b r74 Q0) 0) (= (b r74 Q1) 0) (= (b r74 Q2) 0) (= (b r75 Q0) 0) (= (b r75 Q1) 0) (= (b r75 Q2) 0) (= (b r76 Q0) 0) (= (b r76 Q1) 0) (= (b r76 Q2) 0) (= (b r77 Q0) 0) (= (b r77 Q1) 0) (= (b r77 Q2) 0) (= (b r78 Q0) 0) (= (b r78 Q1) 0) (= (b r78 Q2) 0) (= (b r79 Q0) 0) (= (b r79 Q1) 0) (= (b r79 Q2) 0) (= (b r80 Q0) 0) (= (b r80 Q1) 0) (= (b r80 Q2) 0) (= (b r81 Q0) 0) (= (b r81 Q1) 0) (= (b r81 Q2) 0) (= (b r82 Q0) 0) (= (b r82 Q1) 0) (= (b r82 Q2) 0) (= (b r83 Q0) 0) (= (b r83 Q1) 0) (= (b r83 Q2) 0) (= (b r84 Q0) 0) (= (b r84 Q1) 0) (= (b r84 Q2) 0) (= (b r85 Q0) 0) (= (b r85 Q1) 0) (= (b r85 Q2) 0) (= (b r86 Q0) 0) (= (b r86 Q1) 0) (= (b r86 Q2) 0) (= (b r87 Q0) 0) (= (b r87 Q1) 0) (= (b r87 Q2) 0) (= (b r88 Q0) 0) (= (b r88 Q1) 0) (= (b r88 Q2) 0) (= (b r89 Q0) 0) (= (b r89 Q1) 0) (= (b r89 Q2) 0) (= (b r90 Q0) 0) (= (b r90 Q1) 0) (= (b r90 Q2) 0) (= (b r91 Q0) 0) (= (b r91 Q1) 0) (= (b r91 Q2) 0) (= (b r92 Q0) 0) (= (b r92 Q1) 0) (= (b r92 Q2) 0) (= (b r93 Q0) 0) (= (b r93 Q1) 0) (= (b r93 Q2) 0) (= (b r94 Q0) 0) (= (b r94 Q1) 0) (= (b r94 Q2) 0) (= (b r95 Q0) 0) (= (b r95 Q1) 0) (= (b r95 Q2) 0) (= (b r96 Q0) 0) (= (b r96 Q1) 0) (= (b r96 Q2) 0) (= (b r97 Q0) 0) (= (b r97 Q1) 0) (= (b r97 Q2) 0) (= (b r98 Q0) 0) (= (b r98 Q1) 0) (= (b r98 Q2) 0) (= (b r99 Q0) 0) (= (b r99 Q1) 0) (= (b r99 Q2) 0) (= (b r100 Q0) 0) (= (b r100 Q1) 0) (= (b r100 Q2) 0) (= (b r101 Q0) 0) (= (b r101 Q1) 0) (= (b r101 Q2) 0) (= (b r102 Q0) 0) (= (b r102 Q1) 0) (= (b r102 Q2) 0) (= (b r103 Q0) 0) (= (b r103 Q1) 0) (= (b r103 Q2) 0) (= (b r104 Q0) 0) (= (b r104 Q1) 0) (= (b r104 Q2) 0) (= (b r105 Q0) 0) (= (b r105 Q1) 0) (= (b r105 Q2) 0) (= (b r106 Q0) 0) (= (b r106 Q1) 0) (= (b r106 Q2) 0) (= (b r107 Q0) 0) (= (b r107 Q1) 0) (= (b r107 Q2) 0) (= (b r108 Q0) 0) (= (b r108 Q1) 0) (= (b r108 Q2) 0) (= (b r109 Q0) 0) (= (b r109 Q1) 0) (= (b r109 Q2) 0) (= (b r110 Q0) 0) (= (b r110 Q1) 0) (= (b r110 Q2) 0) (= (b r111 Q0) 0) (= (b r111 Q1) 0) (= (b r111 Q2) 0) (= (b r112 Q0) 0) (= (b r112 Q1) 0) (= (b r112 Q2) 0) (= (b r113 Q0) 0) (= (b r113 Q1) 0) (= (b r113 Q2) 0) (= (b r114 Q0) 0) (= (b r114 Q1) 0) (= (b r114 Q2) 0) (= (b r115 Q0) 0) (= (b r115 Q1) 0) (= (b r115 Q2) 0) (= (b r116 Q0) 0) (= (b r116 Q1) 0) (= (b r116 Q2) 0) (= (b r117 Q0) 0) (= (b r117 Q1) 0) (= (b r117 Q2) 0) (= (b r118 Q0) 0) (= (b r118 Q1) 0) (= (b r118 Q2) 0) (= (b r119 Q0) 0) (= (b r119 Q1) 0) (= (b r119 Q2) 0) (= (b r120 Q0) 0) (= (b r120 Q1) 0) (= (b r120 Q2) 0) (= (b r121 Q0) 0) (= (b r121 Q1) 0) (= (b r121 Q2) 0) (= (b r122 Q0) 0) (= (b r122 Q1) 0) (= (b r122 Q2) 0) (= (b r123 Q0) 0) (= (b r123 Q1) 0) (= (b r123 Q2) 0) (= (b r124 Q0) 0) (= (b r124 Q1) 0) (= (b r124 Q2) 0) (= (b r125 Q0) 0) (= (b r125 Q1) 0) (= (b r125 Q2) 0) (= (b r126 Q0) 0) (= (b r126 Q1) 0) (= (b r126 Q2) 0) (= (b r127 Q0) 0) (= (b r127 Q1) 0) (= (b r127 Q2) 0) (= (b r128 Q0) 0) (= (b r128 Q1) 0) (= (b r128 Q2) 0) (= (b r129 Q0) 0) (= (b r129 Q1) 0) (= (b r129 Q2) 0) (= (b r130 Q0) 0) (= (b r130 Q1) 0) (= (b r130 Q2) 0) (= (b r131 Q0) 0) (= (b r131 Q1) 0) (= (b r131 Q2) 0) (= (b r132 Q0) 0) (= (b r132 Q1) 0) (= (b r132 Q2) 0) (= (b r133 Q0) 0) (= (b r133 Q1) 0) (= (b r133 Q2) 0) (= (b r134 Q0) 0) (= (b r134 Q1) 0) (= (b r134 Q2) 0) (= (b r135 Q0) 0) (= (b r135 Q1) 0) (= (b r135 Q2) 0) (= (b r136 Q0) 0) (= (b r136 Q1) 0) (= (b r136 Q2) 0)
                (= (h r0) 6) (= (h r1) 0) (= (h r2) 0) (= (h r3) 0) (= (h r4) 0) (= (h r5) 0) (= (h r6) 0) (= (h r7) 0) (= (h r8) 0) (= (h r9) 0) (= (h r10) 0) (= (h r11) 0) (= (h r12) 0) (= (h r13) 0) (= (h r14) 0) (= (h r15) 0) (= (h r16) 0) (= (h r17) 0) (= (h r18) 0) (= (h r19) 0) (= (h r20) 0) (= (h r21) 0) (= (h r22) 0) (= (h r23) 0) (= (h r24) 0) (= (h r25) 0) (= (h r26) 0) (= (h r27) 0) (= (h r28) 0) (= (h r29) 0) (= (h r30) 0) (= (h r31) 0) (= (h r32) 0) (= (h r33) 0) (= (h r34) 0) (= (h r35) 0) (= (h r36) 0) (= (h r37) 0) (= (h r38) 0) (= (h r39) 0) (= (h r40) 0) (= (h r41) 0) (= (h r42) 0) (= (h r43) 0) (= (h r44) 0) (= (h r45) 0) (= (h r46) 0) (= (h r47) 0) (= (h r48) 0) (= (h r49) 0) (= (h r50) 0) (= (h r51) 0) (= (h r52) 0) (= (h r53) 0) (= (h r54) 0) (= (h r55) 0) (= (h r56) 0) (= (h r57) 0) (= (h r58) 0) (= (h r59) 0) (= (h r60) 0) (= (h r61) 0) (= (h r62) 0) (= (h r63) 0) (= (h r64) 0) (= (h r65) 0) (= (h r66) 0) (= (h r67) 0) (= (h r68) 0) (= (h r69) 0) (= (h r70) 0) (= (h r71) 0) (= (h r72) 0) (= (h r73) 0) (= (h r74) 0) (= (h r75) 0) (= (h r76) 0) (= (h r77) 0) (= (h r78) 0) (= (h r79) 0) (= (h r80) 0) (= (h r81) 0) (= (h r82) 0) (= (h r83) 0) (= (h r84) 0) (= (h r85) 0) (= (h r86) 0) (= (h r87) 0) (= (h r88) 0) (= (h r89) 0) (= (h r90) 0) (= (h r91) 0) (= (h r92) 0) (= (h r93) 0) (= (h r94) 0) (= (h r95) 0) (= (h r96) 0) (= (h r97) 0) (= (h r98) 0) (= (h r99) 0) (= (h r100) 0) (= (h r101) 0) (= (h r102) 0) (= (h r103) 0) (= (h r104) 0) (= (h r105) 0) (= (h r106) 0) (= (h r107) 0) (= (h r108) 0) (= (h r109) 0) (= (h r110) 0) (= (h r111) 0) (= (h r112) 0) (= (h r113) 0) (= (h r114) 0) (= (h r115) 0) (= (h r116) 0) (= (h r117) 0) (= (h r118) 0) (= (h r119) 0) (= (h r120) 0) (= (h r121) 0) (= (h r122) 0) (= (h r123) 0) (= (h r124) 0) (= (h r125) 0) (= (h r126) 0) (= (h r127) 0) (= (h r128) 0) (= (h r129) 0) (= (h r130) 0) (= (h r131) 0) (= (h r132) 0) (= (h r133) 0) (= (h r134) 0) (= (h r135) 0) (= (h r136) 0)
                
                (td r0 P0) (td r0 P1) (td r0 P2)
                (td r0 Q0) (td r0 Q1) (td r0 Q2)
            )

            (:goal
                (and
                    (td r0 P0) (td r0 P1) (td r0 P2) (td r1 P0) (td r1 P1) (td r1 P2) (td r2 P0) (td r2 P1) (td r2 P2) (td r3 P0) (td r3 P1) (td r3 P2) (td r4 P0) (td r4 P1) (td r4 P2) (td r5 P0) (td r5 P1) (td r5 P2) (td r6 P0) (td r6 P1) (td r6 P2) (td r7 P0) (td r7 P1) (td r7 P2) (td r8 P0) (td r8 P1) (td r8 P2) (td r9 P0) (td r9 P1) (td r9 P2) (td r10 P0) (td r10 P1) (td r10 P2) (td r11 P0) (td r11 P1) (td r11 P2) (td r12 P0) (td r12 P1) (td r12 P2) (td r13 P0) (td r13 P1) (td r13 P2) (td r14 P0) (td r14 P1) (td r14 P2) (td r15 P0) (td r15 P1) (td r15 P2) (td r16 P0) (td r16 P1) (td r16 P2) (td r17 P0) (td r17 P1) (td r17 P2) (td r18 P0) (td r18 P1) (td r18 P2) (td r19 P0) (td r19 P1) (td r19 P2) (td r20 P0) (td r20 P1) (td r20 P2) (td r21 P0) (td r21 P1) (td r21 P2) (td r22 P0) (td r22 P1) (td r22 P2) (td r23 P0) (td r23 P1) (td r23 P2) (td r24 P0) (td r24 P1) (td r24 P2) (td r25 P0) (td r25 P1) (td r25 P2) (td r26 P0) (td r26 P1) (td r26 P2) (td r27 P0) (td r27 P1) (td r27 P2) (td r28 P0) (td r28 P1) (td r28 P2) (td r29 P0) (td r29 P1) (td r29 P2) (td r30 P0) (td r30 P1) (td r30 P2) (td r31 P0) (td r31 P1) (td r31 P2) (td r32 P0) (td r32 P1) (td r32 P2) (td r33 P0) (td r33 P1) (td r33 P2) (td r34 P0) (td r34 P1) (td r34 P2) (td r35 P0) (td r35 P1) (td r35 P2) (td r36 P0) (td r36 P1) (td r36 P2) (td r37 P0) (td r37 P1) (td r37 P2) (td r38 P0) (td r38 P1) (td r38 P2) (td r39 P0) (td r39 P1) (td r39 P2) (td r40 P0) (td r40 P1) (td r40 P2) (td r41 P0) (td r41 P1) (td r41 P2) (td r42 P0) (td r42 P1) (td r42 P2) (td r43 P0) (td r43 P1) (td r43 P2) (td r44 P0) (td r44 P1) (td r44 P2) (td r45 P0) (td r45 P1) (td r45 P2) (td r46 P0) (td r46 P1) (td r46 P2) (td r47 P0) (td r47 P1) (td r47 P2) (td r48 P0) (td r48 P1) (td r48 P2) (td r49 P0) (td r49 P1) (td r49 P2) (td r50 P0) (td r50 P1) (td r50 P2) (td r51 P0) (td r51 P1) (td r51 P2) (td r52 P0) (td r52 P1) (td r52 P2) (td r53 P0) (td r53 P1) (td r53 P2) (td r54 P0) (td r54 P1) (td r54 P2) (td r55 P0) (td r55 P1) (td r55 P2) (td r56 P0) (td r56 P1) (td r56 P2) (td r57 P0) (td r57 P1) (td r57 P2) (td r58 P0) (td r58 P1) (td r58 P2) (td r59 P0) (td r59 P1) (td r59 P2) (td r60 P0) (td r60 P1) (td r60 P2) (td r61 P0) (td r61 P1) (td r61 P2) (td r62 P0) (td r62 P1) (td r62 P2) (td r63 P0) (td r63 P1) (td r63 P2) (td r64 P0) (td r64 P1) (td r64 P2) (td r65 P0) (td r65 P1) (td r65 P2) (td r66 P0) (td r66 P1) (td r66 P2) (td r67 P0) (td r67 P1) (td r67 P2) (td r68 P0) (td r68 P1) (td r68 P2)
                    (not (td r69 P0)) (not (td r69 P1)) (not (td r69 P2)) (not (td r70 P0)) (not (td r70 P1)) (not (td r70 P2)) (not (td r71 P0)) (not (td r71 P1)) (not (td r71 P2)) (not (td r72 P0)) (not (td r72 P1)) (not (td r72 P2)) (not (td r73 P0)) (not (td r73 P1)) (not (td r73 P2)) (not (td r74 P0)) (not (td r74 P1)) (not (td r74 P2)) (not (td r75 P0)) (not (td r75 P1)) (not (td r75 P2)) (not (td r76 P0)) (not (td r76 P1)) (not (td r76 P2)) (not (td r77 P0)) (not (td r77 P1)) (not (td r77 P2)) (not (td r78 P0)) (not (td r78 P1)) (not (td r78 P2)) (not (td r79 P0)) (not (td r79 P1)) (not (td r79 P2)) (not (td r80 P0)) (not (td r80 P1)) (not (td r80 P2)) (not (td r81 P0)) (not (td r81 P1)) (not (td r81 P2)) (not (td r82 P0)) (not (td r82 P1)) (not (td r82 P2)) (not (td r83 P0)) (not (td r83 P1)) (not (td r83 P2)) (not (td r84 P0)) (not (td r84 P1)) (not (td r84 P2)) (not (td r85 P0)) (not (td r85 P1)) (not (td r85 P2)) (not (td r86 P0)) (not (td r86 P1)) (not (td r86 P2)) (not (td r87 P0)) (not (td r87 P1)) (not (td r87 P2)) (not (td r88 P0)) (not (td r88 P1)) (not (td r88 P2)) (not (td r89 P0)) (not (td r89 P1)) (not (td r89 P2)) (not (td r90 P0)) (not (td r90 P1)) (not (td r90 P2)) (not (td r91 P0)) (not (td r91 P1)) (not (td r91 P2)) (not (td r92 P0)) (not (td r92 P1)) (not (td r92 P2)) (not (td r93 P0)) (not (td r93 P1)) (not (td r93 P2)) (not (td r94 P0)) (not (td r94 P1)) (not (td r94 P2)) (not (td r95 P0)) (not (td r95 P1)) (not (td r95 P2)) (not (td r96 P0)) (not (td r96 P1)) (not (td r96 P2)) (not (td r97 P0)) (not (td r97 P1)) (not (td r97 P2)) (not (td r98 P0)) (not (td r98 P1)) (not (td r98 P2)) (not (td r99 P0)) (not (td r99 P1)) (not (td r99 P2)) (not (td r100 P0)) (not (td r100 P1)) (not (td r100 P2)) (not (td r101 P0)) (not (td r101 P1)) (not (td r101 P2)) (not (td r102 P0)) (not (td r102 P1)) (not (td r102 P2)) (not (td r103 P0)) (not (td r103 P1)) (not (td r103 P2)) (not (td r104 P0)) (not (td r104 P1)) (not (td r104 P2)) (not (td r105 P0)) (not (td r105 P1)) (not (td r105 P2)) (not (td r106 P0)) (not (td r106 P1)) (not (td r106 P2)) (not (td r107 P0)) (not (td r107 P1)) (not (td r107 P2)) (not (td r108 P0)) (not (td r108 P1)) (not (td r108 P2)) (not (td r109 P0)) (not (td r109 P1)) (not (td r109 P2)) (not (td r110 P0)) (not (td r110 P1)) (not (td r110 P2)) (not (td r111 P0)) (not (td r111 P1)) (not (td r111 P2)) (not (td r112 P0)) (not (td r112 P1)) (not (td r112 P2)) (not (td r113 P0)) (not (td r113 P1)) (not (td r113 P2)) (not (td r114 P0)) (not (td r114 P1)) (not (td r114 P2)) (not (td r115 P0)) (not (td r115 P1)) (not (td r115 P2)) (not (td r116 P0)) (not (td r116 P1)) (not (td r116 P2)) (not (td r117 P0)) (not (td r117 P1)) (not (td r117 P2)) (not (td r118 P0)) (not (td r118 P1)) (not (td r118 P2)) (not (td r119 P0)) (not (td r119 P1)) (not (td r119 P2)) (not (td r120 P0)) (not (td r120 P1)) (not (td r120 P2)) (not (td r121 P0)) (not (td r121 P1)) (not (td r121 P2)) (not (td r122 P0)) (not (td r122 P1)) (not (td r122 P2)) (not (td r123 P0)) (not (td r123 P1)) (not (td r123 P2)) (not (td r124 P0)) (not (td r124 P1)) (not (td r124 P2)) (not (td r125 P0)) (not (td r125 P1)) (not (td r125 P2)) (not (td r126 P0)) (not (td r126 P1)) (not (td r126 P2)) (not (td r127 P0)) (not (td r127 P1)) (not (td r127 P2)) (not (td r128 P0)) (not (td r128 P1)) (not (td r128 P2)) (not (td r129 P0)) (not (td r129 P1)) (not (td r129 P2)) (not (td r130 P0)) (not (td r130 P1)) (not (td r130 P2)) (not (td r131 P0)) (not (td r131 P1)) (not (td r131 P2)) (not (td r132 P0)) (not (td r132 P1)) (not (td r132 P2)) (not (td r133 P0)) (not (td r133 P1)) (not (td r133 P2)) (not (td r134 P0)) (not (td r134 P1)) (not (td r134 P2)) (not (td r135 P0)) (not (td r135 P1)) (not (td r135 P2)) (not (td r136 P0)) (not (td r136 P1)) (not (td r136 P2))
                    (td r0 Q0) (td r0 Q1) (td r0 Q2) (td r1 Q0) (td r1 Q1) (td r1 Q2) (td r2 Q0) (td r2 Q1) (td r2 Q2) (td r3 Q0) (td r3 Q1) (td r3 Q2) (td r4 Q0) (td r4 Q1) (td r4 Q2) (td r5 Q0) (td r5 Q1) (td r5 Q2) (td r6 Q0) (td r6 Q1) (td r6 Q2) (td r7 Q0) (td r7 Q1) (td r7 Q2) (td r8 Q0) (td r8 Q1) (td r8 Q2) (td r9 Q0) (td r9 Q1) (td r9 Q2) (td r10 Q0) (td r10 Q1) (td r10 Q2) (td r11 Q0) (td r11 Q1) (td r11 Q2) (td r12 Q0) (td r12 Q1) (td r12 Q2) (td r13 Q0) (td r13 Q1) (td r13 Q2) (td r14 Q0) (td r14 Q1) (td r14 Q2) (td r15 Q0) (td r15 Q1) (td r15 Q2) (td r16 Q0) (td r16 Q1) (td r16 Q2) (td r17 Q0) (td r17 Q1) (td r17 Q2) (td r18 Q0) (td r18 Q1) (td r18 Q2) (td r19 Q0) (td r19 Q1) (td r19 Q2) (td r20 Q0) (td r20 Q1) (td r20 Q2) (td r21 Q0) (td r21 Q1) (td r21 Q2) (td r22 Q0) (td r22 Q1) (td r22 Q2) (td r23 Q0) (td r23 Q1) (td r23 Q2) (td r24 Q0) (td r24 Q1) (td r24 Q2) (td r25 Q0) (td r25 Q1) (td r25 Q2) (td r26 Q0) (td r26 Q1) (td r26 Q2) (td r27 Q0) (td r27 Q1) (td r27 Q2) (td r28 Q0) (td r28 Q1) (td r28 Q2) (td r29 Q0) (td r29 Q1) (td r29 Q2) (td r30 Q0) (td r30 Q1) (td r30 Q2) (td r31 Q0) (td r31 Q1) (td r31 Q2) (td r32 Q0) (td r32 Q1) (td r32 Q2) (td r33 Q0) (td r33 Q1) (td r33 Q2) (td r34 Q0) (td r34 Q1) (td r34 Q2) (td r35 Q0) (td r35 Q1) (td r35 Q2) (td r36 Q0) (td r36 Q1) (td r36 Q2) (td r37 Q0) (td r37 Q1) (td r37 Q2) (td r38 Q0) (td r38 Q1) (td r38 Q2) (td r39 Q0) (td r39 Q1) (td r39 Q2) (td r40 Q0) (td r40 Q1) (td r40 Q2) (td r41 Q0) (td r41 Q1) (td r41 Q2) (td r42 Q0) (td r42 Q1) (td r42 Q2) (td r43 Q0) (td r43 Q1) (td r43 Q2) (td r44 Q0) (td r44 Q1) (td r44 Q2) (td r45 Q0) (td r45 Q1) (td r45 Q2) (td r46 Q0) (td r46 Q1) (td r46 Q2) (td r47 Q0) (td r47 Q1) (td r47 Q2) (td r48 Q0) (td r48 Q1) (td r48 Q2) (td r49 Q0) (td r49 Q1) (td r49 Q2) (td r50 Q0) (td r50 Q1) (td r50 Q2) (td r51 Q0) (td r51 Q1) (td r51 Q2) (td r52 Q0) (td r52 Q1) (td r52 Q2) (td r53 Q0) (td r53 Q1) (td r53 Q2) (td r54 Q0) (td r54 Q1) (td r54 Q2) (td r55 Q0) (td r55 Q1) (td r55 Q2) (td r56 Q0) (td r56 Q1) (td r56 Q2) (td r57 Q0) (td r57 Q1) (td r57 Q2) (td r58 Q0) (td r58 Q1) (td r58 Q2) (td r59 Q0) (td r59 Q1) (td r59 Q2) (td r60 Q0) (td r60 Q1) (td r60 Q2) (td r61 Q0) (td r61 Q1) (td r61 Q2) (td r62 Q0) (td r62 Q1) (td r62 Q2) (td r63 Q0) (td r63 Q1) (td r63 Q2) (td r64 Q0) (td r64 Q1) (td r64 Q2) (td r65 Q0) (td r65 Q1) (td r65 Q2) (td r66 Q0) (td r66 Q1) (td r66 Q2) (td r67 Q0) (td r67 Q1) (td r67 Q2) (td r68 Q0) (td r68 Q1) (td r68 Q2) (td r69 Q0) (td r69 Q1) (td r69 Q2) (td r70 Q0) (td r70 Q1) (td r70 Q2) (td r71 Q0) (td r71 Q1) (td r71 Q2) (td r72 Q0) (td r72 Q1) (td r72 Q2) (td r73 Q0) (td r73 Q1) (td r73 Q2) (td r74 Q0) (td r74 Q1) (td r74 Q2) (td r75 Q0) (td r75 Q1) (td r75 Q2) (td r76 Q0) (td r76 Q1) (td r76 Q2) (td r77 Q0) (td r77 Q1) (td r77 Q2) (td r78 Q0) (td r78 Q1) (td r78 Q2) (td r79 Q0) (td r79 Q1) (td r79 Q2) (td r80 Q0) (td r80 Q1) (td r80 Q2) (td r81 Q0) (td r81 Q1) (td r81 Q2) (td r82 Q0) (td r82 Q1) (td r82 Q2) (td r83 Q0) (td r83 Q1) (td r83 Q2) (td r84 Q0) (td r84 Q1) (td r84 Q2) (td r85 Q0) (td r85 Q1) (td r85 Q2) (td r86 Q0) (td r86 Q1) (td r86 Q2) (td r87 Q0) (td r87 Q1) (td r87 Q2) (td r88 Q0) (td r88 Q1) (td r88 Q2) (td r89 Q0) (td r89 Q1) (td r89 Q2) (td r90 Q0) (td r90 Q1) (td r90 Q2) (td r91 Q0) (td r91 Q1) (td r91 Q2) (td r92 Q0) (td r92 Q1) (td r92 Q2) (td r93 Q0) (td r93 Q1) (td r93 Q2) (td r94 Q0) (td r94 Q1) (td r94 Q2) (td r95 Q0) (td r95 Q1) (td r95 Q2) (td r96 Q0) (td r96 Q1) (td r96 Q2) (td r97 Q0) (td r97 Q1) (td r97 Q2) (td r98 Q0) (td r98 Q1) (td r98 Q2) (td r99 Q0) (td r99 Q1) (td r99 Q2) (td r100 Q0) (td r100 Q1) (td r100 Q2) (td r101 Q0) (td r101 Q1) (td r101 Q2) (td r102 Q0) (td r102 Q1) (td r102 Q2) (td r103 Q0) (td r103 Q1) (td r103 Q2) (td r104 Q0) (td r104 Q1) (td r104 Q2) (td r105 Q0) (td r105 Q1) (td r105 Q2) (td r106 Q0) (td r106 Q1) (td r106 Q2) (td r107 Q0) (td r107 Q1) (td r107 Q2) (td r108 Q0) (td r108 Q1) (td r108 Q2) (td r109 Q0) (td r109 Q1) (td r109 Q2) (td r110 Q0) (td r110 Q1) (td r110 Q2) (td r111 Q0) (td r111 Q1) (td r111 Q2) (td r112 Q0) (td r112 Q1) (td r112 Q2) (td r113 Q0) (td r113 Q1) (td r113 Q2) (td r114 Q0) (td r114 Q1) (td r114 Q2) (td r115 Q0) (td r115 Q1) (td r115 Q2) (td r116 Q0) (td r116 Q1) (td r116 Q2) (td r117 Q0) (td r117 Q1) (td r117 Q2) (td r118 Q0) (td r118 Q1) (td r118 Q2) (td r119 Q0) (td r119 Q1) (td r119 Q2) (td r120 Q0) (td r120 Q1) (td r120 Q2) (td r121 Q0) (td r121 Q1) (td r121 Q2) (td r122 Q0) (td r122 Q1) (td r122 Q2) (td r123 Q0) (td r123 Q1) (td r123 Q2) (td r124 Q0) (td r124 Q1) (td r124 Q2) (td r125 Q0) (td r125 Q1) (td r125 Q2) (td r126 Q0) (td r126 Q1) (td r126 Q2) (td r127 Q0) (td r127 Q1) (td r127 Q2) (td r128 Q0) (td r128 Q1) (td r128 Q2) (td r129 Q0) (td r129 Q1) (td r129 Q2) (td r130 Q0) (td r130 Q1) (td r130 Q2) (td r131 Q0) (td r131 Q1) (td r131 Q2) (td r132 Q0) (td r132 Q1) (td r132 Q2) (td r133 Q0) (td r133 Q1) (td r133 Q2) (td r134 Q0) (td r134 Q1) (td r134 Q2) (td r135 Q0) (td r135 Q1) (td r135 Q2) (td r136 Q0) (td r136 Q1) (td r136 Q2)
                    (= (b r0 P0) 1) (= (b r0 P1) 1) (= (b r0 P2) 1)
                    (= (b r136 Q0) 1) (= (b r136 Q1) 1) (= (b r136 Q2) 1)
                )
            )
        )