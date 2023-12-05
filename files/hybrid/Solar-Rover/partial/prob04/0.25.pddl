(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (sunexposure_time) 200.0)
		(night)
		(off b2)
	)
	(:goal
			(and
				(datasent)
			)
	)
)