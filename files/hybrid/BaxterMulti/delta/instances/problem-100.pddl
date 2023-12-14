(define (problem example)
  (:domain paco3d)
  (:objects
    armA armB - arm
    L1A L1B L2A L2B L3A L3B L4A L4B - link

    xyaxes ZAXES - axis
  )
  (:init

    (= (time) 0)
    (= (tk armA) 0)
    (= (tk armB) 0)
    (= (delta armA) 1)
    (= (delta armB) 100)

    (= (speed-i armA) 10)
    (= (speed-d armA) 10)
    (= (speed-i armB) 0.1)
    (= (speed-d armB) 0.1)

    (= (angle armA L1A xyaxes) 64.6)
    (= (angle armB L1B xyaxes) 64.6)
    (= (angle armA L1A ZAXES) 323.2)
    (= (angle armB L1B ZAXES) 323.2)
    (= (angle armA L2A xyaxes) 261.6)
    (= (angle armB L2B xyaxes) 261.6)
    (= (angle armA L2A ZAXES) 122.1)
    (= (angle armB L2B ZAXES) 122.1)
    (= (angle armA L3A xyaxes) 10.3)
    (= (angle armB L3B xyaxes) 10.3)
    (= (angle armA L3A ZAXES) 21.5)
    (= (angle armB L3B ZAXES) 21.5)
    (= (angle armA L4A xyaxes) 189.6)
    (= (angle armB L4B xyaxes) 189.6)
    (= (angle armA L4A ZAXES) 302.3)
    (= (angle armB L4B ZAXES) 302.3)

    (freeToMove armA L1A)
    (freeToMove armB L1B)
    (freeToMove armA L2A)
    (freeToMove armB L2B)
    (freeToMove armA L3A)
    (freeToMove armB L3B)
    (freeToMove armA L4A)
    (freeToMove armB L4B)

    (connected armA L1A L2A)
    (connected armB L1B L2B)
    (connected armA L2A L3A)
    (connected armB L2B L3B)
    (connected armA L3A L4A)
    (connected armB L3B L4B)

    (affects armA L2A L3A)
    (affects armB L2B L3B)
    (affects armA L2A L4A)
    (affects armB L2B L4B)
    (affects armA L3A L4A)
    (affects armB L3B L4B)
  )

  (:goal
    (and

      (> (angle armA L3A xyaxes) 3.5)
      (> (angle armB L3B xyaxes) 3.5)
      (> (angle armA L3A ZAXES) 236.9)
      (> (angle armB L3B ZAXES) 236.9)

    )
  )
)