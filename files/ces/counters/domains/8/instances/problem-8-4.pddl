(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 c3 c4 - counter)
    (:init
        (z c1)(z c2)(z c3)(z c4)
        (next c1 c2)(next c2 c3)(next c3 c4)
         ;0 - 00000000
        (x8 c1)(x8 c3) ;128 - 10000000
    )
    (:goal
        (and  (l1 c1 c2)(l1 c2 c3)(l1 c3 c4)(l2 c1 c2)(l2 c2 c3)(l2 c3 c4)(l3 c1 c2)(l3 c2 c3)(l3 c3 c4)(l4 c1 c2)(l4 c2 c3)(l4 c3 c4)(l5 c1 c2)(l5 c2 c3)(l5 c3 c4)(l6 c1 c2)(l6 c2 c3)(l6 c3 c4)(l7 c1 c2)(l7 c2 c3)(l7 c3 c4)(l8 c1 c2)(l8 c2 c3)(l8 c3 c4))
    )
    )
            
            