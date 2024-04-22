
        (define (problem prob9)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 r3 r5 r6 r7 r8 - robot
              r4 - mailrobot
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4) (= (i r5) 5) (= (i r6) 6) (= (i r7) 7) (= (i r8) 8)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80) (= (x r5) 100) (= (x r6) 120) (= (x r7) 140) (= (x r8) 160)
                
                (= (p r0) 1) (= (p r1) 0) (= (p r2) 0) (= (p r3) 0) (= (p r4) 0) (= (p r5) 0) (= (p r6) 0) (= (p r7) 0) (= (p r8) 0)
                (= (q r0) 1) (= (q r1) 0) (= (q r2) 0) (= (q r3) 0) (= (q r4) 0) (= (q r5) 0) (= (q r6) 0) (= (q r7) 0) (= (q r8) 0)
            )

            (:goal
                (and
                    (psd)
                    (qsd)
                    (= (p r0) 1)
                    (= (q r8) 1)
                )
            )
        )