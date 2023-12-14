(define (domain car_linear_mt_sc)
    ;(:requirements :fluents :durative-actions :duration-inequalities :adl :typing :time)

    (:types
        vehicle
    )

    (:predicates
        (engine_running ?v - vehicle)
        (engine_stopped ?v - vehicle)
        (engine_ok ?v - vehicle)
    )

    (:functions
        (d ?v - vehicle)
        (v ?v - vehicle)
        (a ?v - vehicle)
        (max_acceleration ?v - vehicle)
        (min_acceleration ?v - vehicle)
    )

    (:process displacement
        :parameters (?v - vehicle)
        :precondition (and (engine_running ?v))
        :effect (and(increase (d ?v) (* #t (v ?v))))
    )

    (:process moving
        :parameters (?v - vehicle)
        :precondition (and
            (engine_running ?v)
            (>= (v ?v) 0)
        )
        :effect (and
            (increase (v ?v) (* #t (a ?v))) ;; velocity changes because of the acceleration
        )
    )

    (:event engine_explosion
        :parameters (?v - vehicle)
        :precondition (and
            (> (v ?v) (max_speed ?v))
        )
        :effect (and
            (assign (v ?v) (max_speed ?v))
            (assign (a ?v) 0.0)
            (not (engine_ok ?v))
        )
    )

    (:action full-gas
        :parameters (?v - vehicle)
        :precondition (and
            (engine_running ?v)
        )
        :effect (and
            (assign (a ?v) (max_acceleration ?v))
        )
    )

    (:action keep-velocity
        :parameters (?v - vehicle)
        :precondition (and
            (engine_running ?v)
            (engine_ok ?v)
        )
        :effect (and
            (assign (a ?v) 0)
        )
    )

    (:action full-brake
        :parameters (?v - vehicle)
        :precondition (and
            (engine_running ?v)
            (engine_ok ?v)
        )
        :effect (and
            (assign (a ?v) (min_acceleration ?v))
        )
    )

    (:event idle
        :parameters (?v - vehicle)
        :precondition (and
            (engine_running ?v)
            (< (a ?v) 0)
            (<= (v ?v) 0.1)
        )
        :effect (and
            (assign (v ?v) 0.0)
            (assign (a ?v) 0.0)
        )
    )

    (:action on
        :parameters (?v - vehicle)
        :precondition (and
            (engine_stopped ?v)
            (engine_ok ?v)
        )
        :effect (and
            (engine_running ?v)
            (not (engine_stopped ?v))
        )
    )

    (:action off
        :parameters (?v - vehicle)
        :precondition (and
            (> (v ?v) -0.1)
            (< (v ?v) 0.1)
            (= (a ?v) 0.0)
            (engine_running ?v)
            (engine_ok ?v)
        )
        :effect (and
            (assign (v ?v) 0.0)
            (engine_stopped ?v)
            (not (engine_running ?v))
        )

    )
)