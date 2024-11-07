(define (problem p_1_5)

  (:domain optional_goals_1_5)

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
        )
  )

  (:metric minimize (total-cost))
)
