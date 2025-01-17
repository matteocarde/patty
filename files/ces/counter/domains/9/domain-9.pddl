
        (define (domain counter)
            (:requirements :strips :equality :conditional-effects)
            (:types counter)
            (:predicates
                (x01)(x02)(x03)(x04)(x05)(x06)(x07)(x08)(x09)
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
                        (and (not (x05))(x04)(x03)(x02)(x01))
                        (and (x05)(not (x04))(not (x03))(not (x02))(not (x01)))
                    )
                    (when
                        (and (not (x06))(x05)(x04)(x03)(x02)(x01))
                        (and (x06)(not (x05))(not (x04))(not (x03))(not (x02))(not (x01)))
                    )
                    (when
                        (and (not (x07))(x06)(x05)(x04)(x03)(x02)(x01))
                        (and (x07)(not (x06))(not (x05))(not (x04))(not (x03))(not (x02))(not (x01)))
                    )
                    (when
                        (and (not (x08))(x07)(x06)(x05)(x04)(x03)(x02)(x01))
                        (and (x08)(not (x07))(not (x06))(not (x05))(not (x04))(not (x03))(not (x02))(not (x01)))
                    )
                    (when
                        (and (not (x09))(x08)(x07)(x06)(x05)(x04)(x03)(x02)(x01))
                        (and (x09)(not (x08))(not (x07))(not (x06))(not (x05))(not (x04))(not (x03))(not (x02))(not (x01)))
                    )
                    (when
                        (and (x09)(x08)(x07)(x06)(x05)(x04)(x03)(x02)(x01))
                        (and (not (x09))(not (x08))(not (x07))(not (x06))(not (x05))(not (x04))(not (x03))(not (x02))(not (x01)))
                    )
                )
            )
        )
        