(define (problem p_2)

  (:domain bottles)

  (:objects
    b1 b2 - bottle
  )

  (:init
    (= (litres b1) 0)
    (= (litres b2) 5)
    (capped b1) ;Se tolgo questo funziona lo stesso
    (capped b2)
    (= (index b1) 1)
    (= (index b2) 2)
    (= (p) 1)
    (= (on-scale) 0)
  )

  (:goal
    (and
      (= (litres b1) 0)
      (= (litres b2) 0)
    )
  )
)