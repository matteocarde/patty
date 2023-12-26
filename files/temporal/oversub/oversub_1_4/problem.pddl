(define (problem p_1_4)

  (:domain optional_goals_1_4)

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
        )
  )

  (:metric minimize (total-cost))
)
