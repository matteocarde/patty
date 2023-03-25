
(define (domain paper)

  (:functions
    (x)
    (y)
  )

  (:action a
    :parameters ()
    :precondition (and
      (>= (x) 4)
    )
    :effect (and
      (increase (x) 5)
      (assign (y) 4)
    )
  )

  (:action b
    :parameters ()
    :precondition ()
    :effect (and
      (decrease (x) 3)
      (increase (y) 6)
    )
  )

)