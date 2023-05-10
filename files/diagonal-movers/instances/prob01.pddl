(define (problem prob01)
  (:domain diagonal-movers)
  (:objects
    red green - mover
    bOrange bBlue - basket
    tOrange tBlue - truck
    orange blue - color
  )
  (:init
    (= (grid-size) 7)

    (= (sign red) 1)
    (= (sign green) -1)

    (= (xMover red) 6)
    (= (yMover red) 3)

    (= (xMover green) 2)
    (= (yMover green) 6)

    (= (xBasket bOrange) 1)
    (= (yBasket bOrange) 6)

    (= (xBasket bBlue) 2)
    (= (yBasket bBlue) 7)

    (= (xTruck tOrange) 7)
    (= (yTruck tOrange) 2)

    (= (xTruck tBlue) 6)
    (= (yTruck tBlue) 1)

    (= (package-size bBlue) 1)
    (= (package-size bOrange) 1)

    (= (objectsInBasket bBlue) 10)
    (= (objectsInBasket bOrange) 9)

    (= (objectsInMover green) 0)
    (= (objectsInMover red) 0)

    (= (capacity green) 20)
    (= (capacity red) 20)

    (= (objectsInTruck tBlue) 0)
    (= (objectsInTruck tOrange) 0)

    (isBasketOfColor bOrange orange)
    (isBasketOfColor bBlue blue)

    (isTruckOfColor tOrange orange)
    (isTruckOfColor tBlue blue)
  )

  (:goal
    (and
      (= (objectsInTruck tOrange) 2)
      (= (objectsInTruck tBlue) 2)
    )
  )
)