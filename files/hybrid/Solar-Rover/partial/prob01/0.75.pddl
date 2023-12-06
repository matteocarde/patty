(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (sunexposure_time) 50.0)
		(= (roverenergy) 0.0)
		(off b2)
		(off b1)
		(gboff GB)
		(= (SoC b2) 80.0)
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