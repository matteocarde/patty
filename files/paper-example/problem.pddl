(define (problem small)
  (:domain paper)
  (:objects)
  (:init
    (= (x) 6)
    (= (y) 1)
  )
  (:goal
    (and
      (>= (x) 12)
      (>= (y) 9)
    )
  )
)