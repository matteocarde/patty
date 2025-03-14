(define (problem pb5)
            (:domain grid)
            (:objects 
                x01 x02 x03 x04 x05 - x
                y01 y02 y03 y04 y05 - y
                z01 z02 z03 z04 z05 - z
                r1 r2 r3 - robot
            )
            (:init
                (isNextX x01 x02) (isNextX x02 x03) (isNextX x03 x04) (isNextX x04 x05)
                (isNextY y01 y02) (isNextY y02 y03) (isNextY y03 y04) (isNextY y04 y05)
                (isNextZ z01 z02) (isNextZ z02 z03) (isNextZ z03 z04) (isNextZ z04 z05)
                (atX r1 x05) (atX r2 x01) (atX r3 x01)
                (atY r1 y01) (atY r2 y05) (atY r3 y01)
                (atZ r1 z01) (atZ r2 z01) (atZ r3 z05)
            )
            (:goal
                (and  
                    (atX r1 x05) (atX r2 x05) (atX r3 x05)
                    (atY r1 y05) (atY r2 y05) (atY r3 y05)
                    (atZ r1 z05) (atZ r2 z05) (atZ r3 z05)
                )
            )
            )

                    