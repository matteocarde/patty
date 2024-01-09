(define (problem p_2_3)

  (:domain optional_goals_2_3)

  (:init
        (= (total-cost) 0)
  )

  (:goal
        (and
        (y)
        (g1)
        (g2)
        (g3)
        )
  )

  (:metric minimize (total-cost))
)
