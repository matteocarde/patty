(define (domain optional_goals_2_7)
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
        (x51)
        (x52)
        (x61)
        (x62)
        (x71)
        (x72)
        (y)
        (g1)
        (g2)
        (g3)
        (g4)
        (g5)
        (g6)
        (g7)
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

    (:durative-action set_x31
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x31))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x32
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x32))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x41
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x41))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x42
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x42))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x51
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x51))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x52
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x52))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x61
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x61))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x62
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x62))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x71
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x71))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x72
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x72))
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
            )
        :effect
            (and
                (at end (g2))
                (at end (increase (total-cost) 1))
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
                (at end (increase (total-cost) 1))
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
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action goal5
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x51))
                (at start (x52))
            )
        :effect
            (and
                (at end (g5))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action goal6
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x61))
                (at start (x62))
            )
        :effect
            (and
                (at end (g6))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action goal7
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x71))
                (at start (x72))
            )
        :effect
            (and
                (at end (g7))
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

    (:durative-action goal3_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at end (g3))
                (at end (increase (total-cost) 200))
            )
    )

    (:durative-action goal4_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at end (g4))
                (at end (increase (total-cost) 200))
            )
    )

    (:durative-action goal5_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at end (g5))
                (at end (increase (total-cost) 200))
            )
    )

    (:durative-action goal6_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at end (g6))
                (at end (increase (total-cost) 200))
            )
    )

    (:durative-action goal7_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at end (g7))
                (at end (increase (total-cost) 200))
            )
    )
)
