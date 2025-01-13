(define (problem pb15)
            (:domain grid)
            (:objects 
                r01 r02 r03 r04 r05 r06 r07 r08 r09 r10 r11 r12 r13 r14 r15 - row
                c01 c02 c03 c04 c05 c06 c07 c08 c09 c10 c11 c12 c13 c14 c15 - column
                r - robot
            )
            (:init
                (isLeft c01 c02) (isLeft c02 c03) (isLeft c03 c04) (isLeft c04 c05) (isLeft c05 c06) (isLeft c06 c07) (isLeft c07 c08) (isLeft c08 c09) (isLeft c09 c10) (isLeft c10 c11) (isLeft c11 c12) (isLeft c12 c13) (isLeft c13 c14) (isLeft c14 c15) (isLeft c15 c01)
                (isDown r01 r02) (isDown r02 r03) (isDown r03 r04) (isDown r04 r05) (isDown r05 r06) (isDown r06 r07) (isDown r07 r08) (isDown r08 r09) (isDown r09 r10) (isDown r10 r11) (isDown r11 r12) (isDown r12 r13) (isDown r13 r14) (isDown r14 r15) (isDown r15 r01)
                (atColumn r c01)
                (atRow r r01)
            )
            (:goal
                (and  
                    (atColumn r c08)
                    (atRow r r08)
                )
            )
            )

                    