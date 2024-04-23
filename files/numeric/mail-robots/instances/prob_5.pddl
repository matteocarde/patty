
        (define (problem prob5)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 r3 r4 - robot
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80)
                
                (= (p r0) 1) (= (p r1) 0) (= (p r2) 0) (= (p r3) 0) (= (p r4) 0)
            )

            (:goal
                (and
                    (psd r0) (psd r1) (psd r2) (psd r3) (psd r4)
                    (= (p r0) 1)
                )
            )
        )