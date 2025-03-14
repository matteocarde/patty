(define (problem pb01)
    (:domain counters)
    (:objects
        water earth fire air - primary
        sea stone mud wind steam dust pressure rain lava energy - element
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
        (combination earth water mud)
        (combination fire water steam)
        (combination water water sea)
        (combination air energy wind)
        (combination air lava stone)
    )
    (:goal
        (and (have stone))
    )
)