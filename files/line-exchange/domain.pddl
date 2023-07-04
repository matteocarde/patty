
(define (domain line-exchange)

  (:types
    robot - object
  )

  (:predicates
    (pd ?r1 - robot ?r2 - robot)
    (ps ?r - robot)
    (next ?r1 ?r2 - robot)
  )

  (:functions
    (D)
    (i ?r - robot)
    (x ?r - robot)
    (q ?r - robot)
    (e ?r1 - robot ?r2 - robot)
  )

  (:action lft
    :parameters (?r - robot)
    :precondition (and
      (not (ps ?r))
      (> (x ?r) (* (D) (i ?r)))
    )
    :effect (and
      (decrease (x ?r) 1)
    )
  )

  (:action rgt
    :parameters (?r - robot)
    :precondition (and
      (not (ps ?r))
      (< (x ?r) (* (D) (+ (i ?r) 1)))
    )
    :effect (and
      (increase (x ?r) 1)
    )
  )

  (:action conn
    :parameters (?r1 ?r2 - robot)
    :precondition (and
      (next ?r1 ?r2)
      (= (x ?r1) (x ?r2))
    )
    :effect (and
      (ps ?r1)
      (ps ?r2)
      (pd ?r1 ?r2)
    )
  )

  (:action disc
    :parameters (?r1 ?r2 - robot)
    :precondition (and
      (pd ?r1 ?r2)
      (next ?r1 ?r2)
    )
    :effect (and
      (not (ps ?r1))
      (not (ps ?r2))
      (not (pd ?r1 ?r2))
    )
  )

  (:action exch
    :parameters (?r1 ?r2 - robot)
    :precondition (and
      (next ?r1 ?r2)
      (pd ?r1 ?r2)
      (>= (q ?r1) (e ?r1 ?r2))
      (>= (q ?r2) (* -1 (e ?r1 ?r2)))
    )
    :effect (and
      (decrease (q ?r1) (e ?r1 ?r2))
      (increase (q ?r2) (e ?r1 ?r2))
    )
  )

  (:action lre
    :parameters (?r1 ?r2 - robot)
    :precondition (and
      (next ?r1 ?r2)
    )
    :effect (and
      (assign (e ?r1 ?r2) 1)
    )
  )

  (:action rle
    :parameters (?r1 ?r2 - robot)
    :precondition (and
      (next ?r1 ?r2)
    )
    :effect (and
      (assign (e ?r1 ?r2) -1)
    )
  )

)