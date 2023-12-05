(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (sunexposure_time) 50.0)
		(= (SoC b2) 80.0)
		(= (roverenergy) 0.0)
		(off b2)
		(gboff GB)
		(off b1)
	)
	(:goal
			(and
				(datasent)
			)
	)
)