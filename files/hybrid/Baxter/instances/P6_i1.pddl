(define (problem example)
  (:domain paco3d)
  (:objects
    L1 L2 L3 L4 L5 L6 - link

    xyaxes ZAXES - axis
  )
  (:init

    (= (speed-i) 10)
    (= (speed-d) 10)

    (= (angle L1 xyaxes) 242.0)
    (= (angle L1 ZAXES) 323.9)
    (= (angle L2 xyaxes) 100.2)
    (= (angle L2 ZAXES) 252.4)
    (= (angle L3 xyaxes) 269.0)
    (= (angle L3 ZAXES) 168.4)
    (= (angle L4 xyaxes) 235.1)
    (= (angle L4 ZAXES) 301.1)
    (= (angle L5 xyaxes) 106.5)
    (= (angle L5 ZAXES) 346.6)
    (= (angle L6 xyaxes) 70.1)
    (= (angle L6 ZAXES) 267.7)

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

      (> (angle L3 xyaxes) 83.1)
      (> (angle L3 ZAXES) 165.4)

      (> (angle L5 xyaxes) 180.5)
      (> (angle L5 ZAXES) 125.3)

      (< (angle L2 xyaxes) 207.2)

    ))
)