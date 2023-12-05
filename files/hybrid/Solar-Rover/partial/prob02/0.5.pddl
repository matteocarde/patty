(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (SoC b2) 80.0)
		(datatosend)
		(off b3)
		(= (SoC b1) 40.0)
		(= (sunexposure_time) 100.0)
		(= (roverenergy) 0.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)