(define (domain optional_goals_2_10)
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
        (x81)
        (x82)
        (x91)
        (x92)
        (x101)
        (x102)
        (y)
        (g1)
        (g2)
        (g3)
        (g4)
        (g5)
        (g6)
        (g7)
        (g8)
        (g9)
        (g10)
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

    (:durative-action set_x51
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x51))
                (at end (x51))
            )
    )

    (:durative-action set_x52
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x52))
                (at end (x52))
            )
    )

    (:durative-action set_x61
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x61))
                (at end (x61))
            )
    )

    (:durative-action set_x62
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x62))
                (at end (x62))
            )
    )

    (:durative-action set_x71
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x71))
                (at end (x71))
            )
    )

    (:durative-action set_x72
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x72))
                (at end (x72))
            )
    )

    (:durative-action set_x81
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x81))
                (at end (x81))
            )
    )

    (:durative-action set_x82
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x82))
                (at end (x82))
            )
    )

    (:durative-action set_x91
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x91))
                (at end (x91))
            )
    )

    (:durative-action set_x92
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x92))
                (at end (x92))
            )
    )

    (:durative-action set_x101
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x101))
                (at end (x101))
            )
    )

    (:durative-action set_x102
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x102))
                (at end (x102))
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
            )
    )

    (:durative-action goal8
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x81))
                (at start (x82))
            )
        :effect
            (and
                (at end (g8))
            )
    )

    (:durative-action goal9
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x91))
                (at start (x92))
            )
        :effect
            (and
                (at end (g9))
            )
    )

    (:durative-action goal10
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x101))
                (at start (x102))
            )
        :effect
            (and
                (at end (g10))
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

    (:durative-action goal5_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (g5))
                (at end (g5))
            )
    )

    (:durative-action goal6_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (g6))
                (at end (g6))
            )
    )

    (:durative-action goal7_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (g7))
                (at end (g7))
            )
    )

    (:durative-action goal8_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (g8))
                (at end (g8))
            )
    )

    (:durative-action goal9_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (g9))
                (at end (g9))
            )
    )

    (:durative-action goal10_fake
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (g10))
                (at end (g10))
            )
    )
)
