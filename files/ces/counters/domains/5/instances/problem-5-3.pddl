(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 c3 - counter)
    (:init
        (z c1)(z c2)(z c3)
        (next c1 c2)(next c2 c3)
         ;0 - 00000
        (x5 c1)(x5 c3) ;16 - 10000
    )
    (:goal
        (and  (l1 c1 c2)(l1 c2 c3)(l2 c1 c2)(l2 c2 c3)(l3 c1 c2)(l3 c2 c3)(l4 c1 c2)(l4 c2 c3)(l5 c1 c2)(l5 c2 c3))
    )
    )
            
            