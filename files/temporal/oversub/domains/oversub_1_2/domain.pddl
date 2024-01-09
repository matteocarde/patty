(define (domain optional_goals_1_2)
    (:requirements :fluents :equality :typing :durative-actions :action-costs)

    (:predicates
        (x1)
        (x2)
        (y)
        (g1)
        (g2)
    )

    (:functions
        (total-cost)
    )

    (:durative-action set_x1
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x1))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x2
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x2))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_y
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (y))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action goal1
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x1))
            )
        :effect
            (and
                (at end (g1))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action goal2
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x2))
            )
        :effect
            (and
                (at end (g2))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action goal1_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at end (g1))
                (at end (increase (total-cost) 200))
            )
    )

    (:durative-action goal2_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at end (g2))
                (at end (increase (total-cost) 200))
            )
    )
)
