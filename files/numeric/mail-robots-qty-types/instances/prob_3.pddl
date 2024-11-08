
        (define (problem prob3)
            (:domain mail-robots)
            (:objects
              r0 r1 r2 - robot
              g0 - green
              y0 - yellow
            )
            
            (:init
                (= (L) 20)
                
                (= (i r0) 0) (= (i r1) 1) (= (i r2) 2)
                (next r0 r1) (next r1 r2)
                
                (= (x r0) 0) (= (x r1) 20) (= (x r2) 40)
                
                (= (g r0 g0) 1) (= (g r1 g0) 0) (= (g r2 g0) 0)
                (= (y r0 y0) 1) (= (y r1 y0) 0) (= (y r2 y0) 0)
                (= (hg r0) 1) (= (hg r1) 0) (= (hg r2) 0)
                (= (hy r0) 1) (= (hy r1) 0) (= (hy r2) 0)
            )

            (:goal
                (and
                    (gsd r0 g0) (gsd r1 g0)
                    (ysd r0 y0) (ysd r1 y0) (ysd r2 y0)
                    (= (hg r0) 1)
                    (= (hy r2) 1)
                )
            )
        )