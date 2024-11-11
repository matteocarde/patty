
        (define (domain counter)
            (:requirements :strips :equality :conditional-effects)
            (:predicates
                (ok)
                (l1)(l2)
                (x1)(x2)
                (y1)(y2)
            )

            (:action inx
                :parameters ()
                :precondition(and (ok))
                :effect(and
                    (when
                        (and (not (x1)))
                        (and (x1))
                    )
                    (when
                        (and (not (x2))(x1))
                        (and (x2)(not (x1)))
                    )
                    (when
                        (and (x2)(x1))
                        (and (not (x2))(not (x1)))
                    )
                )
            )
            (:action iny
                :parameters ()
                :precondition(and (ok))
                :effect(and
                    (when
                        (and (not (y1)))
                        (and (y1))
                    )
                    (when
                        (and (not (y2))(y1))
                        (and (y2)(not (y1)))
                    )
                    (when
                        (and (y2)(y1))
                        (and (not (y2))(not (y1)))
                    )
                )
            )
            
            (:action dex
                :parameters ()
                :precondition(and (ok))
                :effect(and
                    (when
                        (and (x1))
                        (and (not (x1)))
                    )
                    (when
                        (and (x2)(not (x1)))
                        (and (not (x2))(x1))
                    )
                    (when
                        (and (not (x2))(not (x1)))
                        (and (x2)(x1))
                    )
                )
            )
            (:action dey
                :parameters ()
                :precondition(and (ok))
                :effect(and
                    (when
                        (and (y1))
                        (and (not (y1)))
                    )
                    (when
                        (and (y2)(not (y1)))
                        (and (not (y2))(y1))
                    )
                    (when
                        (and (not (y2))(not (y1)))
                        (and (y2)(y1))
                    )
                )
            )
            (:action lck
                :parameters ()
                :precondition()
                :effect(and
                    (when
                        (and (x1)(y1))
                        (and (l1))
                    )
                    (when
                        (and (not (x1))(not (y1)))
                        (and (l1))
                    )
                    (when
                        (and (x2)(y2))
                        (and (l2))
                    )
                    (when
                        (and (not (x2))(not (y2)))
                        (and (l2))
                    )
(not (ok))
                )
            )
        )
        