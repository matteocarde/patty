(define (problem pb01)
(:domain counters)
(:objects c1 c2 - counter)
(:init
    (z c1)(z c2)
    (next c1 c2)
     ;0 - 000000
    (x06 c1) ;32 - 100000
)
(:goal
    (and  (l01 c1 c2)(l02 c1 c2)(l03 c1 c2)(l04 c1 c2)(l05 c1 c2)(l06 c1 c2))
)
)
        
        