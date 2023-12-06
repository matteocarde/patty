(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (roverenergy) 0.0)
		(= (SoC b2) 80.0)
		(datatosend)
		(off b3)
		(= (SoC b3) 100.0)
		(= (SoC b1) 40.0)
		(gboff GB)
		(off b1)
		(= (sunexposure_time) 150.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)