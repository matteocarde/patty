(define (problem prob01)
  (:domain mailrobot)
  (:objects
    r0 r1 r2 - robot
    l0 l2 - letter
  )

  (:init
    (hasLetter l0 r0)
    (hasLetter l2 r2)
    (canSign l0 r0)
    (canSign l2 r2)
    (canStamp r1)
    (= (i r0) 0)
    (= (i r1) 1)
    (= (i r2) 2)

    (= (L) 5)
    (= (x r0) 0)
    (= (x r1) 5)
    (= (x r2) 10)
    (= (s l0) 0)
    (= (s l2) 0)
  )

  (:goal
    (and
      (hasLetter l0 r0)
      (hasLetter l2 r2)
      (signed l0)
      (signed l2)
    )
  )
)