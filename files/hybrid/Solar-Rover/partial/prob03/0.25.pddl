(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (sunexposure_time) 150.0)
		(off b2)
		(= (time) 0.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)