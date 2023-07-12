;Header and description

(define (domain domain_name)

  ;remove requirements that are not needed
  (:requirements :strips :)

  (:types
    switch
  )

  (:predicates
    (p ?s - switch)
    (next ?a ?b - switch)
  )

  (:action toggle
    :parameters (?a ?b - switch)
    :precondition (and
      (next ?a ?b)
      (p?a)
      (not (p ?b))
    )
    :effect (and
      (not (p ?a))
      (p ?b)
    )
  )

)