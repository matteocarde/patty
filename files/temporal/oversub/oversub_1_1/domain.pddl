(define (domain optional_goals_1_1)
    (:requirements :fluents :equality :typing :durative-actions :action-costs)

    (:predicates
        (x1)
        (y)
        (g1)
    )

    (:functions
        (total-cost)
    )

    (:durative-action set_x1
        :parameters ()
        :duration (= ?duration 1)
        :effect (and
            (at start (x1))
            (at end (increase (total-cost) 1))
        )
    )

    (:durative-action set_y
        :parameters ()
        :duration (= ?duration 1)
        :effect (and
            (at start (y))
            (at end (increase (total-cost) 1))
        )
    )

    (:durative-action goal1
        :parameters ()
        :duration (= ?duration 1)
        :condition (and
            (at start (x1))
        )
        :effect (and
            (at end (g1))
            (at end (increase (total-cost) 1))
        )
    )

    (:durative-action goal1_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect (and
            (at end (g1))
            (at end (increase (total-cost) 200))
        )
    )
)