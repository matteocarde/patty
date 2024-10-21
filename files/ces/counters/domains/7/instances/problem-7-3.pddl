(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 c3 - counter)
    (:init
        (free c1)(free c2)(free c3)
        (next c1 c2)(next c2 c3)
         ;0 - 0000000
        (x7 c1)(x7 c3) ;64 - 1000000
    )
    (:goal
        (and  (l1 c1 c2)(l1 c2 c3)(l2 c1 c2)(l2 c2 c3)(l3 c1 c2)(l3 c2 c3)(l4 c1 c2)(l4 c2 c3)(l5 c1 c2)(l5 c2 c3)(l6 c1 c2)(l6 c2 c3)(l7 c1 c2)(l7 c2 c3))
    )
    )
            
            