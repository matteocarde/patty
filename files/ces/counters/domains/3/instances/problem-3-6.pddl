(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 c3 c4 c5 c6 - counter)
    (:init
        (z c1)(z c2)(z c3)(z c4)(z c5)(z c6)
        (next c1 c2)(next c2 c3)(next c3 c4)(next c4 c5)(next c5 c6)
         ;0 - 000
        (x3 c1)(x3 c3)(x3 c5) ;4 - 100
    )
    (:goal
        (and  (l1 c1 c2)(l1 c2 c3)(l1 c3 c4)(l1 c4 c5)(l1 c5 c6)(l2 c1 c2)(l2 c2 c3)(l2 c3 c4)(l2 c4 c5)(l2 c5 c6)(l3 c1 c2)(l3 c2 c3)(l3 c3 c4)(l3 c4 c5)(l3 c5 c6))
    )
    )
            
            