(define (problem p_3_6)

  (:domain match_makespan)

  (:objects
    f1 f3 f4 - Fuse
    m1 m2 m3 m4 m5 m6 - Match
  )

  (:init
        (= (light_duration m1) 70)
        (= (light_duration m2) 9)
        (= (light_duration m3) 8)
        (= (light_duration m4) 7)
        (= (light_duration m5) 6)
        (= (light_duration m6) 5)
        (= (mend_duration f1) 1)
        (= (mend_duration f3) 4)
        (= (mend_duration f4) 8)
        (match_unused m1)
        (match_unused m2)
        (match_unused m3)
        (match_unused m4)
        (match_unused m5)
        (match_unused m6)
        (handfree)
        (dark)
  )

  (:goal
        (and
        (fuse_mended f1)
        (fuse_mended f3)
        (fuse_mended f4)
        )
  )
)
