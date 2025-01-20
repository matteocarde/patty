(define (domain tapes)
	(:requirements :strips :equality :conditional-effects)
	(:types
		robot tape cell counter
	)
	(:predicates
		(onTape ?r - robot ?t - tape)
		(onCellRobot ?r - robot ?c - cell)
		(onCellCounter ?a - counter ?t - tape ?c - cell)
		(connected ?r - robot ?a - counter)
		(connected ?r - robot)
		(startCell ?c - cell)
		(isNextCell ?c1 - cell ?c2 - cell)
		(isNextTape ?t1 - tape ?t2 - tape)
		;#COUNTERS#
	)

	(:action connect
		:parameters (?r - robot ?t - tape ?c - cell ?a - counter)
		:precondition(and
			(onTape ?r ?t)
			(onCellRobot ?r ?c)
			(onCellCounter ?a ?t ?c)
			(not (connected ?r ?a))
		)
		:effect (and
			(connected ?r ?a)
			(connected ?r)
		)
	)

	(:action disconnect
		:parameters (?r - robot ?a - counter)
		:precondition(and
			(connected ?r ?a)
		)
		:effect (and
			(not (connected ?r ?a))
			(not (connected ?r))
		)
	)

	(:action mv
		:parameters (?r - robot ?t - tape)
		:precondition(and
			(onTape ?r ?t)
			(not (connected ?r))
		)
		:effect(and
			(forall
				(?from - cell ?to - cell)
				(when
					(and
						(isNextCell ?from ?to)
						(onCellRobot ?r ?from)
					)
					(and
						(not (onCellRobot ?r ?from))
						(onCellRobot ?r ?to)
					)
				)
			)
		)
	)

	(:action change
		:parameters (?r - robot ?c - cell)
		:precondition(and
			(startCell ?c)
			(onCellRobot ?r ?c)
		)
		:effect(and
			(forall
				(?from - tape ?to - tape ?c - cell)
				(when
					(and
						(onTape ?r ?from)
						(isNextTape ?from ?to)
					)
					(and
						(not (onTape ?r ?from))
						(onTape ?r ?to)
					)
				)
			)
		)
	)

	;#INCR#


)