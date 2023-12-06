(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (SoC b3) 100.0)
		(= (roverenergy) 0.0)
		(= (SoC b1) 40.0)
		(off b2)
		(= (sunexposure_time) 100.0)
		(= (SoC b2) 80.0)
		(= (time) 0.0)
		(night)
		(gboff GB)
	)
	(:goal
			(and
				(datasent)
			)
	)
)