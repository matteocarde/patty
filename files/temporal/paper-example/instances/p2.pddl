(define (problem p_2_1)

  (:domain bottles)

  (:objects
    b1 b2 - bottle
  )

  (:init
    (= (litres b1) 5)
    (= (litres b2) 0)
    (= (index b1) 1)
    (= (index b2) 2)
    (= (p) 1)
  )

  (:goal
    (and
      (= (litres b1) 0)
    )
  )
)