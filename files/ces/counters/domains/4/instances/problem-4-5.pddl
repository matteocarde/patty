(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 c3 c4 c5 - counter)
    (:init
        (z c1)(z c2)(z c3)(z c4)(z c5)
        (next c1 c2)(next c2 c3)(next c3 c4)(next c4 c5)
         ;0 - 0000
        (x04 c1)(x04 c3)(x04 c5) ;8 - 1000
    )
    (:goal
        (and  (l01 c1 c2)(l01 c2 c3)(l01 c3 c4)(l01 c4 c5)(l02 c1 c2)(l02 c2 c3)(l02 c3 c4)(l02 c4 c5)(l03 c1 c2)(l03 c2 c3)(l03 c3 c4)(l03 c4 c5)(l04 c1 c2)(l04 c2 c3)(l04 c3 c4)(l04 c4 c5))
    )
    )
            
            