(define (domain shake)
  (:requirements :fluents :equality :typing :durative-actions)

  (:types
    bottle - obj
  )

  (:predicates
    (capped ?a - bottle)
  )

  (:functions
    (litres ?a - bottle)
  )

  (:durative-action cap-uncap
    :parameters (?a - bottle)
    :duration (= ?duration 5)
    :condition (and
      (at start (not (capped ?a)))
      (at end (capped ?a))
    )
    :effect (and
      (at start (capped ?a))
      (at end (not (capped ?a)))
    )
  )

  (:durative-action shake
    :parameters (?a - bottle)
    :duration (= ?duration 5)
    :condition (and
      (at start (> (litres ?a) 0))
      (at start (capped ?a))
      (at end (not (capped ?a)))
    )
    :effect (and
      (at end (assign (litres ?a) 0))
    )
  )

)