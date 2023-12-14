(define (domain car_linear_mt_sc)

    (:types
        car
    )

    (:predicates
        (engine_running ?c - car)
        (engine_stopped ?c - car)
        (crash_happened)
        (overtaking ?c - car)
    )

    (:functions
        (d ?c)
        (v ?c)
        (a ?c)
        (max_acceleration)
        (min_acceleration)
        (max_speed)
    )

    (:process displacement
        :parameters (?c - car)
        :precondition (engine_running ?c)
        :effect (increase (d ?c) (* #t (v ?c)))
    )

    (:process moving
        :parameters (?c - car)
        :precondition (engine_running ?c)
        :effect (and
            (increase (v ?c) (* #t (a ?c))) ;; velocity changes because of the acceleration
        )
    )
    (:event idle
        :parameters (?c - car)
        :precondition (and
            (engine_running ?c)
            (< (a ?c) 0)
            (<= (v ?c) 0.1)
        )
        :effect (and
            (assign (v ?c) 0.0)
            (assign (a ?c) 0.0)
        )
    )

    (:action accelerate
        :parameters (?c - car)
        :precondition (and (< (a ?c) (max_acceleration)) (engine_running ?c))
        :effect (increase (a ?c) 1.0) ;;
    )

    (:action stop_car
        :parameters (?c - car)
        :precondition (and (> (v ?c) -0.1)
            (< (v ?c) 0.1) (= (a ?c) 0.0) (engine_running ?c))
        :effect (and
            (assign (v ?c) 0.0)
            (engine_stopped ?c)
            (not (engine_running ?c))
        )

    )

    (:action overtake
        :parameters (?c - car)
        :precondition (and (> (v ?c) 0.0) (not (overtaking ?c)))
        :effect (and (overtaking ?c))
    )

    (:action not_overtake
        :parameters (?c - car)
        :precondition (and (> (v ?c) 0.0) (overtaking ?c))
        :effect (and (not (overtaking ?c)))
    )

    (:action start_car
        :parameters (?c - car)
        :precondition (engine_stopped ?c)
        :effect (and
            (engine_running ?c)
            (not (engine_stopped ?c))
        )
    )

    (:action decelerate
        :parameters (?c - car)
        :precondition (and (> (a ?c) (min_acceleration)) (engine_running ?c))
        :effect (decrease (a ?c) 1.0) ;;
    )

    (:event crash_1
        :parameters (?c1 - car ?c2 - car)
        :precondition (and
            (not (crash_happened))
            (< (- (d ?c1) (d ?c2)) (max_speed))
            (> (- (d ?c1) (d ?c2)) 0)
            (not (overtaking ?c1))
            (not (overtaking ?c2))
        )
        :effect (crash_happened)
    )

    (:event crash_2
        :parameters (?c1 - car ?c2 - car)
        :precondition (and
            (not (crash_happened))
            (< (- (d ?c1) (d ?c2)) (max_speed))
            (> (- (d ?c1) (d ?c2)) 0)
            (overtaking ?c1)
            (overtaking ?c2)
        )
        :effect (crash_happened)
    )

)