
(define (problem pb17)
    (:domain tapes)
    (:objects 
        r - robot
        t01 t02 t03 - tape
        a01 a02 a03 - counter
        c01 c02 c03 - cell
    )
    (:init
        (onTape r t01)
        (onCellRobot r c01)
        (onCellCounter a01 t01 c02) (onCellCounter a02 t02 c02) (onCellCounter a03 t03 c02)
        (startCell c01)
        (isNextCell c01 c02) (isNextCell c02 c03) (isNextCell c03 c01)
        (isNextTape t01 t02) (isNextTape t02 t03) (isNextTape t03 t01)
        (x19 a01) (x19 a03)
    )
    (:goal
        (and  
            (or (and (x01 a01) (x01 a02))(and (not (x01 a01)) (not (x01 a02)))) (or (and (x01 a02) (x01 a03))(and (not (x01 a02)) (not (x01 a03)))) (or (and (x02 a01) (x02 a02))(and (not (x02 a01)) (not (x02 a02)))) (or (and (x02 a02) (x02 a03))(and (not (x02 a02)) (not (x02 a03)))) (or (and (x03 a01) (x03 a02))(and (not (x03 a01)) (not (x03 a02)))) (or (and (x03 a02) (x03 a03))(and (not (x03 a02)) (not (x03 a03)))) (or (and (x04 a01) (x04 a02))(and (not (x04 a01)) (not (x04 a02)))) (or (and (x04 a02) (x04 a03))(and (not (x04 a02)) (not (x04 a03)))) (or (and (x05 a01) (x05 a02))(and (not (x05 a01)) (not (x05 a02)))) (or (and (x05 a02) (x05 a03))(and (not (x05 a02)) (not (x05 a03)))) (or (and (x06 a01) (x06 a02))(and (not (x06 a01)) (not (x06 a02)))) (or (and (x06 a02) (x06 a03))(and (not (x06 a02)) (not (x06 a03)))) (or (and (x07 a01) (x07 a02))(and (not (x07 a01)) (not (x07 a02)))) (or (and (x07 a02) (x07 a03))(and (not (x07 a02)) (not (x07 a03)))) (or (and (x08 a01) (x08 a02))(and (not (x08 a01)) (not (x08 a02)))) (or (and (x08 a02) (x08 a03))(and (not (x08 a02)) (not (x08 a03)))) (or (and (x09 a01) (x09 a02))(and (not (x09 a01)) (not (x09 a02)))) (or (and (x09 a02) (x09 a03))(and (not (x09 a02)) (not (x09 a03)))) (or (and (x10 a01) (x10 a02))(and (not (x10 a01)) (not (x10 a02)))) (or (and (x10 a02) (x10 a03))(and (not (x10 a02)) (not (x10 a03)))) (or (and (x11 a01) (x11 a02))(and (not (x11 a01)) (not (x11 a02)))) (or (and (x11 a02) (x11 a03))(and (not (x11 a02)) (not (x11 a03)))) (or (and (x12 a01) (x12 a02))(and (not (x12 a01)) (not (x12 a02)))) (or (and (x12 a02) (x12 a03))(and (not (x12 a02)) (not (x12 a03)))) (or (and (x13 a01) (x13 a02))(and (not (x13 a01)) (not (x13 a02)))) (or (and (x13 a02) (x13 a03))(and (not (x13 a02)) (not (x13 a03)))) (or (and (x14 a01) (x14 a02))(and (not (x14 a01)) (not (x14 a02)))) (or (and (x14 a02) (x14 a03))(and (not (x14 a02)) (not (x14 a03)))) (or (and (x15 a01) (x15 a02))(and (not (x15 a01)) (not (x15 a02)))) (or (and (x15 a02) (x15 a03))(and (not (x15 a02)) (not (x15 a03)))) (or (and (x16 a01) (x16 a02))(and (not (x16 a01)) (not (x16 a02)))) (or (and (x16 a02) (x16 a03))(and (not (x16 a02)) (not (x16 a03)))) (or (and (x17 a01) (x17 a02))(and (not (x17 a01)) (not (x17 a02)))) (or (and (x17 a02) (x17 a03))(and (not (x17 a02)) (not (x17 a03)))) (or (and (x18 a01) (x18 a02))(and (not (x18 a01)) (not (x18 a02)))) (or (and (x18 a02) (x18 a03))(and (not (x18 a02)) (not (x18 a03)))) (or (and (x19 a01) (x19 a02))(and (not (x19 a01)) (not (x19 a02)))) (or (and (x19 a02) (x19 a03))(and (not (x19 a02)) (not (x19 a03))))
        )
    )
    )
 