(define (domain stackworld)
  (:requirements :strips :equality)
  (:types
    card - object
    first last - card
    movable - card
  )
  (:predicates
    (on-top ?a - card ?b - card)
  )

  (:action rotate
    :parameters ()
    :precondition ()
    :effect(and
      (forall
        (?f - first ?a - movable ?b - movable ?c - movable ?l - last)
        (when
          (and
            (not (= ?a ?b))
            (on-top ?f ?a)
            (on-top ?c ?l)
            (on-top ?a ?b)
          )
          (and
            (not (on-top ?a ?b))
            (on-top ?a ?l)
            (not (on-top ?c ?l))
            (on-top ?c ?a)
            (not (on-top ?f ?a))
            (on-top ?f ?b)
          )
        )
      )
    )
  )



)