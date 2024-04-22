
        (define (problem prob3)
            (:domain mail-robots)
            (:objects
              r0 r2 - robot
              r1 - mailrobot
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40)
                
                (= (p r0) 1) (= (p r1) 0) (= (p r2) 0)
                (= (q r0) 1) (= (q r1) 0) (= (q r2) 0)
            )

            (:goal
                (and
                    (psd)
                    (qsd)
                    (= (p r0) 1)
                    (= (q r2) 1)
                )
            )
        )