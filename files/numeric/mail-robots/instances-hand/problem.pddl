(define (problem prob01)
  (:domain mailrobot)
  (:objects
    r0 r2 - robot
    r1 - mailrobot
  )

  (:init
    (= (i r0) 0)
    (= (i r1) 1)
    (= (i r2) 2)

    (= (L) 5)
    (= (x r0) 0)
    (= (x r1) 5)
    (= (x r2) 10)
    (= (p r0) 1)
    (= (p r1) 0)
    (= (p r2) 0)
    (= (q r0) 1)
    (= (q r1) 0)
    (= (q r2) 0)
  )

  (:goal
    (and
      (psd)
      (qsd)
      (= (p r0) 1)
      (= (q r2) 1)
    )
  )
)