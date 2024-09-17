(define (domain counter)
  (:requirements :strips :equality :conditional-effects)

  (:predicates
    (x1)
    (x2)
    (x3)
    (x4)
    (x5)
    (x6)
    (x7)

    (y1)
    (y2)
    (y3)
    (y4)
    (y5)
    (y6)
    (y7)

    (l1)
    (l2)
    (l3)
    (l4)
    (l5)
    (l6)
    (l7)
  )

  (:action inx
    :parameters ()
    :precondition ()
    :effect (and
      (when ;xxxxxx0 -> xxxxxx1
        (and
          (not (x1))
          (not (l1)))
        (and (x1))
      )
      (when ;xxxxx01 -> xxxxx10
        (and
          (not (x2))(x1)
          (not (l2))
          (not (l1)))
        (and
          (x2)
          (not (x1)))
      )
      (when ;xxxx011 -> xxxx100
        (and
          (not (x3))(x2)(x1)
          (not (l3))
          (not (l2))
          (not (l1)))
        (and
          (x3)
          (not (x2))
          (not (x1)))
      )
      (when ;xxx0111 -> xxx1000
        (and
          (not (x4))(x3)(x2)(x1)
          (not (l4))
          (not (l3))
          (not (l2))
          (not (l1)))
        (and
          (x4)
          (not (x3))
          (not (x2))
          (not (x1)))
      )
      (when ;xx01111 -> xx10000
        (and
          (not (x5))(x4)(x3)(x2)(x1)
          (not (l5))
          (not (l4))
          (not (l3))
          (not (l2))
          (not (l1)))
        (and (x5)
          (not (x4))
          (not (x3))
          (not (x2))
          (not (x1)))
      )
      (when ;x011111 -> x100000
        (and
          (not (x6))(x5)(x4)(x3)(x2)(x1)
          (not (l6))
          (not (l5))
          (not (l4))
          (not (l3))
          (not (l2))
          (not (l1)))
        (and (x6)
          (not (x5))
          (not (x4))
          (not (x3))
          (not (x2))
          (not (x1)))
      )
      (when ;0111111 -> 1000000
        (and
          (not (x7))(x6)(x5)(x4)(x3)(x2)(x1)
          (not (l7))
          (not (l6))
          (not (l5))
          (not (l4))
          (not (l3))
          (not (l2))
          (not (l1)))
        (and
          (x7)
          (not (x6))
          (not (x5))
          (not (x4))
          (not (x3))
          (not (x2))
          (not (x1)))
      )
      (when ;1111111 -> 0000000
        (and
          (x7)(x6)(x5)(x4)(x3)(x2)(x1)
          (not (l7))
          (not (l6))
          (not (l5))
          (not (l4))
          (not (l3))
          (not (l2))
          (not (l1)))
        (and
          (not (x7))
          (not (x6))
          (not (x5))
          (not (x4))
          (not (x3))
          (not (x2))
          (not (x1)))
      )
    )
  )

(:action inx
    :parameters ()
    :precondition ()
    :effect (and
      (when ;xxxxxx0 -> xxxxxx1
        (and
          (not (x1))
          (not (l1)))
        (and (x1))
      )
      (when ;xxxxx01 -> xxxxx10
        (and
          (not (x2))(x1)
          (not (l2))
          (not (l1)))
        (and
          (x2)
          (not (x1)))
      )
      (when ;xxxx011 -> xxxx100
        (and
          (not (x3))(x2)(x1)
          (not (l3))
          (not (l2))
          (not (l1)))
        (and
          (x3)
          (not (x2))
          (not (x1)))
      )
      (when ;xxx0111 -> xxx1000
        (and
          (not (x4))(x3)(x2)(x1)
          (not (l4))
          (not (l3))
          (not (l2))
          (not (l1)))
        (and
          (x4)
          (not (x3))
          (not (x2))
          (not (x1)))
      )
      (when ;xx01111 -> xx10000
        (and
          (not (x5))(x4)(x3)(x2)(x1)
          (not (l5))
          (not (l4))
          (not (l3))
          (not (l2))
          (not (l1)))
        (and (x5)
          (not (x4))
          (not (x3))
          (not (x2))
          (not (x1)))
      )
      (when ;x011111 -> x100000
        (and
          (not (x6))(x5)(x4)(x3)(x2)(x1)
          (not (l6))
          (not (l5))
          (not (l4))
          (not (l3))
          (not (l2))
          (not (l1)))
        (and (x6)
          (not (x5))
          (not (x4))
          (not (x3))
          (not (x2))
          (not (x1)))
      )
      (when ;0111111 -> 1000000
        (and
          (not (x7))(x6)(x5)(x4)(x3)(x2)(x1)
          (not (l7))
          (not (l6))
          (not (l5))
          (not (l4))
          (not (l3))
          (not (l2))
          (not (l1)))
        (and
          (x7)
          (not (x6))
          (not (x5))
          (not (x4))
          (not (x3))
          (not (x2))
          (not (x1)))
      )
      (when ;1111111 -> 0000000
        (and
          (x7)(x6)(x5)(x4)(x3)(x2)(x1)
          (not (l7))
          (not (l6))
          (not (l5))
          (not (l4))
          (not (l3))
          (not (l2))
          (not (l1)))
        (and
          (not (x7))
          (not (x6))
          (not (x5))
          (not (x4))
          (not (x3))
          (not (x2))
          (not (x1)))
      )
    )
  )

)