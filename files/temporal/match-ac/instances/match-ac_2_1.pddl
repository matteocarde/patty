(define (problem p_2_1)

  (:domain match_action_cost)

  (:objects
    f1 f4 - Fuse
    m1 - Match
  )

  (:init
    (= (match_cost m1) 70)
    (= (light_duration m1) 70)
    (= (mend_duration f1) 1)
    (= (mend_duration f4) 8)
    (match_unused m1)
    (handfree)
    (= (total-cost) 0)
  )

  (:goal
    (and
      (fuse_mended f1)
      (fuse_mended f4)
    )
  )

  (:metric minimize
    (total-cost)
  )
)