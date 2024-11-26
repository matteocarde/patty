(define (domain dig)
  (:requirements :strips :equality )
  (:types
    element
  )
  (:predicates
    (have ?e - element)
    (combination ?a - element ?b - element ?c - element)
  )

  (:action alchemy
    :parameters ()
    :precondition()
    :effect(and
      (forall
        (?a - element ?b - element ?c - element)
        (when
          (and
            (combination ?a ?b ?c)
            (have ?a)
            (have ?b)
          )
          (and
            (have ?c)
          )
        )
      )
    )
  )
)