(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 c3 c4 - counter)
    (:init
        (z c1)(z c2)(z c3)(z c4)
        (next c1 c2)(next c2 c3)(next c3 c4)
         ;0 - 000000
        (x6 c1)(x6 c3) ;32 - 100000
    )
    (:goal
        (and  (l1 c1 c2)(l1 c2 c3)(l1 c3 c4)(l2 c1 c2)(l2 c2 c3)(l2 c3 c4)(l3 c1 c2)(l3 c2 c3)(l3 c3 c4)(l4 c1 c2)(l4 c2 c3)(l4 c3 c4)(l5 c1 c2)(l5 c2 c3)(l5 c3 c4)(l6 c1 c2)(l6 c2 c3)(l6 c3 c4))
    )
    )
            
            