
        (define (domain counter)
            (:requirements :strips :equality :conditional-effects)
            (:predicates
                (ok)
                (l1)(l2)(l3)(l4)(l5)(l6)
                (x1)(x2)(x3)(x4)(x5)(x6)
                (y1)(y2)(y3)(y4)(y5)(y6)
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
                        (and (not (x3))(x2)(x1))
                        (and (x3)(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x4))(x3)(x2)(x1))
                        (and (x4)(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x5))(x4)(x3)(x2)(x1))
                        (and (x5)(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x6))(x5)(x4)(x3)(x2)(x1))
                        (and (x6)(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (x6)(x5)(x4)(x3)(x2)(x1))
                        (and (not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
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
                        (and (not (y3))(y2)(y1))
                        (and (y3)(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y4))(y3)(y2)(y1))
                        (and (y4)(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y5))(y4)(y3)(y2)(y1))
                        (and (y5)(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y6))(y5)(y4)(y3)(y2)(y1))
                        (and (y6)(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (y6)(y5)(y4)(y3)(y2)(y1))
                        (and (not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
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
                        (and (x3)(not (x2))(not (x1)))
                        (and (not (x3))(x2)(x1))
                    )
                    (when
                        (and (x4)(not (x3))(not (x2))(not (x1)))
                        (and (not (x4))(x3)(x2)(x1))
                    )
                    (when
                        (and (x5)(not (x4))(not (x3))(not (x2))(not (x1)))
                        (and (not (x5))(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (x6)(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                        (and (not (x6))(x5)(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                        (and (x6)(x5)(x4)(x3)(x2)(x1))
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
                        (and (y3)(not (y2))(not (y1)))
                        (and (not (y3))(y2)(y1))
                    )
                    (when
                        (and (y4)(not (y3))(not (y2))(not (y1)))
                        (and (not (y4))(y3)(y2)(y1))
                    )
                    (when
                        (and (y5)(not (y4))(not (y3))(not (y2))(not (y1)))
                        (and (not (y5))(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (y6)(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                        (and (not (y6))(y5)(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                        (and (y6)(y5)(y4)(y3)(y2)(y1))
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
                    (when
                        (and (x4)(y4))
                        (and (l4))
                    )
                    (when
                        (and (not (x4))(not (y4)))
                        (and (l4))
                    )
                    (when
                        (and (x5)(y5))
                        (and (l5))
                    )
                    (when
                        (and (not (x5))(not (y5)))
                        (and (l5))
                    )
                    (when
                        (and (x6)(y6))
                        (and (l6))
                    )
                    (when
                        (and (not (x6))(not (y6)))
                        (and (l6))
                    )
(not (ok))
                )
            )
        )
        