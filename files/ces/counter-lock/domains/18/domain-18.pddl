
        (define (domain counter)
            (:requirements :strips :equality :conditional-effects)
            (:predicates
                (x1)(x2)(x3)(x4)(x5)(x6)(x7)(x8)(x9)(x10)(x11)(x12)(x13)(x14)(x15)(x16)(x17)(x18)
                (y1)(y2)(y3)(y4)(y5)(y6)(y7)(y8)(y9)(y10)(y11)(y12)(y13)(y14)(y15)(y16)(y17)(y18)
                (l1)(l2)(l3)(l4)(l5)(l6)(l7)(l8)(l9)(l10)(l11)(l12)(l13)(l14)(l15)(l16)(l17)(l18)
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
                        (and (not (x4))(x3)(x2)(x1)(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x4)(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x5))(x4)(x3)(x2)(x1)(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x5)(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x6))(x5)(x4)(x3)(x2)(x1)(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x6)(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x7))(x6)(x5)(x4)(x3)(x2)(x1)(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x7)(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x8))(x7)(x6)(x5)(x4)(x3)(x2)(x1)(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x8)(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x9))(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1)(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x9)(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x10))(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1)(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x10)(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x11))(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1)(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x11)(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x12))(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1)(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x12)(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x13))(x12)(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1)(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x13)(not (x12))(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x14))(x13)(x12)(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1)(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x14)(not (x13))(not (x12))(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x15))(x14)(x13)(x12)(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1)(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x15)(not (x14))(not (x13))(not (x12))(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x16))(x15)(x14)(x13)(x12)(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1)(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x16)(not (x15))(not (x14))(not (x13))(not (x12))(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x17))(x16)(x15)(x14)(x13)(x12)(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1)(not (l17))(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x17)(not (x16))(not (x15))(not (x14))(not (x13))(not (x12))(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (not (x18))(x17)(x16)(x15)(x14)(x13)(x12)(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1)(not (l18))(not (l17))(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x18)(not (x17))(not (x16))(not (x15))(not (x14))(not (x13))(not (x12))(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
                    )
                    (when
                        (and (x18)(x17)(x16)(x15)(x14)(x13)(x12)(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1)(not (l18))(not (l17))(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x18))(not (x17))(not (x16))(not (x15))(not (x14))(not (x13))(not (x12))(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1)))
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
                        (and (not (y4))(y3)(y2)(y1)(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y4)(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y5))(y4)(y3)(y2)(y1)(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y5)(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y6))(y5)(y4)(y3)(y2)(y1)(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y6)(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y7))(y6)(y5)(y4)(y3)(y2)(y1)(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y7)(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y8))(y7)(y6)(y5)(y4)(y3)(y2)(y1)(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y8)(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y9))(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1)(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y9)(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y10))(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1)(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y10)(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y11))(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1)(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y11)(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y12))(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1)(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y12)(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y13))(y12)(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1)(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y13)(not (y12))(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y14))(y13)(y12)(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1)(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y14)(not (y13))(not (y12))(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y15))(y14)(y13)(y12)(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1)(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y15)(not (y14))(not (y13))(not (y12))(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y16))(y15)(y14)(y13)(y12)(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1)(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y16)(not (y15))(not (y14))(not (y13))(not (y12))(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y17))(y16)(y15)(y14)(y13)(y12)(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1)(not (l17))(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y17)(not (y16))(not (y15))(not (y14))(not (y13))(not (y12))(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (not (y18))(y17)(y16)(y15)(y14)(y13)(y12)(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1)(not (l18))(not (l17))(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y18)(not (y17))(not (y16))(not (y15))(not (y14))(not (y13))(not (y12))(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
                    )
                    (when
                        (and (y18)(y17)(y16)(y15)(y14)(y13)(y12)(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1)(not (l18))(not (l17))(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y18))(not (y17))(not (y16))(not (y15))(not (y14))(not (y13))(not (y12))(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1)))
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
                        (and (x4)(not (x3))(not (x2))(not (x1))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x4))(x3)(x2)(x1))
                    )
                    (when
                        (and (x5)(not (x4))(not (x3))(not (x2))(not (x1))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x5))(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (x6)(not (x5))(not (x4))(not (x3))(not (x2))(not (x1))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x6))(x5)(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (x7)(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x7))(x6)(x5)(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (x8)(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x8))(x7)(x6)(x5)(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (x9)(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x9))(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (x10)(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x10))(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (x11)(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x11))(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (x12)(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x12))(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (x13)(not (x12))(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x13))(x12)(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (x14)(not (x13))(not (x12))(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x14))(x13)(x12)(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (x15)(not (x14))(not (x13))(not (x12))(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x15))(x14)(x13)(x12)(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (x16)(not (x15))(not (x14))(not (x13))(not (x12))(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1))(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x16))(x15)(x14)(x13)(x12)(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (x17)(not (x16))(not (x15))(not (x14))(not (x13))(not (x12))(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1))(not (l17))(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x17))(x16)(x15)(x14)(x13)(x12)(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (x18)(not (x17))(not (x16))(not (x15))(not (x14))(not (x13))(not (x12))(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1))(not (l18))(not (l17))(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (x18))(x17)(x16)(x15)(x14)(x13)(x12)(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1))
                    )
                    (when
                        (and (not (x18))(not (x17))(not (x16))(not (x15))(not (x14))(not (x13))(not (x12))(not (x11))(not (x10))(not (x9))(not (x8))(not (x7))(not (x6))(not (x5))(not (x4))(not (x3))(not (x2))(not (x1))(not (l18))(not (l17))(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (x18)(x17)(x16)(x15)(x14)(x13)(x12)(x11)(x10)(x9)(x8)(x7)(x6)(x5)(x4)(x3)(x2)(x1))
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
                        (and (y4)(not (y3))(not (y2))(not (y1))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y4))(y3)(y2)(y1))
                    )
                    (when
                        (and (y5)(not (y4))(not (y3))(not (y2))(not (y1))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y5))(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (y6)(not (y5))(not (y4))(not (y3))(not (y2))(not (y1))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y6))(y5)(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (y7)(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y7))(y6)(y5)(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (y8)(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y8))(y7)(y6)(y5)(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (y9)(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y9))(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (y10)(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y10))(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (y11)(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y11))(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (y12)(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y12))(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (y13)(not (y12))(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y13))(y12)(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (y14)(not (y13))(not (y12))(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y14))(y13)(y12)(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (y15)(not (y14))(not (y13))(not (y12))(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y15))(y14)(y13)(y12)(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (y16)(not (y15))(not (y14))(not (y13))(not (y12))(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1))(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y16))(y15)(y14)(y13)(y12)(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (y17)(not (y16))(not (y15))(not (y14))(not (y13))(not (y12))(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1))(not (l17))(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y17))(y16)(y15)(y14)(y13)(y12)(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (y18)(not (y17))(not (y16))(not (y15))(not (y14))(not (y13))(not (y12))(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1))(not (l18))(not (l17))(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (not (y18))(y17)(y16)(y15)(y14)(y13)(y12)(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1))
                    )
                    (when
                        (and (not (y18))(not (y17))(not (y16))(not (y15))(not (y14))(not (y13))(not (y12))(not (y11))(not (y10))(not (y9))(not (y8))(not (y7))(not (y6))(not (y5))(not (y4))(not (y3))(not (y2))(not (y1))(not (l18))(not (l17))(not (l16))(not (l15))(not (l14))(not (l13))(not (l12))(not (l11))(not (l10))(not (l9))(not (l8))(not (l7))(not (l6))(not (l5))(not (l4))(not (l3))(not (l2))(not (l1)))
                        (and (y18)(y17)(y16)(y15)(y14)(y13)(y12)(y11)(y10)(y9)(y8)(y7)(y6)(y5)(y4)(y3)(y2)(y1))
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
                    (when
                        (and (x7)(y7))
                        (and (l7))
                    )
                    (when
                        (and (not (x7))(not (y7)))
                        (and (l7))
                    )
                    (when
                        (and (x8)(y8))
                        (and (l8))
                    )
                    (when
                        (and (not (x8))(not (y8)))
                        (and (l8))
                    )
                    (when
                        (and (x9)(y9))
                        (and (l9))
                    )
                    (when
                        (and (not (x9))(not (y9)))
                        (and (l9))
                    )
                    (when
                        (and (x10)(y10))
                        (and (l10))
                    )
                    (when
                        (and (not (x10))(not (y10)))
                        (and (l10))
                    )
                    (when
                        (and (x11)(y11))
                        (and (l11))
                    )
                    (when
                        (and (not (x11))(not (y11)))
                        (and (l11))
                    )
                    (when
                        (and (x12)(y12))
                        (and (l12))
                    )
                    (when
                        (and (not (x12))(not (y12)))
                        (and (l12))
                    )
                    (when
                        (and (x13)(y13))
                        (and (l13))
                    )
                    (when
                        (and (not (x13))(not (y13)))
                        (and (l13))
                    )
                    (when
                        (and (x14)(y14))
                        (and (l14))
                    )
                    (when
                        (and (not (x14))(not (y14)))
                        (and (l14))
                    )
                    (when
                        (and (x15)(y15))
                        (and (l15))
                    )
                    (when
                        (and (not (x15))(not (y15)))
                        (and (l15))
                    )
                    (when
                        (and (x16)(y16))
                        (and (l16))
                    )
                    (when
                        (and (not (x16))(not (y16)))
                        (and (l16))
                    )
                    (when
                        (and (x17)(y17))
                        (and (l17))
                    )
                    (when
                        (and (not (x17))(not (y17)))
                        (and (l17))
                    )
                    (when
                        (and (x18)(y18))
                        (and (l18))
                    )
                    (when
                        (and (not (x18))(not (y18)))
                        (and (l18))
                    )
                )
            )
        )
        