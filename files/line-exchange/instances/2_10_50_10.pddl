
        (define (problem prob01)
            (:domain line-exchange)
            (:objects
              r0 r1 - robot
            )
            
            (:init
                (= (D) 10)
                
                (= (i r0) 0) (= (i r1) 1)
                
                (= (x r0) 5.0) (= (x r1) 15.0)
                
                (= (q r0) 9) (= (q r1) 11)
                
                (= (e r0 r1) 1)
                
                (next r0 r1)
            )

            (:goal
                (and
                    (= (x r0) 5.0) (= (x r1) 15.0)
                    
                    (= (q r0) (q r1))
                )
            )
        )