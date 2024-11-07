(define (domain bottles)
  (:requirements :fluents :equality :typing :durative-actions)

  (:types
    bottle - obj
    bottleleft bottleright - bottle
  )

  (:functions
    (litres ?a - bottle)
  )

  (:durative-action pour
    :parameters (?a - bottleleft ?b - bottleright)
    :duration (= ?duration 1)
    :condition (and
      (at start (> (litres ?a) 0))
    )
    :effect (and
      (at start (decrease (litres ?a) 1))
      (at end (increase (litres ?b) 1))
    )
  )

)