
        (define (domain counter)
            (:requirements :strips :equality :conditional-effects)
            (:types counter)
            (:predicates
                (x01)(x02)(x03)(x04)(x05)(x06)(x07)(x08)(x09)(x10)(x11)(x12)(x13)(x14)
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
                        (and (not (x10))(x09)(x08)(x07)(x06)(x05)(x04)(x03)(x02)(x01))
                        (and (x10)(not (x09))(not (x08))(not (x07))(not (x06))(not (x05))(not (x04))(not (x03))(not (x02))(not (x01)))
                    )
                    (when
                        (and (not (x11))(x10)(x09)(x08)(x07)(x06)(x05)(x04)(x03)(x02)(x01))
                        (and (x11)(not (x10))(not (x09))(not (x08))(not (x07))(not (x06))(not (x05))(not (x04))(not (x03))(not (x02))(not (x01)))
                    )
                    (when
                        (and (not (x12))(x11)(x10)(x09)(x08)(x07)(x06)(x05)(x04)(x03)(x02)(x01))
                        (and (x12)(not (x11))(not (x10))(not (x09))(not (x08))(not (x07))(not (x06))(not (x05))(not (x04))(not (x03))(not (x02))(not (x01)))
                    )
                    (when
                        (and (not (x13))(x12)(x11)(x10)(x09)(x08)(x07)(x06)(x05)(x04)(x03)(x02)(x01))
                        (and (x13)(not (x12))(not (x11))(not (x10))(not (x09))(not (x08))(not (x07))(not (x06))(not (x05))(not (x04))(not (x03))(not (x02))(not (x01)))
                    )
                    (when
                        (and (not (x14))(x13)(x12)(x11)(x10)(x09)(x08)(x07)(x06)(x05)(x04)(x03)(x02)(x01))
                        (and (x14)(not (x13))(not (x12))(not (x11))(not (x10))(not (x09))(not (x08))(not (x07))(not (x06))(not (x05))(not (x04))(not (x03))(not (x02))(not (x01)))
                    )
                    (when
                        (and (x14)(x13)(x12)(x11)(x10)(x09)(x08)(x07)(x06)(x05)(x04)(x03)(x02)(x01))
                        (and (not (x14))(not (x13))(not (x12))(not (x11))(not (x10))(not (x09))(not (x08))(not (x07))(not (x06))(not (x05))(not (x04))(not (x03))(not (x02))(not (x01)))
                    )
                )
            )
        )
        