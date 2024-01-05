(define (domain bottles)
  (:requirements :durative-actions :typing :fluents)

  (:types
    bottle
  )

  (:predicates
    (capped ?a - bottle)
  )

  (:functions
    (index ?a - bottle)
    (p)
    (litres ?a - bottle)
  )

  (:durative-action pour
    :parameters (?a - bottle ?b - bottle)
    :duration (= ?duration 1)
    :condition (and
      (at start (<= (index ?a) (p)))
      (at start (> (index ?b) (p)))
      (at start (> (litres ?a) 0))
      (at start (not (capped ?b)))
      (over all (not (capped ?b)))
    )
    :effect (and
      (at start (decrease (litres ?a) 1))
      (at end (increase (litres ?b) 1))
    )
  )

  (:action cap
    :parameters (?a - bottle)
    :precondition (and
      (> (index ?a) (p))
      (not (capped ?a))
    )
    :effect (and
      (capped ?a)
    )
  )

  (:action uncap
    :parameters (?a - bottle)
    :precondition (and
      (> (index ?a) (p))
      (capped ?a)
    )
    :effect (and
      (not (capped ?a))
    )
  )

)