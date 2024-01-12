(define (domain bottles)
  (:requirements :fluents :equality :typing :durative-actions)

  (:types
    bottle - obj
    bottleleft bottleright - bottle
  )

  (:predicates
    (capped ?a - bottle)
  )

  (:functions
    (litres ?a - bottle)
  )

  (:durative-action ncap-cap
    :parameters (?a - bottle)
    :duration (= ?duration 5)
    :condition (and
      (at start (capped ?a))
      (at end (not (capped ?a)))
    )
    :effect (and
      (at end (capped ?a))
      (at start (not (capped ?a)))
    )
  )

  (:durative-action pour
    :parameters (?a - bottleleft ?b - bottleright)
    :duration (= ?duration 1)
    :condition (and
      (at start (> (litres ?a) 0))
      (at start (not (capped ?a)))
      (at start (not (capped ?b)))
      (over all (not (capped ?a)))
      (over all (not (capped ?b)))
    )
    :effect (and
      (at start (decrease (litres ?a) 1))
      (at end (increase (litres ?b) 1))
    )
  )

)