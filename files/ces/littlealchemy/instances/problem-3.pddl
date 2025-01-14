(define (problem pb01)
            (:domain counters)
            (:objects sea earth stone atmosphere dust rain earthquake fire lava gunpowder air water wind salt mud cloud steam pressure energy - element)
            (:init
                (have water)
                (have earth)
                (have fire)
                (have air)
                (combination air air pressure) (combination air fire energy) (combination air earth dust) (combination earth fire lava) (combination air water rain) (combination earth water mud) (combination fire water steam) (combination water water sea) (combination air energy wind) (combination air lava stone) (combination air pressure atmosphere) (combination air steam cloud) (combination earth energy earthquake) (combination dust fire gunpowder) (combination fire sea salt)
            )
            (:goal
                (and  (have stone))
            )
            )

                    