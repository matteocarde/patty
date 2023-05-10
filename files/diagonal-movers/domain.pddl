
(define (domain diagonal-movers)

  (:types
    truck mover basket color
  )

  (:predicates
    (isBasketOfColor ?b - basket ?c - color)
    (isTruckOfColor ?t - truck ?c - color)
    (transporting ?m - mover ?c - color)
  )

  (:functions
    (grid-size)
    (xMover ?m - mover)
    (yMover ?m - mover)
    (capacity ?m - mover)
    (xBasket ?b - basket)
    (yBasket ?b - basket)
    (objectsInBasket ?b - basket)
    (objectsInMover ?m - mover)
    (xTruck ?t - truck)
    (yTruck ?t - truck)
    (objectsInTruck ?t - truck)
    (package-size ?b - basket)
    (sign ?m - mover) ;+1 for one mover and -1 for the other
  )

  (:action move-up
    :parameters (?m - mover)
    :precondition (and
      (<= (+ (yMover ?m) 1) (grid-size))
      (>= (* (sign ?m) (- (xMover ?m) (yMover ?m))) 0)
    )
    :effect (and
      (increase (yMover ?m) 1)
    )
  )

  (:action move-down
    :parameters (?m - mover)
    :precondition (and
      (>= (- (yMover ?m) 1) 1)
      (>= (* (sign ?m) (- (xMover ?m) (yMover ?m))) 0)
    )
    :effect (and
      (decrease (yMover ?m) 1)
    )
  )

  (:action move-right
    :parameters (?m - mover)
    :precondition (and
      (<= (+ (xMover ?m) 1) (grid-size))
      (>= (* (sign ?m) (- (xMover ?m) (yMover ?m))) 0)
    )
    :effect (and
      (increase (xMover ?m) 1)
    )
  )

  (:action move-left
    :parameters (?m - mover)
    :precondition (and
      (>= (- (xMover ?m) 1) 1)
      (>= (* (sign ?m) (- (xMover ?m) (yMover ?m))) 0)
    )
    :effect (and
      (decrease (xMover ?m) 1)
    )
  )

  (:action incr-package-size
    :parameters (?b - basket ?m - mover)
    :precondition (and
      (= (xMover ?m) (xBasket ?b))
      (= (yMover ?m) (yBasket ?b))
      (<= (+ (package-size ?b) 1) 6)
      (= (objectsInMover ?m) 0)
    )
    :effect (and
      (increase (package-size ?b) 1)
    )
  )

  (:action decr-package-size
    :parameters (?b - basket ?m - mover)
    :precondition (and
      (= (xMover ?m) (xBasket ?b))
      (= (yMover ?m) (yBasket ?b))
      (>= (- (package-size ?b) 1) 1)
      (= (objectsInMover ?m) 0)
    )
    :effect (and
      (decrease (package-size ?b) 1)
    )
  )

  (:action pick
    :parameters (?b - basket ?c - color ?m - mover)
    :precondition (and
      (= (xMover ?m) (xBasket ?b))
      (= (yMover ?m) (yBasket ?b))
      (isBasketOfColor ?b ?c)
      (<= (+ (objectsInMover ?m) (package-size ?b)) (capacity ?m))
      (>= (- (objectsInBasket ?b) (package-size ?b)) 0)
    )
    :effect (and
      (increase (objectsInMover ?m) (package-size ?b))
      (decrease (objectsInBasket ?b) (package-size ?b))
      (transporting ?m ?c)
    )
  )

  (:action hand-over
    :parameters (?from ?to - mover ?c - color)
    :precondition (and
      (= (xMover ?from) (xMover ?to))
      (= (yMover ?from) (yMover ?to))
      (transporting ?from ?c)
      (= (objectsInMover ?to) 0)
      (<= (objectsInMover ?from) (capacity ?to))
    )
    :effect (and
      (assign
        (objectsInMover ?to)
        (objectsInMover ?from))
      (assign (objectsInMover ?from) 0)
      (not (transporting ?from ?c))
      (transporting ?to ?c)
    )
  )

  (:action load-truck
    :parameters (?m - mover ?t - truck ?c - color)
    :precondition (and
      (transporting ?m ?c)
      (isTruckOfColor ?t ?c)
      (= (xMover ?m) (xTruck ?t))
      (= (yMover ?m) (yTruck ?t))
    )
    :effect (and
      (increase (objectsInTruck ?t) (objectsInMover ?m))
      (assign (objectsInMover ?m) 0)
      (not (transporting ?m ?c))
    )
  )

)