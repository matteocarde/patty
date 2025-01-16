(define (problem pb01)
(:domain counters)
(:objects c1 c2 - counter)
(:init
    (z c1)(z c2)
    (next c1 c2)
     ;0 - 00
    (x02 c1) ;2 - 10
)
(:goal
    (and  (l01 c1 c2)(l02 c1 c2))
)
)
        
        