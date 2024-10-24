(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 c3 c4 c5 c6 - counter)
    (:init
        (z c1)(z c2)(z c3)(z c4)(z c5)(z c6)
        (next c1 c2)(next c2 c3)(next c3 c4)(next c4 c5)(next c5 c6)
         ;0 - 00000000
        (x08 c1)(x08 c3)(x08 c5) ;128 - 10000000
    )
    (:goal
        (and  (l01 c1 c2)(l01 c2 c3)(l01 c3 c4)(l01 c4 c5)(l01 c5 c6)(l02 c1 c2)(l02 c2 c3)(l02 c3 c4)(l02 c4 c5)(l02 c5 c6)(l03 c1 c2)(l03 c2 c3)(l03 c3 c4)(l03 c4 c5)(l03 c5 c6)(l04 c1 c2)(l04 c2 c3)(l04 c3 c4)(l04 c4 c5)(l04 c5 c6)(l05 c1 c2)(l05 c2 c3)(l05 c3 c4)(l05 c4 c5)(l05 c5 c6)(l06 c1 c2)(l06 c2 c3)(l06 c3 c4)(l06 c4 c5)(l06 c5 c6)(l07 c1 c2)(l07 c2 c3)(l07 c3 c4)(l07 c4 c5)(l07 c5 c6)(l08 c1 c2)(l08 c2 c3)(l08 c3 c4)(l08 c4 c5)(l08 c5 c6))
    )
    )
            
            