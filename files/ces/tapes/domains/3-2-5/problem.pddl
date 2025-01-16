
(define (problem pb3)
    (:domain tapes)
    (:objects 
        r - robot
        t01 t02 - tape
        a01 a02 - counter
        c01 c02 c03 c04 c05 - cell
    )
    (:init
        (onTape r t01)
        (onCellRobot r c01)
        (onCellCounter a01 t01 c03) (onCellCounter a02 t02 c03)
        (startCell c01)
        (isNextCell c01 c02) (isNextCell c02 c03) (isNextCell c03 c04) (isNextCell c04 c05) (isNextCell c05 c01)
        (isNextTape t01 t02) (isNextTape t02 t01)
        (x02 a01) (x03 a02) (x02 a02)
    )
    (:goal
        (and  
            (or (and (x01 a01) (x01 a02))(and (not (x01 a01)) (not (x01 a02)))) (or (and (x02 a01) (x02 a02))(and (not (x02 a01)) (not (x02 a02)))) (or (and (x03 a01) (x03 a02))(and (not (x03 a01)) (not (x03 a02))))
        )
    )
    )
 