(define (problem p_2_1)

  (:domain bottles)

  (:objects
    b1 b2 b3 - bottle
  )

  (:init
    (= (litres b1) 5)
    (= (litres b2) 0)
    (= (litres b3) 0)
    (= (index b1) 1)
    (= (index b2) 2)
    (= (index b3) 3)
    (= (p) 1)
    (capped b2)
    (capped b3)
  )

  (:goal
    (and
      (= (litres b2) 2)
      (= (litres b3) 3)
      (capped b2)
      (capped b3)
    )
  )
)