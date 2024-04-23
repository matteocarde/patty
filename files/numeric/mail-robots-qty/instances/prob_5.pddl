
        (define (problem prob5)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 r3 r4 - robot
              l0 l1 - letter
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4)
                (next r0 r1) (next r1 r2) (next r2 r3) (next r3 r4)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80)
                
                (= (p r0 l0) 1) (= (p r0 l1) 1) (= (p r1 l0) 0) (= (p r1 l1) 0) (= (p r2 l0) 0) (= (p r2 l1) 0) (= (p r3 l0) 0) (= (p r3 l1) 0) (= (p r4 l0) 0) (= (p r4 l1) 0)
                (= (h r0) 2) (= (h r1) 0) (= (h r2) 0) (= (h r3) 0) (= (h r4) 0)
            )

            (:goal
                (and
                    (psd r0 l0) (psd r0 l1) (psd r1 l0) (psd r1 l1) (psd r2 l0) (psd r2 l1) (psd r3 l0) (psd r3 l1) (psd r4 l0) (psd r4 l1)
                    (= (h r0) 2)
                )
            )
        )