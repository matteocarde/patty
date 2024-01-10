(define (domain pack)
  (:requirements :fluents :equality :typing :durative-actions)

  (:types
    bottle - obj
  )

  (:predicates
    (packed ?a - bottle)
    (packing ?a - bottle)
    (is-packing)
  )

  (:functions
    (on-platform)
  )

  (:durative-action pack
    :parameters (?a - bottle)
    :duration (= ?duration 3)
    :condition (and
      (at start (not (packed ?a)))
      (at start (not (packing ?a)))
      (at start (< (on-platform) 2))
      (at end (= (on-platform) 2))
    )
    :effect (and
      (at start (is-packing))
      (at start (packing ?a))
      (at start (increase (on-platform) 1))
      (at end (packed ?a))
      (at end (not (is-packing)))
    )
  )

  (:action clear-platform
    :parameters ()
    :precondition (and
      (not (is-packing))
    )
    :effect (and
      (assign (on-platform) 0)
    )
  )

)