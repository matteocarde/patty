(define (problem pb13)
            (:domain grid)
            (:objects 
                x01 x02 x03 x04 x05 x06 x07 x08 x09 x10 x11 x12 x13 - x
                y01 y02 y03 y04 y05 y06 y07 y08 y09 y10 y11 y12 y13 - y
                z01 z02 z03 z04 z05 z06 z07 z08 z09 z10 z11 z12 z13 - z
                r1 r2 r3 - robot
            )
            (:init
                (isNextX x01 x02) (isNextX x02 x03) (isNextX x03 x04) (isNextX x04 x05) (isNextX x05 x06) (isNextX x06 x07) (isNextX x07 x08) (isNextX x08 x09) (isNextX x09 x10) (isNextX x10 x11) (isNextX x11 x12) (isNextX x12 x13) (isNextX x13 x01)
                (isNextY y01 y02) (isNextY y02 y03) (isNextY y03 y04) (isNextY y04 y05) (isNextY y05 y06) (isNextY y06 y07) (isNextY y07 y08) (isNextY y08 y09) (isNextY y09 y10) (isNextY y10 y11) (isNextY y11 y12) (isNextY y12 y13) (isNextY y13 y01)
                (isNextZ z01 z02) (isNextZ z02 z03) (isNextZ z03 z04) (isNextZ z04 z05) (isNextZ z05 z06) (isNextZ z06 z07) (isNextZ z07 z08) (isNextZ z08 z09) (isNextZ z09 z10) (isNextZ z10 z11) (isNextZ z11 z12) (isNextZ z12 z13) (isNextZ z13 z01)
                (atX r1 x13) (atX r2 x01) (atX r3 x01)
                (atY r1 y01) (atY r2 y13) (atY r3 y01)
                (atZ r1 z01) (atZ r2 z01) (atZ r3 z13)
            )
            (:goal
                (and  
                    (atX r1 x13) (atX r2 x13) (atX r3 x13)
                    (atY r1 y13) (atY r2 y13) (atY r3 y13)
                    (atZ r1 z13) (atZ r2 z13) (atZ r3 z13)
                )
            )
            )

                    