(define (problem pb01)
            (:domain counters)
            (:objects sea earth stone swamp tsunami atmosphere wall dust rain earthquake fire lava gunpowder air fog water geyser explosion isle wind ocean salt metal algae mud obsidian plant mountain sand flood cloud brick sky storm granite steam pressure energy volcano - element)
            (:init
                (have water)
                (have earth)
                (have fire)
                (have air)
                (combination air air pressure) (combination air fire energy) (combination air earth dust) (combination earth fire lava) (combination air water rain) (combination earth water mud) (combination fire water steam) (combination water water sea) (combination air energy wind) (combination air lava stone) (combination air pressure atmosphere) (combination air steam cloud) (combination earth energy earthquake) (combination dust fire gunpowder) (combination fire sea salt) (combination earth lava volcano) (combination lava pressure granite) (combination lava water obsidian) (combination fire mud brick) (combination earth rain plant) (combination rain rain flood) (combination sea sea ocean) (combination steam earth geyser) (combination air cloud sky) (combination air stone sand) (combination brick brick wall) (combination cloud earth fog) (combination earth earthquake mountain) (combination cloud energy storm) (combination fire stone metal) (combination fire gunpowder explosion) (combination mud plant swamp) (combination earthquake ocean tsunami) (combination ocean plant algae) (combination ocean volcano isle)
            )
            (:goal
                (and  (have swamp))
            )
            )

                    