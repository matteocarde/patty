(define (problem pb3)
            (:domain grid)
            (:objects 
                x01 x02 x03 - x
                y01 y02 y03 - y
                z01 z02 z03 - z
                r1 r2 r3 - robot
            )
            (:init
                (isNextX x01 x02) (isNextX x02 x03) (isNextX x03 x01)
                (isNextY y01 y02) (isNextY y02 y03) (isNextY y03 y01)
                (isNextZ z01 z02) (isNextZ z02 z03) (isNextZ z03 z01)
                (atX r1 x03) (atX r2 x01) (atX r3 x01)
                (atY r1 y01) (atY r2 y03) (atY r3 y01)
                (atZ r1 z01) (atZ r2 z01) (atZ r3 z03)
            )
            (:goal
                (and  
                    (atX r1 x03) (atX r2 x03) (atX r3 x03)
                    (atY r1 y03) (atY r2 y03) (atY r3 y03)
                    (atZ r1 z03) (atZ r2 z03) (atZ r3 z03)
                )
            )
            )

                    