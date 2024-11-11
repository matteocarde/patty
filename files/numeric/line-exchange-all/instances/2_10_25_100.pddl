
        (define (problem prob01)
            (:domain line-exchange)
            (:objects
              r0 r1 - robot
            )
            
            (:init
                (= (D) 100)
                
                (= (i r0) 0) (= (i r1) 1)
                
                (= (x r0) 50.0) (= (x r1) 150.0)
                
                (= (q r0) 10) (= (q r1) 10)
                
                (= (e r0 r1) 1)
                
                (next r0 r1)
            )

            (:goal
                (and
                    (= (x r0) 50.0) (= (x r1) 150.0)
                    
                    (= (q r0) (q r1))
                )
            )
        )