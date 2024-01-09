(define (problem bottles_prob)

  (:domain bottles)

  (:objects
    l1 l2 - bottleleft
    r1 r2 r3 - bottleright
  )

  (:init
    (= (litres l1) 15)
    (= (litres l2) 5)
    (= (litres r1) 0)
    (= (litres r2) 0)
    (= (litres r3) 0)
    (capped l1)
    (capped l2)
    (capped r1)
    (capped r2)
    (capped r3)
  )

  (:goal
    (and
      (= (litres r1) 5)
      (= (litres r2) 5)
      (= (litres r3) 5)
    )
  )
)