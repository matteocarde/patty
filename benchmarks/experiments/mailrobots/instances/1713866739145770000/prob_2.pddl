
        (define (problem prob2)
            (:domain mail-robots)
            (:objects
              r0 r1 - robot
              l0 l1 - letter
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1)
                
                (= (x r0) 0) (= (x r1) 20)
                
                (= (p r0 l0) 1) (= (p r0 l1) 1) (= (p r1 l0) 0) (= (p r1 l1) 0)
                (= (h r0) 5) (= (h r1) 0)
            )

            (:goal
                (and
                    (psd r0 l0) (psd r0 l1) (psd r1 l0) (psd r1 l1)
                    (= (h r0) 5)
                )
            )
        )