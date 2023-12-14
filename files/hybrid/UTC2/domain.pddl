(define (domain urbantraffic)
;;(:requirements :typing :fluents :time :timed-initial-literals :duration-inequalities :adl)

(:types junction link stage)

(:predicates 
(controllable ?i - junction)
(inter ?p - stage)
(active ?p - stage)
(next ?p ?p1 - stage)
(trigger ?i - junction)
(contains ?i - junction ?p - stage)
)

(:functions 
(turnrate ?x - stage ?r1 - link  ?r2 - link) 
(interlimit ?p - stage)
(occupancy ?r - link) 
(capacity ?r - link) 
(maxgreentime  ?p - stage ) 
(mingreentime ?p - stage ) 
(defaultgreentime ?p - stage ) 
(greentime ?i - junction)
(intertime ?i - junction)
(granularity)
(counter ?r - link) 
(maxcycletime  ?i - junction)
(cycletime  ?i - junction)
(mincycletime  ?i - junction)
)

;; the maximum time limit for green has been reached, but no need to restart token!
(:event defgreenreached
 :parameters (?p - stage ?i - junction)
 :precondition (and 
	(active ?p) (contains ?i ?p)
	(>= (greentime ?i) (defaultgreentime ?p))
	)
  :effect (and
	(trigger ?i)
	)
)

;; process that keeps the green/intergreen on, and updates the greentime value
(:process keepgreen
:parameters (?p - stage ?i - junction)
:precondition (and 
		(active ?p) (contains ?i ?p)
                (< (greentime ?i) (defaultgreentime ?p))
)
:effect (and
		(increase (greentime ?i) (* #t 1 ) )
))



;;allows car to flow if the corresponding green is on
(:process flowrun_green
:parameters (?p - stage ?r1 ?r2 - link)
:precondition (and 
		(active ?p)
		(> (occupancy ?r1) 0.0)
		(> (turnrate ?p ?r1 ?r2) 0.0)
		(< (occupancy ?r2) (capacity ?r2))
)
:effect (and
		(increase (occupancy ?r2) (* #t (turnrate ?p ?r1 ?r2)))
		(decrease (occupancy ?r1) (* #t (turnrate ?p ?r1 ?r2)))
    (increase (counter ?r2) (* #t (turnrate ?p ?r1 ?r2)))
))
;; let the planner in control to stop the green before maxgreen

(:action extendStage
:parameters (?p1 - stage ?i - junction)
:precondition (and
		(controllable ?i)
		(contains ?i ?p1)
    ;;   	(active ?p1)
		(< (+ (defaultgreentime ?p1) (granularity)) (maxgreentime ?p1) )
        (< (+ (cycletime ?i) (granularity)) (maxcycletime ?i))
		)
:effect (and 
		(increase (defaultgreentime ?p1) (granularity))
        (increase (cycletime ?i) (granularity))
))

(:action reduceStage
:parameters (?p1 - stage ?i - junction)
:precondition (and
		(controllable ?i)
		(contains ?i ?p1)
	  ;; 	(active ?p1)
		(> (- (defaultgreentime ?p1) (granularity)) (mingreentime ?p1) )
        (> (- (cycletime ?i) (granularity)) (mincycletime ?i))
		)
:effect (and 
		(decrease (defaultgreentime ?p1) (granularity))
        (decrease (cycletime ?i) (granularity))
))

(:process handle_time
:parameters()
:precondition ()
:effect (and (increase (time) (* #t 1 )))
)


(:event trigger-inter
:parameters (?p - stage ?i - junction)
 :precondition (and
        (trigger ?i)
        (active ?p) (contains ?i ?p)
        )
  :effect (and
        (not (trigger ?i))
        (not (active ?p))
        (inter ?p)
	(assign (greentime ?i) 0)
        )
)



(:process keepinter
  :parameters (?p - stage ?i - junction)
  :precondition (and 
      (inter ?p) (contains ?i ?p)
      (< (intertime ?i) (interlimit ?p)  )
   )
   :effect (and
      (increase (intertime ?i) (* #t 1 ) )
   ))

(:event trigger-change
:parameters (?p ?p1 - stage ?i - junction)
 :precondition (and 
	(inter ?p) (contains ?i ?p)
        (next ?p ?p1)
        (>= (intertime ?i) (- (interlimit ?p) 0.1)  )
	)
  :effect (and
	(not (inter ?p))
        (active ?p1)
	(assign (intertime ?i) 0)
	)
)

)
