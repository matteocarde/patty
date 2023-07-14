(define (domain motion_planning_v3)

;(:requirements :typing :fluents)

(:types   obstacle entity - object
          waypoint rover - entity
)

(:predicates
          (collected_soil_sample ?w - waypoint)
          (fired_laser_at ?w - waypoint)
          (taken_picture ?w - waypoint)
)

(:functions (x ?e - entity)
            (y ?e - entity)
            (max_y)
            (max_x)
            (min_y)
            (min_x)
            (max_energy ?r - rover)
            (energy ?r - rover)
            (a1 ?o - object)
            (b1 ?o - object)
            (c1 ?o - object)
            (a2 ?o - object)
            (b2 ?o - object)
            (c2 ?o - object)
            (a3 ?o - object)
            (b3 ?o - object)
            (c3 ?o - object)
            (a4 ?o - object)
            (b4 ?o - object)
            (c4 ?o - object)
)

  ;; @action@ ["take_picture",[0,0]]
  (:action take_picture
    :parameters (?r - rover ?w - waypoint)
    :precondition (and
                      (<= (+ (* (x ?r) (a1 ?w)) (* (y ?r) (b1 ?w))) (c1 ?w))
                      (<= (+ (* (x ?r) (a2 ?w)) (* (y ?r) (b2 ?w))) (c2 ?w))
                      (<= (+ (* (x ?r) (a3 ?w)) (* (y ?r) (b3 ?w))) (c3 ?w))
                  )
    :effect(and (taken_picture ?w))
  )

  ;; @action@ ["take_soil_sample",[0,0]]
  (:action take_soil_sample
    :parameters (?r - rover ?w - waypoint)
    :precondition (and
                      (>= (+ (* (x ?r) (a1 ?w)) (* (y ?r) (b1 ?w))) (c1 ?w))
                      (>= (+ (* (x ?r) (a2 ?w)) (* (y ?r) (b2 ?w))) (c2 ?w))
                      (>= (+ (* (x ?r) (a3 ?w)) (* (y ?r) (b3 ?w))) (c3 ?w))
                      (>= (+ (* (x ?r) (a4 ?w)) (* (y ?r) (b4 ?w))) (c4 ?w))
                  )
    :effect(and (collected_soil_sample ?w))
  )

  ;; @action@ ["take_rock_sample",[0,0]]
  (:action take_rock_sample
    :parameters (?r - rover ?w - waypoint)
    :precondition (and
                      (<= (+ (* (x ?r) (a1 ?w)) (* (y ?r) (b1 ?w))) (c1 ?w))
                      (<= (+ (* (x ?r) (a2 ?w)) (* (y ?r) (b2 ?w))) (c2 ?w))
                      (<= (+ (* (x ?r) (a3 ?w)) (* (y ?r) (b3 ?w))) (c3 ?w))
                  )
    :effect (and (fired_laser_at ?w))
  )


    ;; @action@ ["move_up",[0,1]]
  (:action move_up
   :parameters (?r - rover)
   :precondition (and (> (energy ?r) 1) (< (+ (y ?r) 1) (max_y)))
   :effect (and
  		(increase (y ?r) 1)
      (decrease (energy ?r) 1)
      )
  )

  ;; @action@ ["move_down",[0,-1]]
  (:action move_down
   :parameters (?r - rover)
   :precondition (and (> (energy ?r) 1) (> (- (y ?r) 1) (min_y)))
   :effect (and
  		(decrease (y ?r) 1)
      (decrease (energy ?r) 1)
      )
  )

  ;; @action@ ["move_right",[1,0]]
  (:action move_right
   :parameters (?r - rover)
   :precondition (and (> (energy ?r) 1) (< (+ (x ?r) 1) (max_x)))
   :effect (and
  		(increase (x ?r) 1)
      (decrease (energy ?r) 1)
      )
  )

  ;; @action@ ["move_left",[-1,0]]
  (:action move_left
   :parameters (?r - rover)
   :precondition (and (> (energy ?r) 1) (> (- (x ?r) 1) (min_x)))
   :effect (and
  		(decrease (x ?r) 1)
      (decrease (energy ?r) 1)
      )

  )

  ;; @action@ ["move_up_left",[-1,1]]
  (:action move_up_left
   :parameters (?r - rover)
   :precondition (and (> (energy ?r) 1.5) (> (- (x ?r) 1) (min_x)) (< (+ (y ?r) 1) (max_y)))
   :effect (and
      (increase (y ?r) 1)
      (decrease (x ?r) 1)
      (decrease (energy ?r) 1.5)
      )

  )

  ;; @action@ ["move_up_right",[1,1]]
  (:action move_up_right
   :parameters (?r - rover)
   :precondition (and (> (energy ?r) 1.5) (< (+ (x ?r) 1) (max_x)) (< (+ (y ?r) 1) (max_y)))
   :effect (and
      (increase (y ?r) 1) (increase (x ?r) 1)
      (decrease (energy ?r) 1.5)
      )
  )

  ;; @action@ ["move_down_left",[-1,-1]]
  (:action move_down_left
   :parameters (?r - rover)
   :precondition (and (> (energy ?r) 1.5) (> (- (x ?r) 1) (min_x)) (> (- (y ?r) 1) (min_y)))
   :effect (and
      (decrease (x ?r) 1) (decrease (y ?r) 1)
      (decrease (energy ?r) 1.5)
      )
  )

  ;; @action@ ["move_down_right",[1,-1]]
  (:action move_down_right
  :parameters (?r - rover)
  :precondition (and (> (energy ?r) 1.5) (< (+ (x ?r) 1) (max_x)) (> (- (y ?r) 1) (min_y)))
  :effect (and
    (decrease (y ?r) 1) (increase (x ?r) 1)
    (decrease (energy ?r) 1.5)
    )
  )

  ;; @action@ ["recharge",[0,0]]
  (:action recharge
    :parameters (?r - rover)
    :precondition (and (<= (+ (energy ?r) 10) (max_energy ?r) ) )
    :effect (and
                (increase (energy ?r) 10)
            )
  )

  (:constraint never_run_dry
    :parameters (?r - rover)
    :condition (and (> (energy ?r) 0))
  )

  (:constraint never_trespasses_energy_capacity
    :parameters (?r - rover)
    :condition (and (>= (max_energy ?r) (energy ?r) ))
  )

  (:constraint bounding_box
      :parameters (?r - rover ?o - obstacle)
      :condition (or (>= (+ (* (x ?r) (a1 ?o)) (* (y ?r) (b1 ?o))) (c1 ?o))
                     (>= (+ (* (x ?r) (a2 ?o)) (* (y ?r) (b2 ?o))) (c2 ?o))
                     (>= (+ (* (x ?r) (a3 ?o)) (* (y ?r) (b3 ?o))) (c3 ?o))
                     (>= (+ (* (x ?r) (a4 ?o)) (* (y ?r) (b4 ?o))) (c4 ?o))
                 )
  )

)
