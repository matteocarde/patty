
    (define (problem pb39)
        (:domain tapes)
        (:objects 
            r - robot
            t01 t02 t03 - tape
            a01 a02 a03 - counter
            c01 c02 c03 c04 c05 c06 c07 c08 c09 c10 c11 c12 c13 c14 c15 c16 c17 c18 c19 c20 c21 c22 - cell
        )
        (:init
            (onTape r t01)
            (onCellRobot r c01)
            (onCellCounter a01 t01 c12) (onCellCounter a02 t02 c12) (onCellCounter a03 t03 c12)
            (startCell c01)
            (isNextCell c01 c02) (isNextCell c02 c03) (isNextCell c03 c04) (isNextCell c04 c05) (isNextCell c05 c06) (isNextCell c06 c07) (isNextCell c07 c08) (isNextCell c08 c09) (isNextCell c09 c10) (isNextCell c10 c11) (isNextCell c11 c12) (isNextCell c12 c13) (isNextCell c13 c14) (isNextCell c14 c15) (isNextCell c15 c16) (isNextCell c16 c17) (isNextCell c17 c18) (isNextCell c18 c19) (isNextCell c19 c20) (isNextCell c20 c21) (isNextCell c21 c22) (isNextCell c22 c01)
            (isNextTape t01 t02) (isNextTape t02 t03) (isNextTape t03 t01)
            (x03 a01) (x03 a03)
        )
        (:goal
            (and  
                (or (and (x01 a01) (x01 a02))(and (not (x01 a01)) (not (x01 a02)))) (or (and (x01 a02) (x01 a03))(and (not (x01 a02)) (not (x01 a03)))) (or (and (x02 a01) (x02 a02))(and (not (x02 a01)) (not (x02 a02)))) (or (and (x02 a02) (x02 a03))(and (not (x02 a02)) (not (x02 a03)))) (or (and (x03 a01) (x03 a02))(and (not (x03 a01)) (not (x03 a02)))) (or (and (x03 a02) (x03 a03))(and (not (x03 a02)) (not (x03 a03))))
            )
        )
        )
     