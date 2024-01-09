(define (problem bottles_prob)

  (:domain bottles)

  (:objects
    l1 l2 - bottleleft
    r1 r2 - bottleright
  )

  (:init
    (= (litres l1) 15)
    (= (litres l2) 5)
    (= (litres r1) 0)
    (= (litres r2) 0)
    (capped l1)
    (capped l2)
    (capped r1)
    (capped r2)
  )

  (:goal
    (and
      (= (litres r1) 10)
      (= (litres r2) 10)
    )
  )
)