;; Enrico Scala (enricos83@gmail.com) and Miquel Ramirez (miquel.ramirez@gmail.com)
(define (problem sample)
  (:domain mt-block-grouping)
  (:objects
    b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 - block
  )

  (:init
  	;;(= (loc b1) pos-3-5)
    (= (x b1) 3) (= (y b1) 5)
  	;;(= (loc b10) pos-4-1)
    (= (x b10) 4) (= (y b10) 1)
  	;;(= (loc b9) pos-3-5)
    (= (x b9) 3) (= (y b9) 5)
  	;;(= (loc b4) pos-4-4)
    (= (x b4) 4) (= (y b4) 4)
  	;;(= (loc b3) pos-1-1)
    (= (x b3) 1) (= (y b3) 1)
  	;;(= (loc b8) pos-3-3)
    (= (x b8) 3) (= (y b8) 3)
  	;;(= (loc b5) pos-4-4)
    (= (x b5) 4) (= (y b5) 4)
  	;;(= (loc b7) pos-5-1)
    (= (x b7) 5) (= (y b7) 1)
  	;;(= (loc b6) pos-1-2)
    (= (x b6) 1) (= (y b6) 2)
  	;;(= (loc b2) pos-4-4)
    (= (x b2) 4) (= (y b2) 4)

    ;; bounds
    (= (min_x) 1) (= (max_x) 5)
    (= (min_y) 1) (= (max_y) 5)
  )

  (:goal (and
    ;;(not (= (loc b1) (loc b2)))
    (or (not (= (x b1) (x b2) ))
    (not (= (y b1) (y b2) )))

	  ;;(= (loc b1) (loc b3))
    (= (x b1) (x b3))
    (= (y b1) (y b3) )

  	;;(= (loc b1) (loc b4))
    (= (x b1) (x b4) )
    (= (y b1) (y b4) )

    ;;(not (= (loc b1) (loc b5)))
    (or (not (= (x b1) (x b5) ))
    (not (= (y b1) (y b5) )))

    ;;(= (loc b1) (loc b6))
    (= (x b1) (x b6) )
    (= (y b1) (y b6) )

    ;;(not (= (loc b1) (loc b7)))
    (or (not (= (x b1) (x b7) ))
    (not (= (y b1) (y b7) )))

    ;;(not (= (loc b1) (loc b8)))
    (or (not (= (x b1) (x b8) ))
    (not (= (y b1) (y b8) )))

    ;;(not (= (loc b1) (loc b9)))
    (or (not (= (x b1) (x b9) ))
    (not (= (y b1) (y b9) )))

    ;;(not (= (loc b1) (loc b10)))
    (or (not (= (x b1) (x b10) ))
    (not (= (y b1) (y b10) )))

    ;;(not (= (loc b2) (loc b3)))
    (or (not (= (x b2) (x b3) ))
    (not (= (y b2) (y b3) )))

    ;;(not (= (loc b2) (loc b4)))
    (or (not (= (x b2) (x b4) ))
    (not (= (y b2) (y b4) )))

    ;;(= (loc b2) (loc b5))
    (= (x b2) (x b5) )
    (= (y b2) (y b5) )

    ;;(not (= (loc b2) (loc b6)))
    (or (not (= (x b2) (x b6) ))
    (not (= (y b2) (y b6) )))

    ;;(= (loc b2) (loc b7))
    (= (x b2) (x b7) )
    (= (y b2) (y b7) )

    ;;(= (loc b2) (loc b8))
    (= (x b2) (x b8) )
    (= (y b2) (y b8) )

    ;;(= (loc b2) (loc b9))
    (= (x b2) (x b9) )
    (= (y b2) (y b9) )

    ;;(= (loc b3) (loc b4))
    (= (x b3) (x b4) )
    (= (y b3) (y b4) )

    ;;(not (= (loc b3) (loc b5)))
    (or (not (= (x b3) (x b5) ))
    (not (= (y b3) (y b5) )))

    ;;(= (loc b3) (loc b6))
    (= (x b3) (x b6) )
    (= (y b3) (y b6) )

    ;;(not (= (loc b3) (loc b7)))
    (or (not (= (x b3) (x b7) ))
    (not (= (y b3) (y b7) )))

    ;;(not (= (loc b3) (loc b8)))
    (or (not (= (x b3) (x b8) ))
    (not (= (y b3) (y b8) )))

    ;;(not (= (loc b3) (loc b9)))
    (or (not (= (x b3) (x b9) ))
    (not (= (y b3) (y b9) )))

    ;;(not (= (loc b4) (loc b5)))
    (or (not (= (x b4) (x b5) ))
    (not (= (y b4) (y b5) )))

    ;;(= (loc b4) (loc b6))
    (= (x b4) (x b6) )
    (= (y b4) (y b6) )

    ;;(not (= (loc b4) (loc b7)))
    (or (not (= (x b4) (x b7) ))
    (not (= (y b4) (y b7) )))

    ;;(not (= (loc b4) (loc b8)))
    (or (not (= (x b4) (x b8) ))
    (not (= (y b4) (y b8) )))

    ;;(not (= (loc b4) (loc b9)))
    (or (not (= (x b4) (x b9) ))
    (not (= (y b4) (y b9) )))

    ;;(not (= (loc b5) (loc b6)))
    (or (not (= (x b5) (x b6) ))
    (not (= (y b5) (y b6) )))

    ;;(= (loc b5) (loc b7))
    (= (x b5) (x b7) )
    (= (y b5) (y b7) )

    ;;(= (loc b5) (loc b8))
    (= (x b5) (x b8) )
    (= (y b5) (y b8) )

    ;;(= (loc b5) (loc b9))
    (= (x b5) (x b9) )
    (= (y b5) (y b9) )

    ;;(not (= (loc b6) (loc b7)))
    (or (not (= (x b6) (x b7) ))
    (not (= (y b6) (y b7) )))

    ;;(not (= (loc b6) (loc b8)))
    (or (not (= (x b6) (x b8) ))
    (not (= (y b6) (y b8) )))

    ;;(not (= (loc b6) (loc b9)))
    (or (not (= (x b6) (x b9) ))
    (not (= (y b6) (y b9) )))

    ;;(= (loc b7) (loc b8))
    (= (x b7) (x b8) )
    (= (y b7) (y b8) )

    ;;(= (loc b7) (loc b9))
    (= (x b7) (x b9) )
    (= (y b7) (y b9) )

    ;;(= (loc b8) (loc b9))
    (= (x b8) (x b9) )
    (= (y b8) (y b9) )

    ;;(= (loc b10) (loc b2))
    (= (x b10) (x b2) )
    (= (y b10) (y b2) )

    ;;(not (= (loc b10) (loc b3)))
    (or (not (= (x b10) (x b3) ))
    (not (= (y b10) (y b3) )))

    ;;(not (= (loc b10) (loc b4)))
    (or (not (= (x b10) (x b4) ))
    (not (= (y b10) (y b4) )))

    ;;(= (loc b10) (loc b5))
    (= (x b10) (x b5) )
    (= (y b10) (y b5) )

    ;;(not (= (loc b10) (loc b6)))
    (or (not (= (x b10) (x b6) ))
    (not (= (y b10) (y b6) )))

    ;;(= (loc b10) (loc b7))
    (= (x b10) (x b7) )
    (= (y b10) (y b7) )

    ;;(= (loc b10) (loc b8))
    (= (x b10) (x b8) )
    (= (y b10) (y b8) )

    ;;(= (loc b10) (loc b9))
    (= (x b10) (x b9) )
    (= (y b10) (y b9) )
  ))
)
