(define (problem pb01)
  (:domain counter)

  (:init
    (x1)
    (x2)
    (x5)
    (x6)
    (x7)
  )
  (:goal
    (and (x1)(x2)
      (not (x3))(x4)(x5)(x6)(x7))
  )
)