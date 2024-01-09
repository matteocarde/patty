(define (problem p_5_5)

  (:domain match_action_cost)

  (:objects
    f1 f2 f3 f4 f5 - Fuse
    m1 m2 m3 m4 m5 - Match
  )

  (:init
        (= (match_cost m1) 70)
        (= (match_cost m2) 9)
        (= (match_cost m3) 8)
        (= (match_cost m4) 7)
        (= (match_cost m5) 6)
        (= (light_duration m1) 70)
        (= (light_duration m2) 9)
        (= (light_duration m3) 8)
        (= (light_duration m4) 7)
        (= (light_duration m5) 6)
        (= (mend_duration f1) 1)
        (= (mend_duration f2) 2)
        (= (mend_duration f3) 4)
        (= (mend_duration f4) 6)
        (= (mend_duration f5) 8)
        (match_unused m1)
        (match_unused m2)
        (match_unused m3)
        (match_unused m4)
        (match_unused m5)
        (handfree)
        (= (total-cost) 0)
  )

  (:goal
        (and
        (fuse_mended f1)
        (fuse_mended f2)
        (fuse_mended f3)
        (fuse_mended f4)
        (fuse_mended f5)
        )
  )

  (:metric minimize (total-cost))
)