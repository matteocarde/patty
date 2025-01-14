(define (problem pb01)
    (:domain counters)
    (:objects
        water earth dust pressure rain fire lava air energy - element
    )
    (:init
        (have water)
        (have earth)
        (have fire)
        (have air)
        (combination air air pressure)
        (combination air fire energy)
        (combination air earth dust)
        (combination earth fire lava)
        (combination air water rain)
    )
    (:goal
        (and (have dust))
    )
)