(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 c3 - counter)
    (:init
        (z c1)(z c2)(z c3)
        (next c1 c2)(next c2 c3)
         ;0 - 00
        (x2 c1)(x2 c3) ;2 - 10
    )
    (:goal
        (and  (l1 c1 c2)(l1 c2 c3)(l2 c1 c2)(l2 c2 c3))
    )
    )
            
            