(define (problem pb7)
            (:domain grid)
            (:objects 
                x01 x02 x03 x04 x05 x06 x07 - x
                y01 y02 y03 y04 y05 y06 y07 - y
                z01 z02 z03 z04 z05 z06 z07 - z
                r1 r2 r3 - robot
            )
            (:init
                (isNextX x01 x02) (isNextX x02 x03) (isNextX x03 x04) (isNextX x04 x05) (isNextX x05 x06) (isNextX x06 x07) (isNextX x07 x01)
                (isNextY y01 y02) (isNextY y02 y03) (isNextY y03 y04) (isNextY y04 y05) (isNextY y05 y06) (isNextY y06 y07) (isNextY y07 y01)
                (isNextZ z01 z02) (isNextZ z02 z03) (isNextZ z03 z04) (isNextZ z04 z05) (isNextZ z05 z06) (isNextZ z06 z07) (isNextZ z07 z01)
                (atX r1 x07) (atX r2 x01) (atX r3 x01)
                (atY r1 y01) (atY r2 y07) (atY r3 y01)
                (atZ r1 z01) (atZ r2 z01) (atZ r3 z07)
            )
            (:goal
                (and  
                    (atX r1 x07) (atX r2 x07) (atX r3 x07)
                    (atY r1 y07) (atY r2 y07) (atY r3 y07)
                    (atZ r1 z07) (atZ r2 z07) (atZ r3 z07)
                )
            )
            )

                    