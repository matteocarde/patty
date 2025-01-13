(define (problem pb5)
            (:domain grid)
            (:objects 
                r01 r02 r03 r04 r05 - row
                c01 c02 c03 c04 c05 - column
                r - robot
            )
            (:init
                (isLeft c01 c02) (isLeft c02 c03) (isLeft c03 c04) (isLeft c04 c05) (isLeft c05 c01)
                (isDown r01 r02) (isDown r02 r03) (isDown r03 r04) (isDown r04 r05) (isDown r05 r01)
                (atColumn r c01)
                (atRow r r01)
            )
            (:goal
                (and  
                    (atColumn r c03)
                    (atRow r r03)
                )
            )
            )

                    