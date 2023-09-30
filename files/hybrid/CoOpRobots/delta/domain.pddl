(define (domain robots)

  ;(:requirements :fluents :durative-actions :duration-inequalities :adl :typing :time)
  (:types
    robot room obj
  )

  (:predicates
    (atRobot ?r - robot ?l - room)
    (atObject ?o - obj ?l - room)
    (allowed ?r - robot ?l - room)
    (holding ?r - robot ?o - obj)
    (handsFull ?r - robot)
    (moving ?r - robot ?a - room ?b - room)
    (inMovement ?r - robot)
    (charging ?r - robot)
    (link ?a - room ?b - room)
  )
  (:functions
    (speed ?r - robot)
    (dischargeRate ?r - robot)
    (battery ?r - robot)
    (distance ?a - room ?b - room)
    (distanceRun ?r - robot ?a - room ?b - room)
    (d ?r - robot)
    (tk ?r - robot)
    (time)
    (deltaMovement ?r - robot)
    (deltaCharging ?r - robot)
  )

  (:action startMoving
    :parameters (?r - robot ?a - room ?b - room)
    :precondition (and
      (= (time) (tk ?r))
      (link ?a ?b)
      (not (inMovement ?r))
      (atRobot ?r ?a)
      (allowed ?r ?b)
      (handsFull ?r)
    )
    :effect (and
      (not (atRobot ?r ?a))
      (moving ?r ?a ?b)
      (inMovement ?r)
      (assign (distanceRun ?r ?a ?b) 0)
      (assign (d ?r) (deltaMovement ?r))
      (assign (tk ?r) (time))
      (assign (charges ?r) 0)
    )
  )

  (:process moving
    :parameters (?r - robot ?a - room ?b - room)
    :precondition (and
      (link ?a ?b)
      (moving ?r ?a ?b)
      (inMovement ?r)
      (< (distanceRun ?r ?a ?b) (distance ?a ?b))
      (>= (battery ?r) 20)
    )
    :effect (and
      (increase
        (distanceRun ?r ?a ?b)
        (* (speed ?r) #t))
    )
  )

  (:event endMoving
    :parameters (?r - robot ?a - room ?b - room)
    :precondition (and
      (link ?a ?b)
      (moving ?r ?a ?b)
      (inMovement ?r)
      (>= (battery ?r) 20)
      (>= (distanceRun ?r ?a ?b) (distance ?a ?b))
    )
    :effect (and
      (atRobot ?r ?b)
      (not (moving ?r ?a ?b))
      (not (inMovement ?r))
    )
  )

  (:action startCharging
    :parameters (?r - robot)
    :precondition (and
      (= (time) (tk ?r))
      (>= (battery ?r) 20)
      (inMovement ?r)
    )
    :effect (and
      (not (inMovement ?r))
      (charging ?r)
      (assign (d ?r) (deltaCharging ?r))
      (assign (tk ?r) (time))
    )
  )

  (:process charging
    :parameters (?r - robot)
    :precondition (and
      (charging ?r)
      (< (battery ?r) 100)
    )
    :effect (and
      (increase (battery ?r) (* #t 1))
    )
  )

  (:process discharging
    :parameters (?r - robot)
    :precondition (and
      (handsFull ?r)
      (not (charging ?r))
      (>= (battery ?r) 0)
    )
    :effect (and
      (decrease
        (battery ?r)
        (* #t (* (speed ?r) (dischargeRate ?r))))
    )
  )

  (:action stopCharging
    :parameters (?r - robot)
    :precondition (and
      (= (time) (tk ?r))
      (charging ?r)
    )
    :effect (and
      (not (charging ?r))
      (inMovement ?r)
      (assign (d ?r) (deltaMovement ?r))
      (assign (tk ?r) (time))
    )
  )

  (:action pick
    :parameters (?o - obj ?r - robot ?l - room)
    :precondition (and
      (= (time) (tk ?r))
      (>= (battery ?r) 20)
      (atRobot ?r ?l)
      (atObject ?o ?l)
      (not (handsFull ?r))
    )
    :effect (and
      (holding ?r ?o)
      (not (atObject ?o ?l))
      (handsFull ?r)
    )
  )

  (:action drop
    :parameters (?o - obj ?r - robot ?l - room)
    :precondition (and
      (= (time) (tk ?r))
      (>= (battery ?r) 20)
      (atRobot ?r ?l)
      (holding ?r ?o)
    )
    :effect (and
      (not (holding ?r ?o))
      (atObject ?o ?l)
      (not (handsFull ?r))
    )
  )

  (:event tic
    :parameters (?r - robot)
    :precondition (and
      (> (d ?r) 0)
      (= (time) (+ (tk ?r) #t))
    )
    :effect (and
      (assign (tk ?r) (- (+ (time) (d ?r)) #t))
    )
  )

  (:process ticking
    :parameters ()
    :precondition (or
      (exists
        (?r - robot ?a - room ?b - room)
        (and
          (link ?a ?b)
          (moving ?r ?a ?b)
          (inMovement ?r)
          (< (distanceRun ?r ?a ?b) (distance ?a ?b))
          (>= (battery ?r) 20)
        )
      )
      (exists
        (?r - robot)
        (and
          (charging ?r)
          (< (battery ?r) 100)
        )
      )
      (exists
        (?r - robot)
        (and
          (handsFull ?r)
          (not (charging ?r))
          (>= (battery ?r) 0)
        )
      )
    )
    :effect (and
      (increase (time) (* #t 1.0))
    )
  )

)