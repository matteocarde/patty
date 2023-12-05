(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(datatosend)
		(off b2)
		(= (sunexposure_time) 100.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)