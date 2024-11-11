(define (domain mail-robots)

  (:types
    robot - object
  )

  (:predicates
    (psd ?r - robot)
  )

  (:functions
    (L)
    (x ?r - robot)
    (p ?r - robot)
    (i ?r - robot)
  )

  (:action rt
    :parameters (?r - robot)
    :precondition (and
      (> (p ?r) 0)
      (< (x ?r) (* (L) (+ (i ?r) 1)))
    )
    :effect (and
      (increase (x ?r) 1)
    )
  )

  (:action lf
    :parameters (?r - robot)
    :precondition (and
      (> (p ?r) 0)
      (> (x ?r) (* (L) (i ?r)))
    )
    :effect (and
      (decrease (x ?r) 1)
    )
  )

  (:action pxc
    :parameters (?r1 ?r2 - robot)
    :precondition (and
      (= (i ?r2) (+ (i ?r1) 1))
      (= (x ?r1) (x ?r2))
      (> (+ (p ?r1)(p ?r2)) 0)
    )
    :effect (and
      (assign (p ?r1) (p ?r2))
      (assign (p ?r2) (p ?r1))
    )
  )

  (:action pst
    :parameters (?r - robot)
    :precondition (and
      (> (p ?r) 0)
    )
    :effect (and
      (psd ?r)
    )
  )

)