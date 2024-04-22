
        (define (problem prob5)
            (:domain mail-robots)
            (:objects
              r0 r1 r3 r4 - robot
              r2 - mailrobot
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80)
                
                (= (p r0) 1) (= (p r1) 0) (= (p r2) 0) (= (p r3) 0) (= (p r4) 0)
                (= (q r0) 1) (= (q r1) 0) (= (q r2) 0) (= (q r3) 0) (= (q r4) 0)
            )

            (:goal
                (and
                    (psd)
                    (qsd)
                    (= (p r0) 1)
                    (= (q r4) 1)
                )
            )
        )