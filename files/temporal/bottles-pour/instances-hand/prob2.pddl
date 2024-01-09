(define (problem bottles_prob)

  (:domain bottles)

  (:objects
    l1 - bottleleft
    r1 - bottleright
  )

  (:init
    (= (litres l1) 20)
    (= (litres r1) 0)
    (capped l1)
    (capped r1)
  )

  (:goal
    (and
      (= (litres l1) 0)
      (= (litres r1) 20)
    )
  )
)