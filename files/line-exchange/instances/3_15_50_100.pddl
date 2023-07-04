
        (define (problem prob01)
            (:domain line-exchange)
            (:objects
              r0 r1 r2 - robot
            )
            
            (:init
                (= (D) 100)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2)
                
                (= (x r0) 50.0) (= (x r1) 150.0) (= (x r2) 250.0)
                
                (= (q r0) 11) (= (q r1) 19) (= (q r2) 15)
                
                (= (e r0 r1) 1) (= (e r1 r2) 1)
                
                (next r0 r1) (next r1 r2)
            )

            (:goal
                (and
                    (= (x r0) 50.0) (= (x r1) 150.0) (= (x r2) 250.0)
                    
                    (= (q r0) (q r1)) (= (q r1) (q r2))
                )
            )
        )