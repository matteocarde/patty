(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 c3 - counter)
    (:init
        (free c1)(free c2)(free c3)
        (next c1 c2)(next c2 c3)
         ;0 - 000
        (x3 c1)(x3 c3) ;4 - 100
    )
    (:goal
        (and  (l1 c1 c2)(l1 c2 c3)(l2 c1 c2)(l2 c2 c3)(l3 c1 c2)(l3 c2 c3))
    )
    )
            
            