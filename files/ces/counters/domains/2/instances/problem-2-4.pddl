(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 c3 c4 - counter)
    (:init
        (z c1)(z c2)(z c3)(z c4)
        (next c1 c2)(next c2 c3)(next c3 c4)
         ;0 - 00
        (x02 c1)(x02 c3) ;2 - 10
    )
    (:goal
        (and  (l01 c1 c2)(l01 c2 c3)(l01 c3 c4)(l02 c1 c2)(l02 c2 c3)(l02 c3 c4))
    )
    )
            
            