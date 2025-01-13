(define (problem pb01)
    (:domain counters)
    (:objects
        sea steam water stone lava atmosphere energy air rain mud fire pressure wind earth dust - element
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
    )
    (:goal
        (and (have pressure))
    )
)