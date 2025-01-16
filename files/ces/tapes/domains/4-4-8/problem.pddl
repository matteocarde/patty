
(define (problem pb76)
    (:domain tapes)
    (:objects 
        r - robot
        t01 t02 t03 t04 - tape
        a01 a02 a03 a04 - counter
        c01 c02 c03 c04 c05 c06 c07 c08 - cell
    )
    (:init
        (onTape r t01)
        (onCellRobot r c01)
        (onCellCounter a01 t01 c05) (onCellCounter a02 t02 c05) (onCellCounter a03 t03 c05) (onCellCounter a04 t04 c05)
        (startCell c01)
        (isNextCell c01 c02) (isNextCell c02 c03) (isNextCell c03 c04) (isNextCell c04 c05) (isNextCell c05 c06) (isNextCell c06 c07) (isNextCell c07 c08) (isNextCell c08 c01)
        (isNextTape t01 t02) (isNextTape t02 t03) (isNextTape t03 t04) (isNextTape t04 t01)
        (x04 a01) (x02 a01) (x01 a01) (x03 a02) (x04 a03) (x01 a03) (x03 a04) (x02 a04) (x01 a04)
    )
    (:goal
        (and  
            (or (and (x01 a01) (x01 a02))(and (not (x01 a01)) (not (x01 a02)))) (or (and (x01 a02) (x01 a03))(and (not (x01 a02)) (not (x01 a03)))) (or (and (x01 a03) (x01 a04))(and (not (x01 a03)) (not (x01 a04)))) (or (and (x02 a01) (x02 a02))(and (not (x02 a01)) (not (x02 a02)))) (or (and (x02 a02) (x02 a03))(and (not (x02 a02)) (not (x02 a03)))) (or (and (x02 a03) (x02 a04))(and (not (x02 a03)) (not (x02 a04)))) (or (and (x03 a01) (x03 a02))(and (not (x03 a01)) (not (x03 a02)))) (or (and (x03 a02) (x03 a03))(and (not (x03 a02)) (not (x03 a03)))) (or (and (x03 a03) (x03 a04))(and (not (x03 a03)) (not (x03 a04)))) (or (and (x04 a01) (x04 a02))(and (not (x04 a01)) (not (x04 a02)))) (or (and (x04 a02) (x04 a03))(and (not (x04 a02)) (not (x04 a03)))) (or (and (x04 a03) (x04 a04))(and (not (x04 a03)) (not (x04 a04))))
        )
    )
    )
 