(define (problem run-generator2)
	(:domain generator)
	(:objects
		GB - generalBattery
		b1 b2 b3 - battery
	)
	(:init
		(datatosend)
		(night)
		(off b2)
		(= (roverenergy) 0.0)
		(= (SoC b1) 40.0)
		(= (sunexposure_time) 50.0)
		(= (SoC b2) 80.0)
		(gboff GB)
		(= (time) 0.0)
	)
	(:goal
			(and
				(datasent)
			)
	)
)