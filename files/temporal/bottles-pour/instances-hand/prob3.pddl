(define (problem bottles_prob)

  (:domain bottles)

  (:objects
    l1 l2 - bottleleft
    r1 - bottleright
  )

  (:init
    (= (litres l1) 10)
    (= (litres l2) 10)
    (= (litres r1) 0)
    (capped l1)
    (capped l2)
    (capped r1)
  )

  (:goal
    (and
      (= (litres r1) 20)
    )
  )
)