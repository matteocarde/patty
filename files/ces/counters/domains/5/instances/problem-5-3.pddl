(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 c3 - counter)
    (:init
        (z c1)(z c2)(z c3)
        (next c1 c2)(next c2 c3)
         ;0 - 00000
        (x05 c1)(x05 c3) ;16 - 10000
    )
    (:goal
        (and  (l01 c1 c2)(l01 c2 c3)(l02 c1 c2)(l02 c2 c3)(l03 c1 c2)(l03 c2 c3)(l04 c1 c2)(l04 c2 c3)(l05 c1 c2)(l05 c2 c3))
    )
    )
            
            