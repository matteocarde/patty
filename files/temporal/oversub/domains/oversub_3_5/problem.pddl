(define (problem p_3_5)

  (:domain optional_goals_3_5)

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
