(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 - counter)
    (:init
        (z c1)(z c2)
        (next c1 c2)
         ;0 - 000
        (x03 c1) ;4 - 100
    )
    (:goal
        (and  (l01 c1 c2)(l02 c1 c2)(l03 c1 c2))
    )
    )
            
            