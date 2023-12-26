(define (problem p_2_2)

  (:domain match_action_cost)

  (:objects
    f1 f4 - Fuse
    m1 m2 - Match
  )

  (:init
        (= (match_cost m1) 70)
        (= (match_cost m2) 9)
        (= (light_duration m1) 70)
        (= (light_duration m2) 9)
        (= (mend_duration f1) 1)
        (= (mend_duration f4) 8)
        (match_unused m1)
        (match_unused m2)
        (handfree)
        (= (total-cost) 0)
  )

  (:goal
        (and
        (fuse_mended f1)
        (fuse_mended f4)
        )
  )

  (:metric minimize (total-cost))
)
