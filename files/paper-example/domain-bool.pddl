
(define (domain paper)

  (:predicates
    (done)

  )

  (:functions
    (x)
  )
  

  (:action sum
    :parameters ()
    :precondition ()
    :effect (and
      (increase (x) 1)
    )
  )

  (:action check
    :parameters ()
    :precondition (and
      (>= (x) 10)
    )
    :effect (and
      (done)
    )
  )
  

)