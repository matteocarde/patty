(define (problem example)
  (:domain paco3d)
  (:objects
    L1 L2 L3 L4 L5 L6 - link

    xyaxes ZAXES - axis
  )
  (:init

    (= (speed-i) 10)
    (= (speed-d) 10)

    (= (angle L1 xyaxes) 69.2)
    (= (angle L1 ZAXES) 168.0)
    (= (angle L2 xyaxes) 119.0)
    (= (angle L2 ZAXES) 241.2)
    (= (angle L3 xyaxes) 297.9)
    (= (angle L3 ZAXES) 125.4)
    (= (angle L4 xyaxes) 306.8)
    (= (angle L4 ZAXES) 327.0)
    (= (angle L5 xyaxes) 297.2)
    (= (angle L5 ZAXES) 343.0)
    (= (angle L6 xyaxes) 121.5)
    (= (angle L6 ZAXES) 342.0)

    (freeToMove L1)
    (freeToMove L2)
    (freeToMove L3)
    (freeToMove L4)
    (freeToMove L5)
    (freeToMove L6)

    (connected L1 L2)
    (connected L2 L3)
    (connected L3 L4)
    (connected L4 L5)
    (connected L5 L6)

    (affects L2 L3)
    (affects L2 L4)
    (affects L2 L5)
    (affects L2 L6)
    (affects L3 L4)
    (affects L3 L5)
    (affects L3 L6)
    (affects L4 L5)
    (affects L4 L6)
    (affects L5 L6)
  )

  (:goal
    (and

      (> (angle L3 xyaxes) 0.6)
      (> (angle L3 ZAXES) 186.3)

      (> (angle L5 xyaxes) 125.6)
      (> (angle L5 ZAXES) 299.5)

      (< (angle L2 xyaxes) 197.7)

    ))
)