(define (domain generator2)
	;(:requirements :fluents :durative-actions :duration-inequalities :adl :typing :time)
	(:types
		generalBattery battery
	)
	(:predicates
		(alwaysfalse)
		(edge)
		(gboff ?gb - generalBattery)
		(gbon ?gb - generalBattery)
		(off ?b - battery)
		(on ?b - battery)
		(night)
		(sunexposure)
		(solarsupport)
		(datatosend)
		(datasent)
		(roversafe)
	)
	(:functions
		(ck)
		(tk)
		(delta)
		(roverenergy)
		(SoC ?b - battery)
		(time)
		(sunexposure_time)
	)

	(:event tic
		:parameters ()
		:precondition (and
			(= (ck) (+ (tk) #t))
		)
		:effect (and
			(assign (tk) (- (+ (ck) (delta)) #t))
		)
	)

	(:process ticking
		:parameters ()
		:precondition (and
		)
		:effect (and
			(increase (ck) (* #t 1.0))
		)
	)

	(:action switchGenBatteryOn
		:parameters (?gb - generalBattery)
		:precondition ( and
			(= (ck) (tk))
			(gboff ?gb)

		)
		:effect (and
			(gbon ?gb) (not (gboff ?gb))
			(roversafe)
			(increase (roverenergy) 100)
		)
	)

	(:action start_useBattery
		:parameters (?b - battery)
		:precondition (and
			(= (ck) (tk))
			(off ?b))
		:effect (and
			(increase (roverenergy) 10)
			(on ?b)
			(not (off ?b))
		)
	)

	(:process useBattery
		:parameters (?b - battery)
		:precondition (and (on ?b) (roversafe) (> (SoC ?b) 0))
		:effect (and(decrease (SoC ?b) (* #t 1)))
	)

	(:event end_useBattery
		:parameters (?b - battery)
		:precondition (and (on ?b) (or (not (roversafe)) (not (> (SoC ?b) 0))))
		:effect (and(not (on ?b)))
	)

	(:event sunshine
		:parameters ()
		:precondition (and (night) (sunexposure))
		:effect (and (not (night)) (increase (roverenergy) 400))
	)

	(:event sunexposure_event
		:parameters ()
		:precondition (and (>= (time) (sunexposure_time)) (not (sunexposure)))
		:effect (and(sunexposure))
	)

	(:action sendData
		:parameters ()
		:precondition (and
			(= (ck) (tk))
			(datatosend)
			(roversafe)
			(>= (roverenergy) 500)
		)
		:effect (and (datasent) (not (datatosend)))
	)

	(:process passingTime
		:parameters ()
		:precondition (and(not(alwaysfalse)))
		:effect (and(increase (time) (* #t 1)))

	)

)