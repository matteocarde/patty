(define (problem pb01)
    (:domain counters)
    (:objects c1 c2 c3 c4 c5 - counter)
    (:init
        (free c1)(free c2)(free c3)(free c4)(free c5)
        (next c1 c2)(next c2 c3)(next c3 c4)(next c4 c5)
         ;0 - 0000000000
        (x10 c1)(x10 c3)(x10 c5) ;512 - 1000000000
    )
    (:goal
        (and  (l1 c1 c2)(l1 c2 c3)(l1 c3 c4)(l1 c4 c5)(l2 c1 c2)(l2 c2 c3)(l2 c3 c4)(l2 c4 c5)(l3 c1 c2)(l3 c2 c3)(l3 c3 c4)(l3 c4 c5)(l4 c1 c2)(l4 c2 c3)(l4 c3 c4)(l4 c4 c5)(l5 c1 c2)(l5 c2 c3)(l5 c3 c4)(l5 c4 c5)(l6 c1 c2)(l6 c2 c3)(l6 c3 c4)(l6 c4 c5)(l7 c1 c2)(l7 c2 c3)(l7 c3 c4)(l7 c4 c5)(l8 c1 c2)(l8 c2 c3)(l8 c3 c4)(l8 c4 c5)(l9 c1 c2)(l9 c2 c3)(l9 c3 c4)(l9 c4 c5)(l10 c1 c2)(l10 c2 c3)(l10 c3 c4)(l10 c4 c5))
    )
    )
            
            