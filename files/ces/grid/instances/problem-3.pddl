(define (problem pb3)
    (:domain grid)
    (:objects
        r01 r02 r03 - row
        c01 c02 c03 - column
        r - robot
    )
    (:init
        (isLeft c01 c02)
        (isLeft c02 c03)
        (isLeft c03 c01)

        (isDown r01 r02)
        (isDown r02 r03)
        (isDown r03 r01)

        (atColumn r c01)
        (atRow r r01)
    )
    (:goal
        (and
            (atColumn r c02)
            (atRow r r02)
        )
    )
)