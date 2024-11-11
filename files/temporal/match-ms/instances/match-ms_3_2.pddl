(define (problem p_3_2)

  (:domain match_makespan)

  (:objects
    f1 f3 f4 - Fuse
    m1 m2 - Match
  )

  (:init
        (= (light_duration m1) 70)
        (= (light_duration m2) 9)
        (= (mend_duration f1) 1)
        (= (mend_duration f3) 4)
        (= (mend_duration f4) 8)
        (match_unused m1)
        (match_unused m2)
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
