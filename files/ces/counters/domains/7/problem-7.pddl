(define (problem pb01)
(:domain counters)
(:objects c1 c2 - counter)
(:init
    (z c1)(z c2)
    (next c1 c2)
     ;0 - 0000000
    (x07 c1) ;64 - 1000000
)
(:goal
    (and  (l01 c1 c2)(l02 c1 c2)(l03 c1 c2)(l04 c1 c2)(l05 c1 c2)(l06 c1 c2)(l07 c1 c2))
)
)
        
        