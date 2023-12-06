(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (SoC b2) 80.0)
		(datatosend)
		(= (sunexposure_time) 150.0)
		(= (SoC b1) 40.0)
		(= (SoC b3) 100.0)
		(= (time) 0.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)