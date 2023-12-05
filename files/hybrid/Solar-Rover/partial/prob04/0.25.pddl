(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(off b2)
		(night)
		(off b3)
	)
	(:goal
			(and
				(datasent)
			)
	)
)