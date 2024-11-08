(define (problem p_2)

  (:domain bottles)

  (:objects
    b1 b2 - bottleleft
    b3 b4 - bottleright
  )

  (:init
    (= (litres b1) 5)
    (= (litres b2) 5)
    (= (litres b3) 0)
    (= (litres b4) 0)
    (capped b1)
    (capped b2)
    (capped b3)
    (capped b4)
    (= (on-scale) 0)
  )

  (:goal
    (and
      (= (litres b1) 0)
      (= (litres b2) 0)
      (= (litres b3) 5)
      (= (litres b4) 5)
    )
  )
)