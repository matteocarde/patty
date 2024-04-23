
        (define (problem prob2)
            (:domain mail-robots)
            (:objects
              r0 r1 - robot
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1)
                
                (= (x r0) 0) (= (x r1) 20)
                
                (= (p r0) 1) (= (p r1) 0)
            )

            (:goal
                (and
                    (psd r0) (psd r1)
                    (= (p r0) 1)
                )
            )
        )