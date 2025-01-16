
(define (problem pb150)
    (:domain tapes)
    (:objects 
        r - robot
        t01 t02 t03 t04 t05 t06 t07 - tape
        a01 a02 a03 a04 a05 a06 a07 - counter
        c01 c02 c03 c04 c05 - cell
    )
    (:init
        (onTape r t01)
        (onCellRobot r c01)
        (onCellCounter a01 t01 c03) (onCellCounter a02 t02 c03) (onCellCounter a03 t03 c03) (onCellCounter a04 t04 c03) (onCellCounter a05 t05 c03) (onCellCounter a06 t06 c03) (onCellCounter a07 t07 c03)
        (startCell c01)
        (isNextCell c01 c02) (isNextCell c02 c03) (isNextCell c03 c04) (isNextCell c04 c05) (isNextCell c05 c01)
        (isNextTape t01 t02) (isNextTape t02 t03) (isNextTape t03 t04) (isNextTape t04 t05) (isNextTape t05 t06) (isNextTape t06 t07) (isNextTape t07 t01)
        (x03 a01) (x02 a01) (x04 a02) (x03 a02) (x02 a02) (x03 a03) (x02 a03) (x01 a03) (x05 a04) (x02 a04) (x01 a04) (x05 a05) (x04 a05) (x03 a05) (x02 a05) (x01 a05) (x03 a06) (x02 a06) (x05 a07) (x04 a07) (x03 a07) (x01 a07)
    )
    (:goal
        (and  
            (or (and (x01 a01) (x01 a02))(and (not (x01 a01)) (not (x01 a02)))) (or (and (x01 a02) (x01 a03))(and (not (x01 a02)) (not (x01 a03)))) (or (and (x01 a03) (x01 a04))(and (not (x01 a03)) (not (x01 a04)))) (or (and (x01 a04) (x01 a05))(and (not (x01 a04)) (not (x01 a05)))) (or (and (x01 a05) (x01 a06))(and (not (x01 a05)) (not (x01 a06)))) (or (and (x01 a06) (x01 a07))(and (not (x01 a06)) (not (x01 a07)))) (or (and (x02 a01) (x02 a02))(and (not (x02 a01)) (not (x02 a02)))) (or (and (x02 a02) (x02 a03))(and (not (x02 a02)) (not (x02 a03)))) (or (and (x02 a03) (x02 a04))(and (not (x02 a03)) (not (x02 a04)))) (or (and (x02 a04) (x02 a05))(and (not (x02 a04)) (not (x02 a05)))) (or (and (x02 a05) (x02 a06))(and (not (x02 a05)) (not (x02 a06)))) (or (and (x02 a06) (x02 a07))(and (not (x02 a06)) (not (x02 a07)))) (or (and (x03 a01) (x03 a02))(and (not (x03 a01)) (not (x03 a02)))) (or (and (x03 a02) (x03 a03))(and (not (x03 a02)) (not (x03 a03)))) (or (and (x03 a03) (x03 a04))(and (not (x03 a03)) (not (x03 a04)))) (or (and (x03 a04) (x03 a05))(and (not (x03 a04)) (not (x03 a05)))) (or (and (x03 a05) (x03 a06))(and (not (x03 a05)) (not (x03 a06)))) (or (and (x03 a06) (x03 a07))(and (not (x03 a06)) (not (x03 a07)))) (or (and (x04 a01) (x04 a02))(and (not (x04 a01)) (not (x04 a02)))) (or (and (x04 a02) (x04 a03))(and (not (x04 a02)) (not (x04 a03)))) (or (and (x04 a03) (x04 a04))(and (not (x04 a03)) (not (x04 a04)))) (or (and (x04 a04) (x04 a05))(and (not (x04 a04)) (not (x04 a05)))) (or (and (x04 a05) (x04 a06))(and (not (x04 a05)) (not (x04 a06)))) (or (and (x04 a06) (x04 a07))(and (not (x04 a06)) (not (x04 a07)))) (or (and (x05 a01) (x05 a02))(and (not (x05 a01)) (not (x05 a02)))) (or (and (x05 a02) (x05 a03))(and (not (x05 a02)) (not (x05 a03)))) (or (and (x05 a03) (x05 a04))(and (not (x05 a03)) (not (x05 a04)))) (or (and (x05 a04) (x05 a05))(and (not (x05 a04)) (not (x05 a05)))) (or (and (x05 a05) (x05 a06))(and (not (x05 a05)) (not (x05 a06)))) (or (and (x05 a06) (x05 a07))(and (not (x05 a06)) (not (x05 a07))))
        )
    )
    )
 