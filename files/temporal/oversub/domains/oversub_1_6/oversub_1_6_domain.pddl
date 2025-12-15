(define (domain optional_goals_1_6)
    (:requirements :fluents :equality :typing :durative-actions :action-costs)

    (:predicates
        (x1)
        (x2)
        (x3)
        (x4)
        (x5)
        (x6)
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

    (:durative-action set_x3
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x3))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x4
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x4))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x5
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x5))
                (at end (increase (total-cost) 1))
            )
    )

    (:durative-action set_x6
        :parameters ()
        :duration (= ?duration 1)
        :effect
            (and
                (at start (x6))
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

    (:durative-action goal3
        :parameters ()
        :duration (= ?duration 1)
        :condition
            (and
                (at start (x3))
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
                (at start (x4))
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
                (at start (x5))
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
                (at start (x6))
            )
        :effect
            (and
                (at end (g6))
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
)
