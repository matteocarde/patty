(define (problem p_2_7)

  (:domain optional_goals_2_7)

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
        (g7)
        )
  )

  (:metric minimize (total-cost))
)
