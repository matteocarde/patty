(define (problem pb01)
            (:domain counters)
            (:objects sea earth stone atmosphere dust rain earthquake fire lava gunpowder air water geyser wind ocean salt mud obsidian plant sand flood cloud brick sky granite steam pressure energy volcano - element)
            (:init
                (have water)
                (have earth)
                (have fire)
                (have air)
                (combination air air pressure) (combination air fire energy) (combination air earth dust) (combination earth fire lava) (combination air water rain) (combination earth water mud) (combination fire water steam) (combination water water sea) (combination air energy wind) (combination air lava stone) (combination air pressure atmosphere) (combination air steam cloud) (combination earth energy earthquake) (combination dust fire gunpowder) (combination fire sea salt) (combination earth lava volcano) (combination lava pressure granite) (combination lava water obsidian) (combination fire mud brick) (combination earth rain plant) (combination rain rain flood) (combination sea sea ocean) (combination steam earth geyser) (combination air cloud sky) (combination air stone sand)
            )
            (:goal
                (and  (have sand))
            )
            )

                    