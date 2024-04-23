
        (define (problem prob3)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 - robot
              l0 l1 l2 - letter
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40)
                
                (= (p r0 l0) 1) (= (p r0 l1) 1) (= (p r0 l2) 1) (= (p r1 l0) 0) (= (p r1 l1) 0) (= (p r1 l2) 0) (= (p r2 l0) 0) (= (p r2 l1) 0) (= (p r2 l2) 0)
                (= (h r0) 5) (= (h r1) 0) (= (h r2) 0)
            )

            (:goal
                (and
                    (psd r0 l0) (psd r0 l1) (psd r0 l2) (psd r1 l0) (psd r1 l1) (psd r1 l2) (psd r2 l0) (psd r2 l1) (psd r2 l2)
                    (= (h r0) 5)
                )
            )
        )