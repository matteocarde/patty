(define (domain optional_goals_2_4)
    (:requirements :fluents :equality :typing :durative-actions :action-costs)

    (:predicates
        (x11)
        (x12)
        (x21)
        (x22)
        (x31)
        (x32)
        (x41)
        (x42)
        (y)
        (g1)
        (g2)
        (g3)
        (g4)
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
                (at end (x11))
            )
    )

    (:durative-action set_x12
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x12))
                (at end (x12))
            )
    )

    (:durative-action set_x21
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x21))
                (at end (x21))
            )
    )

    (:durative-action set_x22
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x22))
                (at end (x22))
            )
    )

    (:durative-action set_x31
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x31))
                (at end (x31))
            )
    )

    (:durative-action set_x32
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x32))
                (at end (x32))
            )
    )

    (:durative-action set_x41
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x41))
                (at end (x41))
            )
    )

    (:durative-action set_x42
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x42))
                (at end (x42))
            )
    )

    (:durative-action set_y
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (y))
                (at end (y))
            )
    )

    (:durative-action goal1
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x11))
                (at start (x12))
            )
        :effect
            (and
                (at end (g1))
            )
    )

    (:durative-action goal2
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x21))
                (at start (x22))
            )
        :effect
            (and
                (at end (g2))
            )
    )

    (:durative-action goal3
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x31))
                (at start (x32))
            )
        :effect
            (and
                (at end (g3))
            )
    )

    (:durative-action goal4
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x41))
                (at start (x42))
            )
        :effect
            (and
                (at end (g4))
            )
    )

    (:durative-action goal1_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (g1))
                (at end (g1))
            )
    )

    (:durative-action goal2_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (g2))
                (at end (g2))
            )
    )

    (:durative-action goal3_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (g3))
                (at end (g3))
            )
    )

    (:durative-action goal4_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (g4))
                (at end (g4))
            )
    )
)
