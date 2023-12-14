(define (problem example)
  (:domain paco3d)
  (:objects
    armA armB - arm
    L1A L1B L2A L2B L3A L3B L4A L4B L5A L5B L6A L6B - link

    xyaxes ZAXES - axis
  )
  (:init

    (= (time) 0)
    (= (tk armA) 0)
    (= (tk armB) 0)
    (= (delta armA) 1)
    (= (delta armB) 100000)

    (= (speed-i armA) 10)
    (= (speed-d armA) 10)
    (= (speed-i armB) 0.001)
    (= (speed-d armB) 0.0001)

    (= (angle armA L1A xyaxes) 337.8)
    (= (angle armB L1B xyaxes) 337.8)
    (= (angle armA L1A ZAXES) 180.9)
    (= (angle armB L1B ZAXES) 180.9)
    (= (angle armA L2A xyaxes) 90.1)
    (= (angle armB L2B xyaxes) 90.1)
    (= (angle armA L2A ZAXES) 67.1)
    (= (angle armB L2B ZAXES) 67.1)
    (= (angle armA L3A xyaxes) 130.0)
    (= (angle armB L3B xyaxes) 130.0)
    (= (angle armA L3A ZAXES) 27.3)
    (= (angle armB L3B ZAXES) 27.3)
    (= (angle armA L4A xyaxes) 250.9)
    (= (angle armB L4B xyaxes) 250.9)
    (= (angle armA L4A ZAXES) 270.1)
    (= (angle armB L4B ZAXES) 270.1)
    (= (angle armA L5A xyaxes) 340.1)
    (= (angle armB L5B xyaxes) 340.1)
    (= (angle armA L5A ZAXES) 20.4)
    (= (angle armB L5B ZAXES) 20.4)
    (= (angle armA L6A xyaxes) 60.5)
    (= (angle armB L6B xyaxes) 60.5)
    (= (angle armA L6A ZAXES) 255.3)
    (= (angle armB L6B ZAXES) 255.3)

    (freeToMove armA L1A)
    (freeToMove armB L1B)
    (freeToMove armA L2A)
    (freeToMove armB L2B)
    (freeToMove armA L3A)
    (freeToMove armB L3B)
    (freeToMove armA L4A)
    (freeToMove armB L4B)
    (freeToMove armA L5A)
    (freeToMove armB L5B)
    (freeToMove armA L6A)
    (freeToMove armB L6B)

    (connected armA L1A L2A)
    (connected armB L1B L2B)
    (connected armA L2A L3A)
    (connected armB L2B L3B)
    (connected armA L3A L4A)
    (connected armB L3B L4B)
    (connected armA L4A L5A)
    (connected armB L4B L5B)
    (connected armA L5A L6A)
    (connected armB L5B L6B)

    (affects armA L2A L3A)
    (affects armB L2B L3B)
    (affects armA L2A L4A)
    (affects armB L2B L4B)
    (affects armA L2A L5A)
    (affects armB L2B L5B)
    (affects armA L2A L6A)
    (affects armB L2B L6B)
    (affects armA L3A L4A)
    (affects armB L3B L4B)
    (affects armA L3A L5A)
    (affects armB L3B L5B)
    (affects armA L3A L6A)
    (affects armB L3B L6B)
    (affects armA L4A L5A)
    (affects armB L4B L5B)
    (affects armA L4A L6A)
    (affects armB L4B L6B)
    (affects armA L5A L6A)
    (affects armB L5B L6B)
  )

  (:goal
    (and

      (> (angle armA L3A xyaxes) 348.5)
      (> (angle armB L3B xyaxes) 348.5)
      (> (angle armA L3A ZAXES) 268.6)
      (> (angle armB L3B ZAXES) 268.6)

      (> (angle armA L5A xyaxes) 128.0)
      (> (angle armB L5B xyaxes) 128.0)
      (> (angle armA L5A ZAXES) 279.4)
      (> (angle armB L5B ZAXES) 279.4)

      (< (angle armA L3A xyaxes) 352.9)
      (< (angle armB L3B xyaxes) 352.9)

    )
  )
)