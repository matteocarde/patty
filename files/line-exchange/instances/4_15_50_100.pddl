
        (define (problem prob01)
            (:domain line-exchange)
            (:objects
              r0 r1 r2 r3 - robot
            )
            
            (:init
                (= (D) 100)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3)
                
                (= (x r0) 50.0) (= (x r1) 150.0) (= (x r2) 250.0) (= (x r3) 350.0)
                
                (= (q r0) 6) (= (q r1) 23) (= (q r2) 14) (= (q r3) 17)
                
                (= (e r0 r1) 1) (= (e r1 r2) 1) (= (e r2 r3) 1)
                
                (next r0 r1) (next r1 r2) (next r2 r3)
            )

            (:goal
                (and
                    (= (x r0) 50.0) (= (x r1) 150.0) (= (x r2) 250.0) (= (x r3) 350.0)
                    
                    (= (q r0) (q r1)) (= (q r1) (q r2)) (= (q r2) (q r3))
                )
            )
        )