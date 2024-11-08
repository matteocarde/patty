
        (define (problem prob3)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 - robot
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40)
                
                (= (p r0) 1) (= (p r1) 0) (= (p r2) 0)
            )

            (:goal
                (and
                    (psd r0) (psd r1) (psd r2)
                    (= (p r0) 1)
                )
            )
        )