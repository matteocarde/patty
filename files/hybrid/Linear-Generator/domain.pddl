
(define (domain generator_linear_mt)
    ;(:requirements :fluents :durative-actions :duration-inequalities :adl :typing :time)
    (:types
        generator tank
    )

    (:predicates
        (online ?g - generator)
        (not_online ?g - generator)
        (available ?t - tank)
        (not_available ?t - tank)
        (generator-ran ?g -generator)
        (using ?t -tank)
        (block)
        (block_refuel ?g - generator ?t - tank)
        (block_generator ?g - generator)
        (closed)
        (true)

    )

    (:functions
        (fuelLevel ?g - generator)
        (capacity ?g - generator)
        (generator_running ?g -generator)
        (refuel_running ?g -generator ?t -tank)
        (generator_duration)
        (refuel_duration)
    )

    (:event min_generator_fuel
        :parameters (?g - generator)
        :precondition (and (not (>= (fuelLevel ?g) 0.0)) (not (block)))
        :effect (and (block))
    )

    (:event max_generator_fuel
        :parameters (?g - generator)
        :precondition (and (not (<= (fuelLevel ?g) (capacity ?g))) (not (block)))
        :effect (and (block))
    )

    (:event refuel_duration_block
        :parameters (?g - generator ?t -tank)
        :precondition (and (not (<= (refuel_running ?g ?t) (refuel_duration))) (not (block_refuel ?g ?t)))
        :effect (and (block_refuel ?g ?t))
    )

    (:event generator_duration_block
        :parameters (?g - generator)
        :precondition (and (not (<= (generator_running ?g) (generator_duration))) (not (block_generator ?g)))
        :effect (and (block_generator ?g))
    )

    (:process generate_power
        :parameters (?g - generator)
        :precondition (and (online ?g) (> (fuelLevel ?g) 0.0) (not (block_generator ?g)))
        :effect (and (decrease (fuelLevel ?g) (* #t 1.0))
            (increase (generator_running ?g) (* #t 1.0))
        )
    )

    (:action turn_on
        :parameters (?g - generator)
        :precondition (and (not_online ?g) (< (generator_running ?g) (generator_duration)))
        :effect (and (online ?g)
            (not (not_online ?g))
            (assign (generator_running ?g) 0 )
        )
    )

    (:process refuel_generator
        :parameters (?g - generator ?t -tank)
        :precondition (and (using ?t) (< (fuelLevel ?g) (capacity ?g))
            (< (refuel_running ?g ?t) (refuel_duration)) (not (block_refuel ?g ?t)))
        :effect (and
            (increase (fuelLevel ?g) (* #t 2.0))
            (increase (refuel_running ?g ?t) (* #t 1.0))
        )
    )

    (:action start_refueling
        :parameters (?g - generator ?t - tank)
        :precondition (and (available ?t))
        :effect (and
            (not (available ?t))
            (using ?t)
        )
    )

)