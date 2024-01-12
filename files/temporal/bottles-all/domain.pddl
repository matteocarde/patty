(define (domain bottles-all)
  (:requirements :fluents :equality :typing :durative-actions)

  (:types
    bottle - obj
    bottleleft bottleright - bottle
  )

  (:predicates
    (packed ?a - bottle)
    (packing ?a - bottle)
    (is-packing)
    (capped ?a - bottle)
  )

  (:functions
    (on-platform)
    (litres ?a - bottle)
  )

  (:durative-action cap-uncap
    :parameters (?a - bottle)
    :duration (= ?duration 5)
    :condition (and
      (at start (not (capped ?a)))
      (at start (not (packed ?a)))
      (at end (capped ?a))
    )
    :effect (and
      (at start (capped ?a))
      (at end (not (capped ?a)))
    )
  )

  (:durative-action ncap-cap
    :parameters (?a - bottle)
    :duration (= ?duration 5)
    :condition (and
      (at start (capped ?a))
      (at start (not (packed ?a)))
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
      (at start (not (packed ?a)))
      (at start (not (packed ?b)))
      (over all (not (capped ?a)))
      (over all (not (capped ?b)))
    )
    :effect (and
      (at start (decrease (litres ?a) 1))
      (at end (increase (litres ?b) 1))
    )
  )

  (:durative-action shake
    :parameters (?a - bottleright)
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

  (:durative-action zpack
    :parameters (?a - bottle)
    :duration (= ?duration 3)
    :condition (and
      (at start (not (packed ?a)))
      (at start (not (packing ?a)))
      (at start (< (on-platform) 2))
      (at start (capped ?a))
      (over all (capped ?a))
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