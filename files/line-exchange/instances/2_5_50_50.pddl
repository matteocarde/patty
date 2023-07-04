
        (define (problem prob01)
            (:domain line-exchange)
            (:objects
              r0 r1 - robot
            )
            
            (:init
                (= (D) 50)
                
                (= (i r0) 0) (= (i r1) 1)
                
                (= (x r0) 25.0) (= (x r1) 75.0)
                
                (= (q r0) 3) (= (q r1) 7)
                
                (= (e r0 r1) 1)
                
                (next r0 r1)
            )

            (:goal
                (and
                    (= (x r0) 25.0) (= (x r1) 75.0)
                    
                    (= (q r0) (q r1))
                )
            )
        )