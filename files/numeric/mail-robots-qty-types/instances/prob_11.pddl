
        (define (problem prob11)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 r3 r4 r5 r6 r7 r8 r9 r10 - robot
              g0 - green
              y0 - yellow
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2) (= (i r3) 3) (= (i r4) 4) (= (i r5) 5) (= (i r6) 6) (= (i r7) 7) (= (i r8) 8) (= (i r9) 9) (= (i r10) 10)
                (next r0 r1) (next r1 r2) (next r2 r3) (next r3 r4) (next r4 r5) (next r5 r6) (next r6 r7) (next r7 r8) (next r8 r9) (next r9 r10)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40) (= (x r3) 60) (= (x r4) 80) (= (x r5) 100) (= (x r6) 120) (= (x r7) 140) (= (x r8) 160) (= (x r9) 180) (= (x r10) 200)
                
                (= (g r0 g0) 1) (= (g r1 g0) 0) (= (g r2 g0) 0) (= (g r3 g0) 0) (= (g r4 g0) 0) (= (g r5 g0) 0) (= (g r6 g0) 0) (= (g r7 g0) 0) (= (g r8 g0) 0) (= (g r9 g0) 0) (= (g r10 g0) 0)
                (= (y r0 y0) 1) (= (y r1 y0) 0) (= (y r2 y0) 0) (= (y r3 y0) 0) (= (y r4 y0) 0) (= (y r5 y0) 0) (= (y r6 y0) 0) (= (y r7 y0) 0) (= (y r8 y0) 0) (= (y r9 y0) 0) (= (y r10 y0) 0)
                (= (hg r0) 1) (= (hg r1) 0) (= (hg r2) 0) (= (hg r3) 0) (= (hg r4) 0) (= (hg r5) 0) (= (hg r6) 0) (= (hg r7) 0) (= (hg r8) 0) (= (hg r9) 0) (= (hg r10) 0)
                (= (hy r0) 1) (= (hy r1) 0) (= (hy r2) 0) (= (hy r3) 0) (= (hy r4) 0) (= (hy r5) 0) (= (hy r6) 0) (= (hy r7) 0) (= (hy r8) 0) (= (hy r9) 0) (= (hy r10) 0)
            )

            (:goal
                (and
                    (gsd r0 g0) (gsd r1 g0) (gsd r2 g0) (gsd r3 g0) (gsd r4 g0) (gsd r5 g0)
                    (ysd r0 y0) (ysd r1 y0) (ysd r2 y0) (ysd r3 y0) (ysd r4 y0) (ysd r5 y0) (ysd r6 y0) (ysd r7 y0) (ysd r8 y0) (ysd r9 y0) (ysd r10 y0)
                    (= (hg r0) 1)
                    (= (hy r10) 1)
                )
            )
        )