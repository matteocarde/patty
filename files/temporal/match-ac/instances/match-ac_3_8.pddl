(define (problem p_3_8)

  (:domain match_action_cost)

  (:objects
    f1 f3 f4 - Fuse
    m1 m2 m3 m4 m5 m6 m7 m8 - Match
  )

  (:init
        (= (match_cost m1) 70)
        (= (match_cost m2) 9)
        (= (match_cost m3) 8)
        (= (match_cost m4) 7)
        (= (match_cost m5) 6)
        (= (match_cost m6) 5)
        (= (match_cost m7) 4)
        (= (match_cost m8) 3)
        (= (light_duration m1) 70)
        (= (light_duration m2) 9)
        (= (light_duration m3) 8)
        (= (light_duration m4) 7)
        (= (light_duration m5) 6)
        (= (light_duration m6) 5)
        (= (light_duration m7) 4)
        (= (light_duration m8) 3)
        (= (mend_duration f1) 1)
        (= (mend_duration f3) 4)
        (= (mend_duration f4) 8)
        (match_unused m1)
        (match_unused m2)
        (match_unused m3)
        (match_unused m4)
        (match_unused m5)
        (match_unused m6)
        (match_unused m7)
        (match_unused m8)
        (handfree)
        (= (total-cost) 0)
  )

  (:goal
        (and
        (fuse_mended f1)
        (fuse_mended f3)
        (fuse_mended f4)
        )
  )

  (:metric minimize (total-cost))
)
