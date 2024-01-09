(define (domain optional_goals_3_2)
    (:requirements :fluents :equality :typing :durative-actions :action-costs)

    (:predicates
        (x11)
        (x12)
        (x13)
        (x21)
        (x22)
        (x23)
        (y)
        (g1)
        (g2)
    )

    (:functions
        (total-cost)
    )

    (:durative-action set_x11
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x11))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x12
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x12))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x13
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x13))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x21
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x21))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x22
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x22))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x23
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x23))
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
                (at start (x11))
                (at start (x12))
                (at start (x13))
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
                (at start (x21))
                (at start (x22))
                (at start (x23))
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
