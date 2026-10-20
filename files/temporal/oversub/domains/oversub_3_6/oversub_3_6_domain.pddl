(define (domain optional_goals_3_6)
    (:requirements :fluents :equality :typing :durative-actions :action-costs)

    (:predicates
        (x11)
        (x12)
        (x13)
        (x21)
        (x22)
        (x23)
        (x31)
        (x32)
        (x33)
        (x41)
        (x42)
        (x43)
        (x51)
        (x52)
        (x53)
        (x61)
        (x62)
        (x63)
        (y)
        (g1)
        (g2)
        (g3)
        (g4)
        (g5)
        (g6)
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
            )
    )

    (:durative-action set_x12
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x12))
            )
    )

    (:durative-action set_x13
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x13))
            )
    )

    (:durative-action set_x21
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x21))
            )
    )

    (:durative-action set_x22
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x22))
            )
    )

    (:durative-action set_x23
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x23))
            )
    )

    (:durative-action set_x31
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x31))
            )
    )

    (:durative-action set_x32
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x32))
            )
    )

    (:durative-action set_x33
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x33))
            )
    )

    (:durative-action set_x41
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x41))
            )
    )

    (:durative-action set_x42
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x42))
            )
    )

    (:durative-action set_x43
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x43))
            )
    )

    (:durative-action set_x51
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x51))
            )
    )

    (:durative-action set_x52
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x52))
            )
    )

    (:durative-action set_x53
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x53))
            )
    )

    (:durative-action set_x61
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x61))
            )
    )

    (:durative-action set_x62
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x62))
            )
    )

    (:durative-action set_x63
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x63))
            )
    )

    (:durative-action set_y
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (y))
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
            )
    )

    (:durative-action goal3
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x31))
                (at start (x32))
                (at start (x33))
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
                (at start (x43))
            )
        :effect
            (and
                (at end (g4))
            )
    )

    (:durative-action goal5
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x51))
                (at start (x52))
                (at start (x53))
            )
        :effect
            (and
                (at end (g5))
            )
    )

    (:durative-action goal6
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x61))
                (at start (x62))
                (at start (x63))
            )
        :effect
            (and
                (at end (g6))
            )
    )

    (:durative-action goal1_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at end (g1))
            )
    )

    (:durative-action goal2_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at end (g2))
            )
    )

    (:durative-action goal3_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at end (g3))
            )
    )

    (:durative-action goal4_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at end (g4))
            )
    )

    (:durative-action goal5_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at end (g5))
            )
    )

    (:durative-action goal6_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at end (g6))
            )
    )
)
