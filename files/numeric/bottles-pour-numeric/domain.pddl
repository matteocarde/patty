(define (domain bottles)
  (:requirements :fluents :equality :typing :durative-actions)

  (:types
    bottle - obj
    bottleleft bottleright - bottle
  )

  (:functions
    (litres ?a - bottle)
  )

  (:action pour
    :parameters (?a - bottleleft ?b - bottleright)
    :precondition (and
      (> (litres ?a) 0)
    )
    :effect (and
      (decrease (litres ?a) 1)
      (increase (litres ?b) 1)
    )
  )

)