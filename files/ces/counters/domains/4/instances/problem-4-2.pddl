(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 - counter)
    (:init
        (free c1)(free c2)
        (next c1 c2)
         ;0 - 0000
        (x4 c1) ;8 - 1000
    )
    (:goal
        (and  (l1 c1 c2)(l2 c1 c2)(l3 c1 c2)(l4 c1 c2))
    )
    )
            
            