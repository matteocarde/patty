(define (problem pb01)
    (:domain stackworld)
    (:objects
        lft rgt - ground
        b1 b2 b3 b4 b5 b6 b7 - block
    )
    (:init
        (free b1)
        (on-top b1 b2)
        (on-top b2 b3)
        (on-top b3 b4)
        (on-top b4 b5)
        (on-top b5 b6)
        (on-top b6 b7)
        (on-top b7 lft)
        (free rgt)
    )
    (:goal
        ; (on-top b3 b2)
        (free lft)
    )
)