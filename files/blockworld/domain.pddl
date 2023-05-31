(define (domain blocksworld)
  (:requirements :strips :equality)
  (:types
    obj
  )
  (:predicates
    (clear ?x - obj)
    (on-table ?x - obj)
    (arm-empty)
    (holding ?x - obj)
    (on ?x - obj ?y - obj)
  )

  (:action pickup
    :parameters (?ob - obj)
    :precondition (and (clear ?ob) (on-table ?ob) (arm-empty))
    :effect (and (holding ?ob) (not (clear ?ob)) (not (on-table ?ob))
      (not (arm-empty)))
  )

  (:action putdown
    :parameters (?ob - obj)
    :precondition (and (holding ?ob))
    :effect (and (clear ?ob) (arm-empty) (on-table ?ob)
      (not (holding ?ob)))
  )

  (:action stack
    :parameters (?ob - obj ?underob - obj)
    :precondition (and (clear ?underob) (holding ?ob))
    :effect (and (arm-empty) (clear ?ob) (on ?ob ?underob)
      (not (clear ?underob)) (not (holding ?ob)))
  )

  (:action unstack
    :parameters (?ob - obj ?underob - obj)
    :precondition (and (on ?ob ?underob) (clear ?ob) (arm-empty))
    :effect (and (holding ?ob) (clear ?underob)
      (not (on ?ob ?underob)) (not (clear ?ob)) (not (arm-empty)))
  )
)