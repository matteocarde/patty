(define (problem example)
  (:domain paco3d)
  (:objects
    L1 L2 L3 L4 L5 L6 - link

    xyaxes ZAXES - axis
  )
  (:init

    (= (speed-i) 10)
    (= (speed-d) 10)

    (= (angle L1 xyaxes) 337.8)
    (= (angle L1 ZAXES) 180.9)
    (= (angle L2 xyaxes) 90.1)
    (= (angle L2 ZAXES) 67.1)
    (= (angle L3 xyaxes) 130.0)
    (= (angle L3 ZAXES) 27.3)
    (= (angle L4 xyaxes) 250.9)
    (= (angle L4 ZAXES) 270.1)
    (= (angle L5 xyaxes) 340.1)
    (= (angle L5 ZAXES) 20.4)
    (= (angle L6 xyaxes) 60.5)
    (= (angle L6 ZAXES) 255.3)

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

      (> (angle L3 xyaxes) 348.5)
      (> (angle L3 ZAXES) 268.6)

      (> (angle L5 xyaxes) 128.0)
      (> (angle L5 ZAXES) 279.4)

      (< (angle L3 xyaxes) 352.9)

    ))
)