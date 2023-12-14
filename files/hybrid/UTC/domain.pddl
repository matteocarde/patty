(define (domain urbantraffic)
	(:requirements :typing :durative-actions :fluents :time :adl)

	(:types
		intersection road buffer
	)

	(:predicates
		(saturated ?r - road)
		(normal ?r - road)
		(active ?i - intersection ?r - road)
		(bufferconnected ?b - buffer ?r - road)
		(availableflow ?r1 - road ?r2 - road ?i - intersection)
		(gotcars ?b - buffer)

	)

	(:functions
		(flow ?r1 - road ?r2 - road ?i - intersection)
		(queue ?r - road)
		(max_queue ?r - road)
		(saturated_queue ?r - road)
		(maxgreentime ?i - intersection)
		(mingreentime ?i - intersection)
		(greentime ?i - intersection)
		(token ?i - intersection)
		(tokenvalue ?r - road ?i - intersection)
		(maxtoken ?i - intersection)
		(carsinbuffer ?b - buffer)
	)

	;;; **** structure for cycling among traffic signals ****

	;; token has to be restarted, but the maximum time limit for green has NOT been reached! --> i.e., things have been changed by the switch action
	(:event restartoken
		:parameters (?i - intersection)
		:precondition (and
			;; Two issues here: an event cannot reliably use < or > because it is open and also it really needs a boolean precondition because
			;; it must falsify precondition
			(<= (greentime ?i) (- (maxgreentime ?i) 10))
			(>= (token ?i) (+ (maxtoken ?i) 10))
		)
		:effect (and
			(assign (greentime ?i) 0)
			(assign (token ?i) 10)
		)
	)

	;; the maximum time limit for green has been reached and next round token must be restarted!
	(:event maxgreenreachedANDmaxtoken
		:parameters (?i - intersection)
		:precondition (and
			(>= (greentime ?i) (maxgreentime ?i))
			(= (token ?i) (maxtoken ?i))
		)
		:effect (and
			(assign (greentime ?i) 0)
			(assign (token ?i) 10)
		)
	)

	;; the maximum time limit for green has been reached, but no need to restart token!
	(:event maxgreenreachedANDNOTmaxtoken
		:parameters (?i - intersection)
		:precondition (and
			(>= (greentime ?i) (maxgreentime ?i))
			(< (token ?i) (maxtoken ?i))
		)
		:effect (and
			(assign (greentime ?i) 0)
			(increase (token ?i) 10)
		)
	)

	;; process that keeps the green on, and updates the greentime value
	(:process keepgreen
		:parameters (?r1 - road ?i - intersection)
		:precondition (and
			(active ?i ?r1)
			(= (token ?i) (tokenvalue ?r1 ?i))
			(< (greentime ?i) (maxgreentime ?i))
		)
		:effect (and
			(increase (greentime ?i) (* #t 1))
		)
	)

	;;allows car to flow if the corresponding green is on
	(:process flowrun_green
		:parameters (?r1 ?r2 - road ?i - intersection)
		:precondition (and
			(availableflow ?r1 ?r2 ?i)
			(active ?i ?r1)
			(= (token ?i) (tokenvalue ?r1 ?i))
			(> (queue ?r1) 0)
			(< (queue ?r2) (max_queue ?r2))
			(< (greentime ?i) (maxgreentime ?i))
		)
		:effect (and
			(increase (queue ?r2) (* #t (flow ?r1 ?r2 ?i)))
			(decrease (queue ?r1) (* #t (flow ?r1 ?r2 ?i)))

		)
	)

	;; let the planner in control to stop the green before maxgreen
	(:action switchTrafficSignal
		:parameters (?i - intersection)
		:precondition (>= (greentime ?i) (mingreentime ?i))
		:effect (and
			(increase (token ?i) 10)
			(assign (greentime ?i) 0)
		)
	)

	;;; **** bufferisation for adding cars to the network ****

	(:event releasecar
		:parameters (?b - buffer ?r - road)
		:precondition (and
			(gotcars ?b)
			(>= (carsinbuffer ?b) 1)
			(bufferconnected ?b ?r)
		)
		:effect (and
			(not (gotcars ?b))
			(increase (queue ?r) (carsinbuffer ?b))
			(assign (carsinbuffer ?b) 0)
		)
	)

)