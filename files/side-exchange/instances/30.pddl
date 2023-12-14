
        (define (problem prob30)
            (:domain side-exchange)
            (:objects
              green yellow - color
              r1 r2 r3 - robot
            )
            
            (:init
                
                (= (q r1) 0) (= (q r2) 0) (= (q r3) 0)
                
                (= (b r1 yellow) 30) 
                (= (b r1 green) 0)
                (= (b r3 yellow) 0) 
                (= (b r3 green) 30) 
                
                (edge r1) 
                (edge r3)
                (next r1 r2) (next r2 r3)
            )

            (:goal
                (and
                    (= (b r1 yellow) 0) 
                    (= (b r1 green) 30)
                
                    (= (b r3 yellow) 30) 
                    (= (b r3 green) 0) 
                )
            )
        )