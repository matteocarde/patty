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
		(x01 ?c - counter)
		(x02 ?c - counter)
		(x03 ?c - counter)
		(x04 ?c - counter)
		(x05 ?c - counter)
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

	
                (:action incr
                    :parameters (?r - robot ?a - counter)
                    :precondition(and
                        (connected ?r ?a)
                    )
                    :effect(and
                                            (when
                        (and (not (x01 ?a)))
                        (and (x01 ?a))
                    )
                    (when
                        (and (not (x02 ?a))(x01 ?a))
                        (and (x02 ?a)(not (x01 ?a)))
                    )
                    (when
                        (and (not (x03 ?a))(x02 ?a)(x01 ?a))
                        (and (x03 ?a)(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (not (x04 ?a))(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (x04 ?a)(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (not (x05 ?a))(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (x05 ?a)(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (not (x06 ?a))(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (x06 ?a)(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (not (x07 ?a))(x06 ?a)(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (x07 ?a)(not (x06 ?a))(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (not (x08 ?a))(x07 ?a)(x06 ?a)(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (x08 ?a)(not (x07 ?a))(not (x06 ?a))(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (not (x09 ?a))(x08 ?a)(x07 ?a)(x06 ?a)(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (x09 ?a)(not (x08 ?a))(not (x07 ?a))(not (x06 ?a))(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (not (x10 ?a))(x09 ?a)(x08 ?a)(x07 ?a)(x06 ?a)(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (x10 ?a)(not (x09 ?a))(not (x08 ?a))(not (x07 ?a))(not (x06 ?a))(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (not (x11 ?a))(x10 ?a)(x09 ?a)(x08 ?a)(x07 ?a)(x06 ?a)(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (x11 ?a)(not (x10 ?a))(not (x09 ?a))(not (x08 ?a))(not (x07 ?a))(not (x06 ?a))(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (not (x12 ?a))(x11 ?a)(x10 ?a)(x09 ?a)(x08 ?a)(x07 ?a)(x06 ?a)(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (x12 ?a)(not (x11 ?a))(not (x10 ?a))(not (x09 ?a))(not (x08 ?a))(not (x07 ?a))(not (x06 ?a))(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (not (x13 ?a))(x12 ?a)(x11 ?a)(x10 ?a)(x09 ?a)(x08 ?a)(x07 ?a)(x06 ?a)(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (x13 ?a)(not (x12 ?a))(not (x11 ?a))(not (x10 ?a))(not (x09 ?a))(not (x08 ?a))(not (x07 ?a))(not (x06 ?a))(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (not (x14 ?a))(x13 ?a)(x12 ?a)(x11 ?a)(x10 ?a)(x09 ?a)(x08 ?a)(x07 ?a)(x06 ?a)(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (x14 ?a)(not (x13 ?a))(not (x12 ?a))(not (x11 ?a))(not (x10 ?a))(not (x09 ?a))(not (x08 ?a))(not (x07 ?a))(not (x06 ?a))(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    (when
                        (and (x14 ?a)(x13 ?a)(x12 ?a)(x11 ?a)(x10 ?a)(x09 ?a)(x08 ?a)(x07 ?a)(x06 ?a)(x05 ?a)(x04 ?a)(x03 ?a)(x02 ?a)(x01 ?a))
                        (and (not (x14 ?a))(not (x13 ?a))(not (x12 ?a))(not (x11 ?a))(not (x10 ?a))(not (x09 ?a))(not (x08 ?a))(not (x07 ?a))(not (x06 ?a))(not (x05 ?a))(not (x04 ?a))(not (x03 ?a))(not (x02 ?a))(not (x01 ?a)))
                    )
                    )
                )
            

	(:constraints
		(and
			(forall
				(?r - robot ?c1 - cell ?c2 - cell)
				(and
					(not (= ?c1 ?c2))
					(or
						(not (onCellRobot ?r ?c1))
						(not (onCellRobot ?r ?c2))
					)
				)
			)
			(forall
				(?r - robot ?t1 - tape ?t2 - tape)
				(and
					(not (= ?t1 ?t2))
					(or
						(not (onTape ?r ?t1))
						(not (onTape ?r ?t2))
					)
				)
			)
			(exists
				(?r - robot ?c - cell)
				(and
					(onCellRobot ?r ?c)
				)
			)
			(exists
				(?r - robot ?t - tape)
				(and
					(onTape ?r ?t)
				)
			)
		)

	)

)