(define (problem p_3_9)

  (:domain optional_goals_3_9)

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
        (g8)
        (g9)
        )
  )

  (:metric minimize (total-cost))
)
