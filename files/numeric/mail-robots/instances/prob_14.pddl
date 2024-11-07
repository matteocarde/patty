
        (define (problem prob14)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 r11 r12 r13 - robot
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4) (= (i r5) 5) (= (i r6) 6) (= (i r7) 7) (= (i r8) 8) (= (i r9) 9) (= (i r10) 10) (= (i r11) 11) (= (i r12) 12) (= (i r13) 13)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80) (= (x r5) 100) (= (x r6) 120) (= (x r7) 140) (= (x r8) 160) (= (x r9) 180) (= (x r10) 200) (= (x r11) 220) (= (x r12) 240) (= (x r13) 260)
                
                (= (p r0) 1) (= (p r1) 0) (= (p r2) 0) (= (p r3) 0) (= (p r4) 0) (= (p r5) 0) (= (p r6) 0) (= (p r7) 0) (= (p r8) 0) (= (p r9) 0) (= (p r10) 0) (= (p r11) 0) (= (p r12) 0) (= (p r13) 0)
            )

            (:goal
                (and
                    (psd r0) (psd r1) (psd r2) (psd r3) (psd r4) (psd r5) (psd r6) (psd r7) (psd r8) (psd r9) (psd r10) (psd r11) (psd r12) (psd r13)
                    (= (p r0) 1)
                )
            )
        )