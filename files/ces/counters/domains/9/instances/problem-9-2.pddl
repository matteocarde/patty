(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 - counter)
    (:init
        (z c1)(z c2)
        (next c1 c2)
         ;0 - 000000000
        (x9 c1) ;256 - 100000000
    )
    (:goal
        (and  (l1 c1 c2)(l2 c1 c2)(l3 c1 c2)(l4 c1 c2)(l5 c1 c2)(l6 c1 c2)(l7 c1 c2)(l8 c1 c2)(l9 c1 c2))
    )
    )
            
            