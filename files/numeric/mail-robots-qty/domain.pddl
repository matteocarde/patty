(define (domain mail-robots)

  (:types
    robot letter - object
  )

  (:predicates
    (psd ?r - robot ?l - letter)
    (next ?a - robot ?b - robot)
  )

  (:functions
    (L)
    (x ?r - robot)
    (p ?r - robot ?l - letter)
    (h ?r - robot)
    (i ?r - robot)
  )

  (:action rt
    :parameters (?r - robot)
    :precondition (and
      (> (h ?r) 0)
      (< (x ?r) (* (L) (+ (i ?r) 1)))
    )
    :effect (and
      (increase (x ?r) 1)
    )
  )

  (:action lf
    :parameters (?r - robot)
    :precondition (and
      (> (h ?r) 0)
      (> (x ?r) (* (L) (i ?r)))
    )
    :effect (and
      (decrease (x ?r) 1)
    )
  )

  (:action pxc
    :parameters (?r1 ?r2 - robot ?l - letter)
    :precondition (and
      (next ?r1 ?r2)
      (= (x ?r1) (x ?r2))
      (> (+ (p ?r1 ?l)(p ?r2 ?l)) 0)
    )
    :effect (and
      (assign (p ?r1 ?l) (p ?r2 ?l))
      (assign (p ?r2 ?l) (p ?r1 ?l))
      (increase (h ?r2) (- (p ?r1 ?l)(p ?r2 ?l)))
      (increase (h ?r1) (- (p ?r2 ?l)(p ?r1 ?l)))
    )
  )

  (:action pst
    :parameters (?r - robot ?l - letter)
    :precondition (and
      (> (p ?r ?l) 0)
    )
    :effect (and
      (psd ?r ?l)
    )
  )

)