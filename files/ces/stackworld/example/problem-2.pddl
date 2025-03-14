(define (problem pb01)
    (:domain stackworld)
    (:objects
        f - first
        l - last
        c1 c2 - movable
    )
    (:init
        (on-top f c1)
        (on-top c1 c2)
        (on-top c2 l)
    )
    (:goal
        (on-top c2 c1)
    )
)