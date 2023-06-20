
(define (domain line-exchange)

  (:predicates
    (p)
  )

  (:functions
    (xR)
    (xL)
    (qL)
    (qR)
    (q)
  )

  (:action lft_R
    :parameters ()
    :precondition (and
      (> (xR) 0)
    )
    :effect (and
      (decrease (xR) 1)
    )
  )

  (:action rgt_R
    :parameters ()
    :precondition (and
      (not (p))
    )
    :effect (and
      (increase (xR) 1)
    )
  )

  (:action lft_L
    :parameters ()
    :precondition (and
      (not (p))
    )
    :effect (and
      (decrease (xL) 1)
    )
  )

  (:action rgt_R
    :parameters ()
    :precondition (and
      (< (xL) 0)
    )
    :effect (and
      (increase (xL) 1)
    )
  )

  (:action pair
    :parameters ()
    :precondition (and
      (= (xL) (xR))
    )
    :effect (and
      (p)
    )
  )

  (:action unpair
    :parameters ()
    :precondition ()
    :effect (and
      (not (p))
    )
  )

  (:action exch
    :parameters ()
    :precondition (and
      (p)
      (>= (qL) (q))
      (>= (qR) (* -1 (q)))
    )
    :effect (and
      (decrease (qL) (q))
      (increase (qR) (q))
    )
  )

  (:action lre
    :parameters ()
    :precondition ()
    :effect (and
      (assign (q) 1)
    )
  )

  (:action rle
    :parameters ()
    :precondition ()
    :effect (and
      (assign (q) -1)
    )
  )

)