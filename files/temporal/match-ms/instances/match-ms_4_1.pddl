(define (problem p_4_1)

  (:domain match_makespan)

  (:objects
    f1 f2 f3 f4 - Fuse
    m1 - Match
  )

  (:init
        (= (light_duration m1) 70)
        (= (mend_duration f1) 1)
        (= (mend_duration f2) 2)
        (= (mend_duration f3) 4)
        (= (mend_duration f4) 8)
        (match_unused m1)
        (handfree)
        (dark)
  )

  (:goal
        (and
        (fuse_mended f1)
        (fuse_mended f2)
        (fuse_mended f3)
        (fuse_mended f4)
        )
  )
)
