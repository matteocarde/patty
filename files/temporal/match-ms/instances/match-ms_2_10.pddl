(define (problem p_2_10)

  (:domain match_makespan)

  (:objects
    f1 f4 - Fuse
    m1 m2 m3 m4 m5 m6 m7 m8 m9 m10 - Match
  )

  (:init
        (= (light_duration m1) 70)
        (= (light_duration m2) 9)
        (= (light_duration m3) 8)
        (= (light_duration m4) 7)
        (= (light_duration m5) 6)
        (= (light_duration m6) 5)
        (= (light_duration m7) 4)
        (= (light_duration m8) 3)
        (= (light_duration m9) 2)
        (= (light_duration m10) 1)
        (= (mend_duration f1) 1)
        (= (mend_duration f4) 8)
        (match_unused m1)
        (match_unused m2)
        (match_unused m3)
        (match_unused m4)
        (match_unused m5)
        (match_unused m6)
        (match_unused m7)
        (match_unused m8)
        (match_unused m9)
        (match_unused m10)
        (handfree)
        (dark)
  )

  (:goal
        (and
        (fuse_mended f1)
        (fuse_mended f4)
        )
  )
)
