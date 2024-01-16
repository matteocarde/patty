
(define (domain mailrobot)

  (:types
    robot letter
  )

  (:predicates
    (stamped ?l - letter)
    (signed ?l - letter)
    (canStamp ?r - robot)
    (canSign ?l - letter ?r - robot)
    (hasLetter ?l - letter ?r - robot)
  )

  (:functions
    (L)
    (x ?r - robot)
    (i ?r - robot)
  )

  (:action left
    :parameters (?r - robot)
    :precondition (and
      (> (x ?r) (* (L) (i ?r)))
    )
    :effect (and
      (decrease (x ?r) 1)
    )
  )

  (:action right
    :parameters (?r - robot)
    :precondition (and
      (< (x ?r) (* (L) (+ (i ?r) 1)))
    )
    :effect (and
      (increase (x ?r) 1)
    )
  )

  (:action exchange
    :parameters (?r1 ?r2 - robot ?l - letter)
    :precondition (and
      (= (x ?r1) (x ?r2))
      (hasLetter ?l ?r1)
    )
    :effect (and
      (hasLetter ?l ?r2)
      (not (hasLetter ?l ?r1))
    )
  )

  (:action stamp
    :parameters (?r - robot ?l - letter)
    :precondition (and
      (canStamp ?r)
      (hasLetter ?l ?r)
    )
    :effect (and
      (stamped ?l)
    )
  )

  (:action sign
    :parameters (?r - robot ?l - letter)
    :precondition (and
      (= (x ?r) (* (L) (i ?r)))
      (canSign ?l ?r)
      (hasLetter ?l ?r)
      (stamped ?l)
    )
    :effect (and
      (signed ?l)
    )
  )

)