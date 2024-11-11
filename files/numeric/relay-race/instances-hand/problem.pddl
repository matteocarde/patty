
(define (problem prob3)
  (:domain relay-race)
  (:objects
    r0 r1 r2 - runner
    P Q - baton
  )

  (:init
    (= (L) 20)

    (= (i r0) 0)
    (= (i r1) 1)
    (= (i r2) 2)

    (next r0 r1)
    (next r1 r2)

    (= (x r0) 0)
    (= (x r1) 20)
    (= (x r2) 40)

    (= (b r0 P) 1)
    (= (b r1 P) 0)
    (= (b r2 P) 0)

    (= (b r0 Q) 1)
    (= (b r1 Q) 0)
    (= (b r2 Q) 0)

    (= (h r0) 2)
    (= (h r1) 0)
    (= (h r2) 0)

    (td r0 P)
    (td r0 Q)

  )

  (:goal
    (and
      (td r0 P) (td r1 P)
      (td r0 Q) (td r1 Q) (td r2 Q)
      (= (b r0 P) 1)
      (= (b r2 Q) 1)
    )
  )
)