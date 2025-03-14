
        (define (domain counter)
            (:requirements :strips :equality :conditional-effects)
            (:types counter)
            (:predicates
                (x01)(x02)(x03)(x04)
            )

            (:action incr
                :parameters ()
                :precondition()
                :effect(and
                    (when
                        (and (not (x01)))
                        (and (x01))
                    )
                    (when
                        (and (not (x02))(x01))
                        (and (x02)(not (x01)))
                    )
                    (when
                        (and (not (x03))(x02)(x01))
                        (and (x03)(not (x02))(not (x01)))
                    )
                    (when
                        (and (not (x04))(x03)(x02)(x01))
                        (and (x04)(not (x03))(not (x02))(not (x01)))
                    )
                    (when
                        (and (x04)(x03)(x02)(x01))
                        (and (not (x04))(not (x03))(not (x02))(not (x01)))
                    )
                )
            )
        )
        