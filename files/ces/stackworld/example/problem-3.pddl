(define (problem pb01)
    (:domain stackworld)
    (:objects
        c1 c2 c3 - card
    )
    (:init
        (first c1)
        (on-top c1 c2)
        (on-top c2 c3)
        (last c3)
    )
    (:goal
        (first c3)
        (last c2)
    )
)