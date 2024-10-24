(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 c3 c4 - counter)
    (:init
        (z c1)(z c2)(z c3)(z c4)
        (next c1 c2)(next c2 c3)(next c3 c4)
         ;0 - 000000000000
        (x12 c1)(x12 c3) ;2048 - 100000000000
    )
    (:goal
        (and  (l01 c1 c2)(l01 c2 c3)(l01 c3 c4)(l02 c1 c2)(l02 c2 c3)(l02 c3 c4)(l03 c1 c2)(l03 c2 c3)(l03 c3 c4)(l04 c1 c2)(l04 c2 c3)(l04 c3 c4)(l05 c1 c2)(l05 c2 c3)(l05 c3 c4)(l06 c1 c2)(l06 c2 c3)(l06 c3 c4)(l07 c1 c2)(l07 c2 c3)(l07 c3 c4)(l08 c1 c2)(l08 c2 c3)(l08 c3 c4)(l09 c1 c2)(l09 c2 c3)(l09 c3 c4)(l10 c1 c2)(l10 c2 c3)(l10 c3 c4)(l11 c1 c2)(l11 c2 c3)(l11 c3 c4)(l12 c1 c2)(l12 c2 c3)(l12 c3 c4))
    )
    )
            
            