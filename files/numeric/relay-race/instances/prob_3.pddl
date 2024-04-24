
        (define (problem prob3)
            (:domain relay-race)
            (:objects
              r0 r1 r2 - runner
              P0 P1 P2 Q0 Q1 Q2 - baton
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2)
                (next r0 r1) (next r1 r2)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40)
                
                (= (b r0 P0) 1) (= (b r0 P1) 1) (= (b r0 P2) 1) (= (b r1 P0) 0) (= (b r1 P1) 0) (= (b r1 P2) 0) (= (b r2 P0) 0) (= (b r2 P1) 0) (= (b r2 P2) 0)
                (= (b r0 Q0) 1) (= (b r0 Q1) 1) (= (b r0 Q2) 1) (= (b r1 Q0) 0) (= (b r1 Q1) 0) (= (b r1 Q2) 0) (= (b r2 Q0) 0) (= (b r2 Q1) 0) (= (b r2 Q2) 0)
                (= (h r0) 6) (= (h r1) 0) (= (h r2) 0)
                
                (td r0 P0) (td r0 P1) (td r0 P2)
                (td r0 Q0) (td r0 Q1) (td r0 Q2)
            )

            (:goal
                (and
                    (td r0 P0) (td r0 P1) (td r0 P2) (td r1 P0) (td r1 P1) (td r1 P2)
                    (not (td r2 P0)) (not (td r2 P1)) (not (td r2 P2))
                    (td r0 Q0) (td r0 Q1) (td r0 Q2) (td r1 Q0) (td r1 Q1) (td r1 Q2) (td r2 Q0) (td r2 Q1) (td r2 Q2)
                    (= (b r0 P0) 1) (= (b r0 P1) 1) (= (b r0 P2) 1)
                    (= (b r2 Q0) 1) (= (b r2 Q1) 1) (= (b r2 Q2) 1)
                )
            )
        )