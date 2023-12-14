
        (define (problem prob01)
            (:domain line-exchange)
            (:objects
              r0 r1 r2 r3 - robot
            )
            
            (:init
                (= (D) 2)
                
                (= (max_q) 7)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3)
                
                (= (x r0) 1.0) (= (x r1) 3.0) (= (x r2) 5.0) (= (x r3) 7.0)
                
                (= (q r0) 7) (= (q r1) 0) (= (q r2) 0) (= (q r3) 0)
                
                (= (e r0 r1) 1) (= (e r1 r2) 1) (= (e r2 r3) 1)
                
                (next r0 r1) (next r1 r2) (next r2 r3)
            )

            (:goal
                (and
                    (= (x r0) 1.0) (= (x r1) 3.0) (= (x r2) 5.0) (= (x r3) 7.0)
                    
                    (= (q r3) 7)
                )
            )
        )