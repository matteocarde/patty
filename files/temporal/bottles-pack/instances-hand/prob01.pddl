(define (problem prob_1)
  (:domain pack)
  (:objects
    b1 b2 b3 b4 - bottle
  )
  (:init
    (= (on-platform) 0)
  )
  (:goal
    (and
      (packed b1)
      (packed b2)
      (packed b3)
      (packed b4)
    )
  )
)