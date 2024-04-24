
        (define (problem prob7)
            (:domain relay-race)
            (:objects
              r0 r1 r2 r3 r4 r5 r6 - runner
              P0 P1 P2 Q0 Q1 Q2 - baton
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4) (= (i r5) 5) (= (i r6) 6)
                (next r0 r1) (next r1 r2) (next r2 r3) (next r3 r4) (next r4 r5) (next r5 r6)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80) (= (x r5) 100) (= (x r6) 120)
                
                (= (b r0 P0) 1) (= (b r0 P1) 1) (= (b r0 P2) 1) (= (b r1 P0) 0) (= (b r1 P1) 0) (= (b r1 P2) 0) (= (b r2 P0) 0) (= (b r2 P1) 0) (= (b r2 P2) 0) (= (b r3 P0) 0) (= (b r3 P1) 0) (= (b r3 P2) 0) (= (b r4 P0) 0) (= (b r4 P1) 0) (= (b r4 P2) 0) (= (b r5 P0) 0) (= (b r5 P1) 0) (= (b r5 P2) 0) (= (b r6 P0) 0) (= (b r6 P1) 0) (= (b r6 P2) 0)
                (= (b r0 Q0) 1) (= (b r0 Q1) 1) (= (b r0 Q2) 1) (= (b r1 Q0) 0) (= (b r1 Q1) 0) (= (b r1 Q2) 0) (= (b r2 Q0) 0) (= (b r2 Q1) 0) (= (b r2 Q2) 0) (= (b r3 Q0) 0) (= (b r3 Q1) 0) (= (b r3 Q2) 0) (= (b r4 Q0) 0) (= (b r4 Q1) 0) (= (b r4 Q2) 0) (= (b r5 Q0) 0) (= (b r5 Q1) 0) (= (b r5 Q2) 0) (= (b r6 Q0) 0) (= (b r6 Q1) 0) (= (b r6 Q2) 0)
                (= (h r0) 6) (= (h r1) 0) (= (h r2) 0) (= (h r3) 0) (= (h r4) 0) (= (h r5) 0) (= (h r6) 0)
                
                (td r0 P0) (td r0 P1) (td r0 P2)
                (td r0 Q0) (td r0 Q1) (td r0 Q2)
            )

            (:goal
                (and
                    (td r0 P0) (td r0 P1) (td r0 P2) (td r1 P0) (td r1 P1) (td r1 P2) (td r2 P0) (td r2 P1) (td r2 P2) (td r3 P0) (td r3 P1) (td r3 P2)
                    (not (td r4 P0)) (not (td r4 P1)) (not (td r4 P2)) (not (td r5 P0)) (not (td r5 P1)) (not (td r5 P2)) (not (td r6 P0)) (not (td r6 P1)) (not (td r6 P2))
                    (td r0 Q0) (td r0 Q1) (td r0 Q2) (td r1 Q0) (td r1 Q1) (td r1 Q2) (td r2 Q0) (td r2 Q1) (td r2 Q2) (td r3 Q0) (td r3 Q1) (td r3 Q2) (td r4 Q0) (td r4 Q1) (td r4 Q2) (td r5 Q0) (td r5 Q1) (td r5 Q2) (td r6 Q0) (td r6 Q1) (td r6 Q2)
                    (= (b r0 P0) 1) (= (b r0 P1) 1) (= (b r0 P2) 1)
                    (= (b r6 Q0) 1) (= (b r6 Q1) 1) (= (b r6 Q2) 1)
                )
            )
        )