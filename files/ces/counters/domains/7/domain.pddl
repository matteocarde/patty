
        (define (domain counters)
            (:requirements :strips :equality :conditional-effects)
            (:types counter)
            (:predicates
                (z ?a - counter)
                (next ?a - counter ?b - counter)
                (l01 ?a - counter ?b - counter)(l02 ?a - counter ?b - counter)(l03 ?a - counter ?b - counter)(l04 ?a - counter ?b - counter)(l05 ?a - counter ?b - counter)(l06 ?a - counter ?b - counter)(l07 ?a - counter ?b - counter)
                (x01 ?a - counter)(x02 ?a - counter)(x03 ?a - counter)(x04 ?a - counter)(x05 ?a - counter)(x06 ?a - counter)(x07 ?a - counter)
            )

            (:action incr
                :parameters (?a - counter)
                :precondition(and (z ?a))
                :effect(and
                    (when
                        (and (not (x01 ?a)))
                        (and (x01 ?a))
                    )
                    (when
                        (and (not (x02 ?a))(x01 ?a))
                        (and (x02 ?a)(not (x01 ?a)))
                    )
                    (when
                        (and (not (x03 ?a))(x02 ?a)(x01 ?a))
                        (and (x03 ?a)(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (not (x04 ?a))(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (x04 ?a)(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (not (x05 ?a))(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (x05 ?a)(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (not (x06 ?a))(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (x06 ?a)(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (not (x07 ?a))(x06 ?a)(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (x07 ?a)(not (x06 ?a))(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (x07 ?a)(x06 ?a)(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (not (x07 ?a))(not (x06 ?a))(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                )
            )
            
            (:action decr
                :parameters (?a - counter)
                :precondition(and (z ?a))
                :effect(and
                    (when
                        (and (x01 ?a))
                        (and (not (x01 ?a)))
                    )
                    (when
                        (and (x02 ?a)(not (x01 ?a)))
                        (and (not (x02 ?a))(x01 ?a))
                    )
                    (when
                        (and (x03 ?a)(not (x02 ?a))(not (x01 ?a)))
                        (and (not (x03 ?a))(x02 ?a)(x01 ?a))
                    )
                    (when
                        (and (x04 ?a)(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                        (and (not (x04 ?a))(x03 ?a)(x02 ?a)(x01 ?a))
                    )
                    (when
                        (and (x05 ?a)(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                        (and (not (x05 ?a))(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                    )
                    (when
                        (and (x06 ?a)(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                        (and (not (x06 ?a))(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                    )
                    (when
                        (and (x07 ?a)(not (x06 ?a))(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                        (and (not (x07 ?a))(x06 ?a)(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                    )
                    (when
                        (and (not (x07 ?a))(not (x06 ?a))(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                        (and (x07 ?a)(x06 ?a)(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                    )
                )
            )
            
            (:action lck
                :parameters (?a - counter ?b - counter)
                :precondition(and (next ?a ?b))
                :effect(and
                    (when
                        (and (x01 ?a)(x01 ?b))
                        (and (l01 ?a ?b))
                    )
                    (when
                        (and (not (x01 ?a))(not (x01 ?b)))
                        (and (l01 ?a ?b))
                    )
                    (when
                        (and (x02 ?a)(x02 ?b))
                        (and (l02 ?a ?b))
                    )
                    (when
                        (and (not (x02 ?a))(not (x02 ?b)))
                        (and (l02 ?a ?b))
                    )
                    (when
                        (and (x03 ?a)(x03 ?b))
                        (and (l03 ?a ?b))
                    )
                    (when
                        (and (not (x03 ?a))(not (x03 ?b)))
                        (and (l03 ?a ?b))
                    )
                    (when
                        (and (x04 ?a)(x04 ?b))
                        (and (l04 ?a ?b))
                    )
                    (when
                        (and (not (x04 ?a))(not (x04 ?b)))
                        (and (l04 ?a ?b))
                    )
                    (when
                        (and (x05 ?a)(x05 ?b))
                        (and (l05 ?a ?b))
                    )
                    (when
                        (and (not (x05 ?a))(not (x05 ?b)))
                        (and (l05 ?a ?b))
                    )
                    (when
                        (and (x06 ?a)(x06 ?b))
                        (and (l06 ?a ?b))
                    )
                    (when
                        (and (not (x06 ?a))(not (x06 ?b)))
                        (and (l06 ?a ?b))
                    )
                    (when
                        (and (x07 ?a)(x07 ?b))
                        (and (l07 ?a ?b))
                    )
                    (when
                        (and (not (x07 ?a))(not (x07 ?b)))
                        (and (l07 ?a ?b))
                    )
(not (z ?a))
(not (z ?b))
                )
            )
        )
        