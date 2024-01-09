(define (problem p_3_4)

  (:domain optional_goals_3_4)

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
