(define (problem example)
  (:domain paco3d)
  (:objects
    L1 L2 L3 L4 - link

    xyaxes ZAXES - axis
  )
  (:init

    (= (speed-i) 10)
    (= (speed-d) 10)

    (= (angle L1 xyaxes) 285.1)
    (= (angle L1 ZAXES) 71.5)
    (= (angle L2 xyaxes) 194.8)
    (= (angle L2 ZAXES) 277.6)
    (= (angle L3 xyaxes) 20.2)
    (= (angle L3 ZAXES) 28.7)
    (= (angle L4 xyaxes) 137.0)
    (= (angle L4 ZAXES) 102.2)

    (freeToMove L1)
    (freeToMove L2)
    (freeToMove L3)
    (freeToMove L4)

    (connected L1 L2)
    (connected L2 L3)
    (connected L3 L4)

    (affects L2 L3)
    (affects L2 L4)
    (affects L3 L4)
  )

  (:goal
    (and

      (> (angle L3 xyaxes) 311.6)
      (> (angle L3 ZAXES) 277.1)

      (< (angle L3 xyaxes) 343.4)

    ))
)