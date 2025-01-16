
(define (problem pb8)
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
        (x01 a01) (x02 a02) (x01 a02) (x01 a03)
    )
    (:goal
        (and  
            (or (and (x01 a01) (x01 a02))(and (not (x01 a01)) (not (x01 a02)))) (or (and (x01 a02) (x01 a03))(and (not (x01 a02)) (not (x01 a03)))) (or (and (x02 a01) (x02 a02))(and (not (x02 a01)) (not (x02 a02)))) (or (and (x02 a02) (x02 a03))(and (not (x02 a02)) (not (x02 a03)))) (or (and (x03 a01) (x03 a02))(and (not (x03 a01)) (not (x03 a02)))) (or (and (x03 a02) (x03 a03))(and (not (x03 a02)) (not (x03 a03))))
        )
    )
    )
 