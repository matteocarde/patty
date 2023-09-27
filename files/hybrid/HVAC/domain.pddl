;;Planning for controlling hvac (Heating, Ventilation and  Air-Conditioning). First very coarse abstraction, which uses a discrete interepretation of the problem where #t = 1 
;;and ignores many thermal aspects of the problem
(define (domain hvac)
   ;(:requirements :fluents :durative-actions :duration-inequalities :adl :typing :time)
   (:types
      room request -object
   )
   (:predicates
      (alwaysfalse)
      (satisfied ?r -request)
   )
   (:functions
      (air-flow ?l -room) ;; air-flow rate 
      (temp ?l -room) ;;temperature of the room. This variable is not controlled directly
      (temp_sa ?l -room) ;;supply air temperature. This variable is controlled directly
      (time) ;; this keeps track of the time. This is meant to allow us to capture the specific time-slot
      (time_requested ?l -room ?r -request) ;; this captures the time slot of interest. Depending on the request there could be many of them
      (temp_requested ?l -room ?r -request) ;; this models the particular temperature request
      (comfort) ;; this is a constant regulating the actual difference between the desired and the perceived temperature
   )

   (:action satisfier
      :parameters (?l -room ?r -request)
      :precondition (and (<= (temp ?l) (+ (temp_requested ?l ?r) (comfort))) (>= (temp ?l) (- (temp_requested ?l ?r) (comfort))) (= (time) (time_requested ?l ?r)))
      :effect (and (satisfied ?r))
   )

   (:constraint temperature_domain
      :parameters (?l -room)
      ;;Constraint on the possible temperature in a room
      :condition (and (<= (temp ?l) 30) (>= (temp ?l) 10))
   )

   ;; this process models the passing of time
   (:process time_passing
      :parameters ()
      :precondition (and(not(alwaysfalse)))
      :effect (increase (time) (* #t 1))
   )

   ;; this process models how the temperature changes along the time according to the air-flow and the temp_sa. Many other parameters have to be added. 
   ;; At this stage the temperature of the room uniquely depends on the enthalpy
   (:process thermal_change
      :parameters (?l -room)
      :precondition (and(not(alwaysfalse)))
      :effect (and (increase
            (temp ?l)
            (* #t (* (air_flow ?l) (- (temp_sa ?l) (temp ?l))))))
   )

   ;; the next actions model the intervention on the air_flow and on the supply air temperature
   (:action increase_air_flow
      :parameters (?l -room)
      :precondition (and (<= (air_flow ?l) 3))
      :effect (and(increase (air_flow ?l) 1))
   )

   (:action decrease_air_flow
      :parameters (?l -room)
      :precondition (and (>= (air_flow ?l) 1))
      :effect (and(decrease (air_flow ?l) 1))
   )

   (:action increase_temp
      :parameters (?l -room)
      :precondition (and (<= (temp_sa ?l) 29))
      :effect (and(increase (temp_sa ?l) 1))
   )

   (:action decrease_temp
      :parameters (?l -room)
      :precondition (and (>= (temp_sa ?l) 11))
      :effect (and(decrease (temp_sa ?l) 1))
   )

)