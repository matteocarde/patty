
(define (problem pb348)
    (:domain tapes)
    (:objects 
        r - robot
        t01 t02 t03 - tape
        a01 a02 a03 - counter
        c01 c02 c03 c04 c05 c06 c07 - cell
    )
    (:init
        (onTape r t01)
        (onCellRobot r c01)
        (onCellCounter a01 t01 c04) (onCellCounter a02 t02 c04) (onCellCounter a03 t03 c04)
        (startCell c01)
        (isNextCell c01 c02) (isNextCell c02 c03) (isNextCell c03 c04) (isNextCell c04 c05) (isNextCell c05 c06) (isNextCell c06 c07) (isNextCell c07 c01)
        (isNextTape t01 t02) (isNextTape t02 t03) (isNextTape t03 t01)
        (x08 a01) (x06 a01) (x05 a01) (x04 a01) (x03 a01) (x01 a01) (x08 a02) (x09 a03) (x08 a03) (x07 a03) (x05 a03) (x02 a03) (x01 a03)
    )
    (:goal
        (and  
            (or (and (x01 a01) (x01 a02))(and (not (x01 a01)) (not (x01 a02)))) (or (and (x01 a02) (x01 a03))(and (not (x01 a02)) (not (x01 a03)))) (or (and (x02 a01) (x02 a02))(and (not (x02 a01)) (not (x02 a02)))) (or (and (x02 a02) (x02 a03))(and (not (x02 a02)) (not (x02 a03)))) (or (and (x03 a01) (x03 a02))(and (not (x03 a01)) (not (x03 a02)))) (or (and (x03 a02) (x03 a03))(and (not (x03 a02)) (not (x03 a03)))) (or (and (x04 a01) (x04 a02))(and (not (x04 a01)) (not (x04 a02)))) (or (and (x04 a02) (x04 a03))(and (not (x04 a02)) (not (x04 a03)))) (or (and (x05 a01) (x05 a02))(and (not (x05 a01)) (not (x05 a02)))) (or (and (x05 a02) (x05 a03))(and (not (x05 a02)) (not (x05 a03)))) (or (and (x06 a01) (x06 a02))(and (not (x06 a01)) (not (x06 a02)))) (or (and (x06 a02) (x06 a03))(and (not (x06 a02)) (not (x06 a03)))) (or (and (x07 a01) (x07 a02))(and (not (x07 a01)) (not (x07 a02)))) (or (and (x07 a02) (x07 a03))(and (not (x07 a02)) (not (x07 a03)))) (or (and (x08 a01) (x08 a02))(and (not (x08 a01)) (not (x08 a02)))) (or (and (x08 a02) (x08 a03))(and (not (x08 a02)) (not (x08 a03)))) (or (and (x09 a01) (x09 a02))(and (not (x09 a01)) (not (x09 a02)))) (or (and (x09 a02) (x09 a03))(and (not (x09 a02)) (not (x09 a03))))
        )
    )
    )
 