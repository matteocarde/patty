(define (problem p_1_2)

  (:domain optional_goals_1_2)

  (:init
        (= (total-cost) 0)
  )

  (:goal
        (and
        (y)
        (g1)
        (g2)
        )
  )

  (:metric minimize (total-cost))
)