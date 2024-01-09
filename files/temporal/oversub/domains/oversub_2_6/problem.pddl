(define (problem p_2_6)

  (:domain optional_goals_2_6)

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
