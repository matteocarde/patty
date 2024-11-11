(define (problem p_2)

  (:domain bottles)

  (:objects
    b1 b2 b3 b4 - bottle
  )

  (:init
    (= (litres b1) 0)
    (= (litres b2) 0)
    (= (litres b3) 0)
    (= (litres b4) 0)
    (= (index b1) 1)
    (= (index b2) 2)
    (= (index b3) 3)
    (= (index b4) 4)
    (= (p) 2)
    (= (on-scale) 0)
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