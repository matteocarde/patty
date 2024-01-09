(define (problem p_2)

  (:domain bottles)

  (:objects
    b1 - bottleleft
    b2 - bottleright
  )

  (:init
    (= (litres b1) 5)
    (= (litres b2) 0)
    (capped b1)
    (capped b2)
    (= (on-scale) 0)
  )

  (:goal
    (and
      (= (litres b1) 0)
      (= (litres b2) 5)
    )
  )
)