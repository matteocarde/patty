(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 - counter)
    (:init
        (free c1)(free c2)
        (next c1 c2)
         ;0 - 000
        (x3 c1) ;4 - 100
    )
    (:goal
        (and  (l1 c1 c2)(l2 c1 c2)(l3 c1 c2))
    )
    )
            
            