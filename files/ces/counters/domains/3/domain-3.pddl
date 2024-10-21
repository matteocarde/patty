
        (define (domain counters)
            (:requirements :strips :equality :conditional-effects)
            (:types counter)
            (:predicates
                (free ?a - counter)
                (next ?a - counter ?b - counter)
                (l1 ?a - counter ?b - counter)(l2 ?a - counter ?b - counter)(l3 ?a - counter ?b - counter)
                (x1 ?a - counter)(x2 ?a - counter)(x3 ?a - counter)
            )

            (:action incr
                :parameters (?a - counter)
                :precondition(and (free ?a))
                :effect(and
                    (when
                        (and (not (x2 ?a))(x1 ?a))
                        (and (x2 ?a)(not (x1 ?a)))
                    )
                    (when
                        (and (not (x3 ?a))(x2 ?a)(x1 ?a))
                        (and (x3 ?a)(not (x2 ?a))(not (x1 ?a)))
                    )
                    (when
                        (and (x3 ?a)(x2 ?a)(x1 ?a))
                        (and (not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                    )
                )
            )
            
            (:action decr
                :parameters (?a - counter)
                :precondition(and (free ?a))
                :effect(and
                    (when
                        (and (x2 ?a)(not (x1 ?a)))
                        (and (not (x2 ?a))(x1 ?a))
                    )
                    (when
                        (and (x3 ?a)(not (x2 ?a))(not (x1 ?a)))
                        (and (not (x3 ?a))(x2 ?a)(x1 ?a))
                    )
                    (when
                        (and (not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                        (and (x3 ?a)(x2 ?a)(x1 ?a))
                    )
                )
            )
            
            (:action lck
                :parameters (?a - counter ?b - counter)
                :precondition(and (next ?a ?b))
                :effect(and
                    (when
                        (and (x1 ?a)(x1 ?b))
                        (and (l1 ?a ?b))
                    )
                    (when
                        (and (not (x1 ?a))(not (x1 ?b)))
                        (and (l1 ?a ?b))
                    )
                    (when
                        (and (x2 ?a)(x2 ?b))
                        (and (l2 ?a ?b))
                    )
                    (when
                        (and (not (x2 ?a))(not (x2 ?b)))
                        (and (l2 ?a ?b))
                    )
                    (when
                        (and (x3 ?a)(x3 ?b))
                        (and (l3 ?a ?b))
                    )
                    (when
                        (and (not (x3 ?a))(not (x3 ?b)))
                        (and (l3 ?a ?b))
                    )
(not (free ?a))
(not (free ?b))
                )
            )
        )
        