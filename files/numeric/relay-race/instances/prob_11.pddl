
        (define (problem prob11)
            (:domain relay-race)
            (:objects
              r0 r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 - runner
              P0 P1 Q0 Q1 - baton
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4) (= (i r5) 5) (= (i r6) 6) (= (i r7) 7) (= (i r8) 8) (= (i r9) 9) (= (i r10) 10)
                (next r0 r1) (next r1 r2) (next r2 r3) (next r3 r4) (next r4 r5) (next r5 r6) (next r6 r7) (next r7 r8) (next r8 r9) (next r9 r10)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80) (= (x r5) 100) (= (x r6) 120) (= (x r7) 140) (= (x r8) 160) (= (x r9) 180) (= (x r10) 200)
                
                (= (b r0 P0) 1) (= (b r0 P1) 1) (= (b r1 P0) 0) (= (b r1 P1) 0) (= (b r2 P0) 0) (= (b r2 P1) 0) (= (b r3 P0) 0) (= (b r3 P1) 0) (= (b r4 P0) 0) (= (b r4 P1) 0) (= (b r5 P0) 0) (= (b r5 P1) 0) (= (b r6 P0) 0) (= (b r6 P1) 0) (= (b r7 P0) 0) (= (b r7 P1) 0) (= (b r8 P0) 0) (= (b r8 P1) 0) (= (b r9 P0) 0) (= (b r9 P1) 0) (= (b r10 P0) 0) (= (b r10 P1) 0)
                (= (b r0 Q0) 1) (= (b r0 Q1) 1) (= (b r1 Q0) 0) (= (b r1 Q1) 0) (= (b r2 Q0) 0) (= (b r2 Q1) 0) (= (b r3 Q0) 0) (= (b r3 Q1) 0) (= (b r4 Q0) 0) (= (b r4 Q1) 0) (= (b r5 Q0) 0) (= (b r5 Q1) 0) (= (b r6 Q0) 0) (= (b r6 Q1) 0) (= (b r7 Q0) 0) (= (b r7 Q1) 0) (= (b r8 Q0) 0) (= (b r8 Q1) 0) (= (b r9 Q0) 0) (= (b r9 Q1) 0) (= (b r10 Q0) 0) (= (b r10 Q1) 0)
                (= (h r0) 4) (= (h r1) 0) (= (h r2) 0) (= (h r3) 0) (= (h r4) 0) (= (h r5) 0) (= (h r6) 0) (= (h r7) 0) (= (h r8) 0) (= (h r9) 0) (= (h r10) 0)
                
                (td r0 P0) (td r0 P1)
                (td r0 Q0) (td r0 Q1)
            )

            (:goal
                (and
                    (td r0 P0) (td r0 P1) (td r1 P0) (td r1 P1) (td r2 P0) (td r2 P1) (td r3 P0) (td r3 P1) (td r4 P0) (td r4 P1) (td r5 P0) (td r5 P1)
                    (not (td r6 P0)) (not (td r6 P1)) (not (td r7 P0)) (not (td r7 P1)) (not (td r8 P0)) (not (td r8 P1)) (not (td r9 P0)) (not (td r9 P1)) (not (td r10 P0)) (not (td r10 P1))
                    (td r0 Q0) (td r0 Q1) (td r1 Q0) (td r1 Q1) (td r2 Q0) (td r2 Q1) (td r3 Q0) (td r3 Q1) (td r4 Q0) (td r4 Q1) (td r5 Q0) (td r5 Q1) (td r6 Q0) (td r6 Q1) (td r7 Q0) (td r7 Q1) (td r8 Q0) (td r8 Q1) (td r9 Q0) (td r9 Q1) (td r10 Q0) (td r10 Q1)
                    (= (b r0 P0) 1) (= (b r0 P1) 1)
                    (= (b r10 Q0) 1) (= (b r10 Q1) 1)
                )
            )
        )