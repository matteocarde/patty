
        (define (domain counters)
            (:requirements :strips :equality :conditional-effects)
            (:types counter)
            (:predicates
                (z ?a - counter)
                (next ?a - counter ?b - counter)
                (l1 ?a - counter ?b - counter)(l2 ?a - counter ?b - counter)(l3 ?a - counter ?b - counter)(l4 ?a - counter ?b - counter)(l5 ?a - counter ?b - counter)(l6 ?a - counter ?b - counter)(l7 ?a - counter ?b - counter)(l8 ?a - counter ?b - counter)(l9 ?a - counter ?b - counter)
                (x1 ?a - counter)(x2 ?a - counter)(x3 ?a - counter)(x4 ?a - counter)(x5 ?a - counter)(x6 ?a - counter)(x7 ?a - counter)(x8 ?a - counter)(x9 ?a - counter)
            )

            (:action incr
                :parameters (?a - counter)
                :precondition(and (z ?a))
                :effect(and
                    (when
                        (and (not (x1 ?a)))
                        (and (x1 ?a))
                    )
                    (when
                        (and (not (x2 ?a))(x1 ?a))
                        (and (x2 ?a)(not (x1 ?a)))
                    )
                    (when
                        (and (not (x3 ?a))(x2 ?a)(x1 ?a))
                        (and (x3 ?a)(not (x2 ?a))(not (x1 ?a)))
                    )
                    (when
                        (and (not (x4 ?a))(x3 ?a)(x2 ?a)(x1 ?a))
                        (and (x4 ?a)(not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                    )
                    (when
                        (and (not (x5 ?a))(x4 ?a)(x3 ?a)(x2 ?a)(x1 ?a))
                        (and (x5 ?a)(not (x4 ?a))(not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                    )
                    (when
                        (and (not (x6 ?a))(x5 ?a)(x4 ?a)(x3 ?a)(x2 ?a)(x1 ?a))
                        (and (x6 ?a)(not (x5 ?a))(not (x4 ?a))(not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                    )
                    (when
                        (and (not (x7 ?a))(x6 ?a)(x5 ?a)(x4 ?a)(x3 ?a)(x2 ?a)(x1 ?a))
                        (and (x7 ?a)(not (x6 ?a))(not (x5 ?a))(not (x4 ?a))(not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                    )
                    (when
                        (and (not (x8 ?a))(x7 ?a)(x6 ?a)(x5 ?a)(x4 ?a)(x3 ?a)(x2 ?a)(x1 ?a))
                        (and (x8 ?a)(not (x7 ?a))(not (x6 ?a))(not (x5 ?a))(not (x4 ?a))(not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                    )
                    (when
                        (and (not (x9 ?a))(x8 ?a)(x7 ?a)(x6 ?a)(x5 ?a)(x4 ?a)(x3 ?a)(x2 ?a)(x1 ?a))
                        (and (x9 ?a)(not (x8 ?a))(not (x7 ?a))(not (x6 ?a))(not (x5 ?a))(not (x4 ?a))(not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                    )
                    (when
                        (and (x9 ?a)(x8 ?a)(x7 ?a)(x6 ?a)(x5 ?a)(x4 ?a)(x3 ?a)(x2 ?a)(x1 ?a))
                        (and (not (x9 ?a))(not (x8 ?a))(not (x7 ?a))(not (x6 ?a))(not (x5 ?a))(not (x4 ?a))(not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                    )
                )
            )
            
            (:action decr
                :parameters (?a - counter)
                :precondition(and (z ?a))
                :effect(and
                    (when
                        (and (x1 ?a))
                        (and (not (x1 ?a)))
                    )
                    (when
                        (and (x2 ?a)(not (x1 ?a)))
                        (and (not (x2 ?a))(x1 ?a))
                    )
                    (when
                        (and (x3 ?a)(not (x2 ?a))(not (x1 ?a)))
                        (and (not (x3 ?a))(x2 ?a)(x1 ?a))
                    )
                    (when
                        (and (x4 ?a)(not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                        (and (not (x4 ?a))(x3 ?a)(x2 ?a)(x1 ?a))
                    )
                    (when
                        (and (x5 ?a)(not (x4 ?a))(not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                        (and (not (x5 ?a))(x4 ?a)(x3 ?a)(x2 ?a)(x1 ?a))
                    )
                    (when
                        (and (x6 ?a)(not (x5 ?a))(not (x4 ?a))(not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                        (and (not (x6 ?a))(x5 ?a)(x4 ?a)(x3 ?a)(x2 ?a)(x1 ?a))
                    )
                    (when
                        (and (x7 ?a)(not (x6 ?a))(not (x5 ?a))(not (x4 ?a))(not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                        (and (not (x7 ?a))(x6 ?a)(x5 ?a)(x4 ?a)(x3 ?a)(x2 ?a)(x1 ?a))
                    )
                    (when
                        (and (x8 ?a)(not (x7 ?a))(not (x6 ?a))(not (x5 ?a))(not (x4 ?a))(not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                        (and (not (x8 ?a))(x7 ?a)(x6 ?a)(x5 ?a)(x4 ?a)(x3 ?a)(x2 ?a)(x1 ?a))
                    )
                    (when
                        (and (x9 ?a)(not (x8 ?a))(not (x7 ?a))(not (x6 ?a))(not (x5 ?a))(not (x4 ?a))(not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                        (and (not (x9 ?a))(x8 ?a)(x7 ?a)(x6 ?a)(x5 ?a)(x4 ?a)(x3 ?a)(x2 ?a)(x1 ?a))
                    )
                    (when
                        (and (not (x9 ?a))(not (x8 ?a))(not (x7 ?a))(not (x6 ?a))(not (x5 ?a))(not (x4 ?a))(not (x3 ?a))(not (x2 ?a))(not (x1 ?a)))
                        (and (x9 ?a)(x8 ?a)(x7 ?a)(x6 ?a)(x5 ?a)(x4 ?a)(x3 ?a)(x2 ?a)(x1 ?a))
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
                    (when
                        (and (x4 ?a)(x4 ?b))
                        (and (l4 ?a ?b))
                    )
                    (when
                        (and (not (x4 ?a))(not (x4 ?b)))
                        (and (l4 ?a ?b))
                    )
                    (when
                        (and (x5 ?a)(x5 ?b))
                        (and (l5 ?a ?b))
                    )
                    (when
                        (and (not (x5 ?a))(not (x5 ?b)))
                        (and (l5 ?a ?b))
                    )
                    (when
                        (and (x6 ?a)(x6 ?b))
                        (and (l6 ?a ?b))
                    )
                    (when
                        (and (not (x6 ?a))(not (x6 ?b)))
                        (and (l6 ?a ?b))
                    )
                    (when
                        (and (x7 ?a)(x7 ?b))
                        (and (l7 ?a ?b))
                    )
                    (when
                        (and (not (x7 ?a))(not (x7 ?b)))
                        (and (l7 ?a ?b))
                    )
                    (when
                        (and (x8 ?a)(x8 ?b))
                        (and (l8 ?a ?b))
                    )
                    (when
                        (and (not (x8 ?a))(not (x8 ?b)))
                        (and (l8 ?a ?b))
                    )
                    (when
                        (and (x9 ?a)(x9 ?b))
                        (and (l9 ?a ?b))
                    )
                    (when
                        (and (not (x9 ?a))(not (x9 ?b)))
                        (and (l9 ?a ?b))
                    )
(not (z ?a))
(not (z ?b))
                )
            )
        )
        