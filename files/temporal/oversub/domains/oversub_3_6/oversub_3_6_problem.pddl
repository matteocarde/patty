(define (problem p_3_6)

  (:domain optional_goals_3_6)

  (:init
        (= (total-cost) 0)
  )

  (:goal
        (and
        (y)
        (g1)
        (g2)
        (g3)
        (g4)
        (g5)
        (g6)
        )
  )

  (:metric minimize (total-cost))
)
