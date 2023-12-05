(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(= (SoC b2) 80.0)
		(off b2)
		(off b1)
		(= (roverenergy) 0.0)
		(= (time) 0.0)
		(gboff GB)
		(= (sunexposure_time) 200.0)
		(night)
		(= (SoC b3) 100.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)