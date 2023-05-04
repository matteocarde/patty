; Now the elevator has both capacity and weight restrictions

(define (domain elevator)
  (:requirements :strips :typing)
  (:types
    person elevator
  )
  (:predicates
    (reached ?p - person)
    (in ?e - elevator ?p - person)
  )
  (:functions
    (at-elevator ?e - elevator)
    (at-person ?p - person)
    (target ?p - person)
    (weight ?p - person)
    (capacity ?e - elevator)
    (max-load ?e - elevator)
    (passengers ?e - elevator)
    (load ?e - elevator)

    (floors)
  )

  (:action move-up
    :parameters (?e - elevator)
    :precondition (and
      (< (at-elevator ?e) (floors))
    )
    :effect (and
      (increase (at-elevator ?e) 1)
    )
  )

  (:action move-down
    :parameters (?e - elevator)
    :precondition (and
      (> (at-elevator ?e) 0)
    )
    :effect (and
      (decrease (at-elevator ?e) 1)
    )
  )

  (:action load
    :parameters (?p - person ?e - elevator)
    :precondition (and
      (= (at-person ?p) (at-elevator ?e))
      (<= (+ (passengers ?e) 1) (capacity ?e))
      (<= (+ (load ?e) (weight ?p)) (max-load ?e)) ;Now the weight is restricted
    )
    :effect (and
      (in ?e ?p)
      (assign (at-person ?p) -1)
      (increase (passengers ?e) 1)
      (increase (load ?e) (weight ?p)) ;The weight is added when a passengers enters 
    )
  )

  (:action unload
    :parameters (?p - person ?e - elevator)
    :precondition (and
      (in ?e ?p)
    )
    :effect (and
      (not (in ?e ?p))
      (assign (at-person ?p) (at-elevator ?e))
      (decrease (passengers ?e) 1)
      (decrease (load ?e) (weight ?p)) ;The weight is removed when a passengers exits 
    )
  )

  (:action reached
    :parameters (?p - person)
    :precondition (and
      (= (at-person ?p) (target ?p))
      (not (reached ?p))
    )
    :effect (and
      (reached ?p)
    )
  )

)