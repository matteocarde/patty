(define (domain car_linear_mt_sc)
    ;(:requirements :fluents :durative-actions :duration-inequalities :adl :typing :time)
    (:predicates
        (alwaysfalse)
        (edge)
        (engine_running)
        (engine_stopped)
    )

    (:functions
        (ck)
        (delta)
        (tk)
        (d)
        (v)
        (a)
        (max_acceleration)
        (min_acceleration)
        (max_speed)
    )

    (:event tic
        :parameters ()
        :precondition (and
            (= (ck) (+ (tk) #t))
        )
        :effect (and
            (assign (tk) (- (+ (ck) (delta)) #t))
        )
    )

    (:process ticking
        :parameters ()
        :precondition (or
            (engine_running)
        )
        :effect (and
            (increase (ck) (* #t 1.0))
        )
    )

    (:process displacement
        :parameters ()
        :precondition (engine_running)
        :effect (and(increase (d) (* #t (v))))
    )

    (:process moving
        :parameters ()
        :precondition (engine_running)
        :effect (and
            (increase (v) (* #t (a))) ;; velocity changes because of the acceleration
        )
    )

    (:event idle
        :parameters ()
        :precondition (and
            (engine_running)
            (< (a) 0)
            (<= (v) 0.1)
        )
        :effect (and
            (assign (v) 0.0)
            (assign (a) 0.0)
        )
    )

    (:action accelerate
        :parameters ()
        :precondition (and
            (= (ck) (tk))
            (< (a) (max_acceleration))
            (engine_running)
        )
        :effect (and(increase (a) 1.0))
    )

    (:action stop_car
        :parameters ()
        :precondition (and
            (= (ck) (tk))
            (< (v) 0.1)
            (= (a) 0.0)
            (engine_running)
        )
        :effect (and
            (assign (v) 0.0)
            (engine_stopped)
            (not (engine_running))
        )

    )

    (:action start_car
        :parameters ()
        :precondition (and
            (= (ck) (tk))
            (engine_stopped)
        )
        :effect (and
            (engine_running)
            (not (engine_stopped))
        )
    )

    (:action decelerate
        :parameters ()
        :precondition (and
            (= (ck) (tk))
            (> (a) (min_acceleration))
            (engine_running)
        )
        :effect (and(decrease (a) 1.0))
    )
)