(define (problem pb4)
            (:domain grid)
            (:objects 
                x01 x02 x03 x04 - x
                y01 y02 y03 y04 - y
                z01 z02 z03 z04 - z
                r1 r2 r3 - robot
            )
            (:init
                (isNextX x01 x02) (isNextX x02 x03) (isNextX x03 x04)
                (isNextY y01 y02) (isNextY y02 y03) (isNextY y03 y04)
                (isNextZ z01 z02) (isNextZ z02 z03) (isNextZ z03 z04)
                (atX r1 x04) (atX r2 x01) (atX r3 x01)
                (atY r1 y01) (atY r2 y04) (atY r3 y01)
                (atZ r1 z01) (atZ r2 z01) (atZ r3 z04)
            )
            (:goal
                (and  
                    (atX r1 x04) (atX r2 x04) (atX r3 x04)
                    (atY r1 y04) (atY r2 y04) (atY r3 y04)
                    (atZ r1 z04) (atZ r2 z04) (atZ r3 z04)
                )
            )
            )

                    