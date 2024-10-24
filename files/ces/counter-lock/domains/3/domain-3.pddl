
        (define (domain counter)
            (:requirements :strips :equality :conditional-effects)
            (:predicates
                (x1)(x2)(x3)
                (y1)(y2)(y3)
                (l1)(l2)(l3)
            )

            (:action inx
                :parameters ()
                :precondition()
                :effect(and
                    (when
                        (and (not (x1))(not (l1)))
                        (and (x1))
                    )
                    (when
                        (and (not (x2))(x1)(not (l2))(not (l1)))
                        (and (x2)(not (x1)))
                    )
                    (when
                        (and (not (x3))(x2)(x1)(not (l3))(not (l2))(not (l1)))
                        (and (x3)(not (x2))(not (x1)))
                    )
                    (when
                        (and (x3)(x2)(x1)(not (l3))(not (l2))(not (l1)))
                        (and (not (x3))(not (x2))(not (x1)))
                    )
                )
            )
            (:action iny
                :parameters ()
                :precondition()
                :effect(and
                    (when
                        (and (not (y1))(not (l1)))
                        (and (y1))
                    )
                    (when
                        (and (not (y2))(y1)(not (l2))(not (l1)))
                        (and (y2)(not (y1)))
                    )
                    (when
                        (and (not (y3))(y2)(y1)(not (l3))(not (l2))(not (l1)))
                        (and (y3)(not (y2))(not (y1)))
                    )
                    (when
                        (and (y3)(y2)(y1)(not (l3))(not (l2))(not (l1)))
                        (and (not (y3))(not (y2))(not (y1)))
                    )
                )
            )
            
            (:action dex
                :parameters ()
                :precondition()
                :effect(and
                    (when
                        (and (x1)(not (l1)))
                        (and (not (x1)))
                    )
                    (when
                        (and (x2)(not (x1))(not (l2))(not (l1)))
                        (and (not (x2))(x1))
                    )
                    (when
                        (and (x3)(not (x2))(not (x1))(not (l3))(not (l2))(not (l1)))
                        (and (not (x3))(x2)(x1))
                    )
                    (when
                        (and (not (x3))(not (x2))(not (x1))(not (l3))(not (l2))(not (l1)))
                        (and (x3)(x2)(x1))
                    )
                )
            )
            (:action dey
                :parameters ()
                :precondition()
                :effect(and
                    (when
                        (and (y1)(not (l1)))
                        (and (not (y1)))
                    )
                    (when
                        (and (y2)(not (y1))(not (l2))(not (l1)))
                        (and (not (y2))(y1))
                    )
                    (when
                        (and (y3)(not (y2))(not (y1))(not (l3))(not (l2))(not (l1)))
                        (and (not (y3))(y2)(y1))
                    )
                    (when
                        (and (not (y3))(not (y2))(not (y1))(not (l3))(not (l2))(not (l1)))
                        (and (y3)(y2)(y1))
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
                    (when
                        (and (x3)(y3))
                        (and (l3))
                    )
                    (when
                        (and (not (x3))(not (y3)))
                        (and (l3))
                    )
                )
            )
        )
        