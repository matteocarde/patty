(define (problem pb20)
            (:domain grid)
            (:objects 
                x01 x02 x03 x04 x05 x06 x07 x08 x09 x10 x11 x12 x13 x14 x15 x16 x17 x18 x19 x20 - x
                y01 y02 y03 y04 y05 y06 y07 y08 y09 y10 y11 y12 y13 y14 y15 y16 y17 y18 y19 y20 - y
                z01 z02 z03 z04 z05 z06 z07 z08 z09 z10 z11 z12 z13 z14 z15 z16 z17 z18 z19 z20 - z
                r1 r2 r3 - robot
            )
            (:init
                (isNextX x01 x02) (isNextX x02 x03) (isNextX x03 x04) (isNextX x04 x05) (isNextX x05 x06) (isNextX x06 x07) (isNextX x07 x08) (isNextX x08 x09) (isNextX x09 x10) (isNextX x10 x11) (isNextX x11 x12) (isNextX x12 x13) (isNextX x13 x14) (isNextX x14 x15) (isNextX x15 x16) (isNextX x16 x17) (isNextX x17 x18) (isNextX x18 x19) (isNextX x19 x20) (isNextX x20 x01)
                (isNextY y01 y02) (isNextY y02 y03) (isNextY y03 y04) (isNextY y04 y05) (isNextY y05 y06) (isNextY y06 y07) (isNextY y07 y08) (isNextY y08 y09) (isNextY y09 y10) (isNextY y10 y11) (isNextY y11 y12) (isNextY y12 y13) (isNextY y13 y14) (isNextY y14 y15) (isNextY y15 y16) (isNextY y16 y17) (isNextY y17 y18) (isNextY y18 y19) (isNextY y19 y20) (isNextY y20 y01)
                (isNextZ z01 z02) (isNextZ z02 z03) (isNextZ z03 z04) (isNextZ z04 z05) (isNextZ z05 z06) (isNextZ z06 z07) (isNextZ z07 z08) (isNextZ z08 z09) (isNextZ z09 z10) (isNextZ z10 z11) (isNextZ z11 z12) (isNextZ z12 z13) (isNextZ z13 z14) (isNextZ z14 z15) (isNextZ z15 z16) (isNextZ z16 z17) (isNextZ z17 z18) (isNextZ z18 z19) (isNextZ z19 z20) (isNextZ z20 z01)
                (atX r1 x20) (atX r2 x01) (atX r3 x01)
                (atY r1 y01) (atY r2 y20) (atY r3 y01)
                (atZ r1 z01) (atZ r2 z01) (atZ r3 z20)
            )
            (:goal
                (and  
                    (atX r1 x20) (atX r2 x20) (atX r3 x20)
                    (atY r1 y20) (atY r2 y20) (atY r3 y20)
                    (atZ r1 z20) (atZ r2 z20) (atZ r3 z20)
                )
            )
            )

                    