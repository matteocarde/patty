(define (domain bottles)
  (:requirements :fluents :equality :typing :durative-actions)

  (:types
    bottle
  )

  (:predicates
    (capped ?a - bottle)
    (packed ?a - bottle)
    (packing)
  )

  (:functions
    (litres ?a - bottle)
    (index ?a - bottle)
    (p)
    (on-scale)
  )

  ; Case 1) Pour must start and end between uncap-cap 
  ; Case 2) Shake must start before and end inside cap-uncap (Third figure of cushing)
  ; Case 3) Two pack must end always at the same time (Figure a and b)

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

  (:durative-action uncap-cap
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
    :parameters (?a - bottle ?b - bottle)
    :duration (= ?duration 1)
    :condition (and
      (at start (> (index ?b) (p)))
      (at start (<= (index ?a) (p)))
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

  (:durative-action shake
    :parameters (?a - bottle)
    :duration (= ?duration 4)
    :condition (and
      (at start (> (index ?a) (p)))
      (at start (capped ?a))
      (at end (not (capped ?a)))
    )
    :effect (and
      (at end (assign (litres ?a) 0))
    )
  )

  (:durative-action pack
    :parameters (?a - bottle)
    :duration (= ?duration 3)
    :condition (and
      (at start (not (packed ?a)))
      (at start (< (on-scale) 2))
      (at end (= (on-scale) 2))
    )
    :effect (and
      (at start (packing))
      (at start (increase (on-scale) 1))
      (at end (packed ?a))
      (at end (not (packing)))
    )
  )
  (:action clear-scale
    :parameters ()
    :precondition (and
      (not (packing))
    )
    :effect (and
      (assign (on-scale) 0)
    )
  )

)