(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 - counter)
    (:init
        (z c1)(z c2)
        (next c1 c2)
         ;0 - 00000000
        (x08 c1) ;128 - 10000000
    )
    (:goal
        (and  (l01 c1 c2)(l02 c1 c2)(l03 c1 c2)(l04 c1 c2)(l05 c1 c2)(l06 c1 c2)(l07 c1 c2)(l08 c1 c2))
    )
    )
            
            