
(define (domain side-exchange)

  (:types
    color robot
  )

  (:predicates
    (holding)
    (holding ?c - color)
    (edge ?r - robot)
    (next ?a - robot ?b - robot)
  )

  (:functions
    (q ?r - robot)
    (b ?e - robot ?c - color)
  )

  (:action exch
    :parameters (?r1 ?r2 - robot)
    :precondition (and
      (next ?r1 ?r2)
      (= (+ (q ?r2) (q ?r1)) 1)
    )
    :effect (and
      (increase (q ?r1) (- (q ?r2) (q ?r1)))
      (increase (q ?r2) (- (q ?r1) (q ?r2)))
    )
  )

  (:action pop
    :parameters (?e - robot ?c - color)
    :precondition (and
      (edge ?e)
      (not (holding))
      (> (b ?e ?c) 0)
    )
    :effect (and
      (holding)
      (holding ?c)
      (assign (q ?e) 1)
      (decrease (b ?e ?c) 1)
    )
  )

  (:action put
    :parameters (?e - robot ?c - color)
    :precondition (and
      (edge ?e)
      (holding ?c)
      (= (q ?e) 1)
    )
    :effect (and
      (not (holding))
      (not (holding ?c))
      (assign (q ?e) 0)
      (increase (b ?e ?c) 1)
    )

  )
)