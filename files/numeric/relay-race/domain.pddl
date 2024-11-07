(define (domain relay-race)

  (:types
    runner baton
  )

  (:predicates
    (td ?r - runner ?b - baton)
    (next ?a ?b - runner)
  )

  (:functions
    (L)
    (x ?r - runner)
    (b ?r - runner ?b - baton)
    (h ?r - runner)
    (i ?r - runner)
  )

  (:action fw
    :parameters (?r - runner)
    :precondition (and
      (< (x ?r) (* (L) (+ (i ?r) 1)))
      (> (h ?r) 0)
    )
    :effect (and
      (increase (x ?r) 1)
    )
  )

  (:action bw
    :parameters (?r - runner)
    :precondition (and
      (> (x ?r) (* (L) (i ?r)))
      (> (h ?r) 0)
    )
    :effect (and
      (decrease (x ?r) 1)
    )
  )

  (:action xc
    :parameters (?r1 ?r2 - runner ?b - baton)
    :precondition (and
      (next ?r1 ?r2)
      (= (x ?r1) (x ?r2))
      (> (+ (b ?r1 ?b)(b ?r2 ?b)) 0)
    )
    :effect (and
      (assign (b ?r1 ?b) (b ?r2 ?b))
      (assign (b ?r2 ?b) (b ?r1 ?b))
      (increase (h ?r2) (- (b ?r1 ?b)(b ?r2 ?b)))
      (increase (h ?r1) (- (b ?r2 ?b)(b ?r1 ?b)))
      (td ?r2 ?b)
    )
  )

)