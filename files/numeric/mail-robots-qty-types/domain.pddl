(define (domain mail-robots)

  (:types
    robot letter - object
    green yellow - letter
  )

  (:predicates
    (gsd ?r - robot ?l - green)
    (ysd ?r - robot ?l - yellow)
    (next ?a - robot ?b - robot)
  )

  (:functions
    (L)
    (x ?r - robot)
    (g ?r - robot ?l - green)
    (y ?r - robot ?l - yellow)
    (hg ?r - robot)
    (hy ?r - robot)
    (i ?r - robot)
  )

  (:action rt
    :parameters (?r - robot)
    :precondition (and
      (> (+ (hg ?r)(hy ?r)) 0)
      (< (x ?r) (* (L) (+ (i ?r) 1)))
    )
    :effect (and
      (increase (x ?r) 1)
    )
  )

  (:action lf
    :parameters (?r - robot)
    :precondition (and
      (> (+ (hg ?r)(hy ?r)) 0)
      (> (x ?r) (* (L) (i ?r)))
    )
    :effect (and
      (decrease (x ?r) 1)
    )
  )

  (:action gxc
    :parameters (?r1 ?r2 - robot ?l - green)
    :precondition (and
      (next ?r1 ?r2)
      (= (x ?r1) (x ?r2))
      (> (+ (g ?r1 ?l)(g ?r2 ?l)) 0)
    )
    :effect (and
      (assign (g ?r1 ?l) (g ?r2 ?l))
      (assign (g ?r2 ?l) (g ?r1 ?l))
      (increase (hg ?r2) (- (g ?r1 ?l)(g ?r2 ?l)))
      (increase (hg ?r1) (- (g ?r2 ?l)(g ?r1 ?l)))
    )
  )

  (:action yxc
    :parameters (?r1 ?r2 - robot ?l - yellow)
    :precondition (and
      (next ?r1 ?r2)
      (= (x ?r1) (x ?r2))
      (> (+ (y ?r1 ?l)(y ?r2 ?l)) 0)
    )
    :effect (and
      (assign (y ?r1 ?l) (y ?r2 ?l))
      (assign (y ?r2 ?l) (y ?r1 ?l))
      (increase (hy ?r2) (- (y ?r1 ?l)(y ?r2 ?l)))
      (increase (hy ?r1) (- (y ?r2 ?l)(y ?r1 ?l)))
    )
  )

  (:action gst
    :parameters (?r - robot ?l - green)
    :precondition (and
      (> (g ?r ?l) 0)
    )
    :effect (and
      (gsd ?r ?l)
    )
  )

  (:action yst
    :parameters (?r - robot ?l - yellow)
    :precondition (and
      (> (y ?r ?l) 0)
    )
    :effect (and
      (ysd ?r ?l)
    )
  )

)