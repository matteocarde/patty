(define (domain elevator)
  (:requirements :strips :typing)
  (:types
    floor person elevator
  )
  (:predicates
    (at-person ?p - person ?f - floor)
    (target ?p - person ?f - floor)
    (reached ?p - person)
    (in ?e - elevator ?p - person)
    (above ?f2 - floor ?f1 - floor)
    (at-elevator ?e - elevator ?f - floor)
  )

  (:action move-up
    :parameters (?e - elevator ?f1 - floor ?f2 - floor)
    :precondition (and
      (at-elevator ?e ?f1)
      (above ?f2 ?f1)
    )
    :effect (and
      (not (at-elevator ?e ?f1))
      (at-elevator ?e ?f2)
    )
  )

  (:action move-down
    :parameters (?e - elevator ?f2 - floor ?f1 - floor)
    :precondition (and
      (at-elevator ?e ?f2)
      (above ?f2 ?f1)
    )
    :effect (and
      (not (at-elevator ?e ?f2))
      (at-elevator ?e ?f1)
    )
  )

  (:action load
    :parameters (?p - person ?e - elevator ?f - floor)
    :precondition (and
      (at-person ?p ?f)
      (at-elevator ?e ?f)
    )
    :effect (and
      (in ?e ?p)
      (not (at-person ?p ?f))
    )
  )

  (:action unload
    :parameters (?p - person ?e - elevator ?f - floor)
    :precondition (and
      (in ?e ?p)
      (at-elevator ?e ?f)
    )
    :effect (and
      (not (in ?e ?p))
      (at-person ?p ?f)
    )
  )

  (:action reached
    :parameters (?p - person ?f - floor)
    :precondition (and
      (at-person ?p ?f)
      (target ?p ?f)
      (not (reached ?p))
    )
    :effect (and
      (reached ?p)
    )
  )

)