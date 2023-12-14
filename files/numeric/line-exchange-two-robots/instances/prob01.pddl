(define (problem prob01)
  (:domain line-exchange)
  (:objects
  )
  (:init
    (= (xL) -10)
    (= (xR) 10)
    (= (qL) 7)
    (= (qR) 5)
    (= (q) 1)
  )

  (:goal
    (and
      (= (qR) 7)
      (= (xL) -10)
      (= (xR) 10)
    )
  )
)