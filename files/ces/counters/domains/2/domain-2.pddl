
        (define (domain counters)
            (:requirements :strips :equality :conditional-effects)
            (:types counter)
            (:predicates
                (z ?a - counter)
                (next ?a - counter ?b - counter)
                (l01 ?a - counter ?b - counter)(l02 ?a - counter ?b - counter)
                (x01 ?a - counter)(x02 ?a - counter)
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
                        (and (x02 ?a)(x01 ?a))
                        (and (not (x02 ?a))(not (x01 ?a)))
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
                        (and (not (x02 ?a))(not (x01 ?a)))
                        (and (x02 ?a)(x01 ?a))
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
(not (z ?a))
(not (z ?b))
                )
            )
        )
        