(define (problem example)
  (:domain paco3d)
  (:objects
    L1 L2 L3 L4 L5 L6 - link

    xyaxes ZAXES - axis
  )
  (:init

    (= (speed-i) 10)
    (= (speed-d) 10)

    (= (angle L1 xyaxes) 54.2)
    (= (angle L1 ZAXES) 300.6)
    (= (angle L2 xyaxes) 161.8)
    (= (angle L2 ZAXES) 108.0)
    (= (angle L3 xyaxes) 201.8)
    (= (angle L3 ZAXES) 58.4)
    (= (angle L4 xyaxes) 287.0)
    (= (angle L4 ZAXES) 326.9)
    (= (angle L5 xyaxes) 297.9)
    (= (angle L5 ZAXES) 10.9)
    (= (angle L6 xyaxes) 172.4)
    (= (angle L6 ZAXES) 35.0)

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

      (> (angle L3 xyaxes) 140.3)
      (> (angle L3 ZAXES) 82.6)

      (> (angle L5 xyaxes) 127.2)
      (> (angle L5 ZAXES) 168.8)

    ))
)