(define (problem p_3_1)

  (:domain optional_goals_3_1)

  (:init
        (= (total-cost) 0)
  )

  (:goal
        (and
        (y)
        (g1)
        )
  )

  (:metric minimize (total-cost))
)
